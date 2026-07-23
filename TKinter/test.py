import sounddevice as sd
from scipy.io.wavfile import write, read
import tkinter as tk
from tkinter import ttk
import threading
import whisper
import urllib.request
import urllib.parse
import json
import os
import tempfile
from PIL import Image, ImageTk
import io

# ── Config ──────────────────────────────────────────────────────────────────
SAMPLE_RATE = 44100
DURATION    = 5          # seconds to record
UNSPLASH_ACCESS_KEY = "YOUR_UNSPLASH_ACCESS_KEY"   # sign up free at unsplash.com/developers

# Load Whisper model once at startup (tiny = fast, base = more accurate)
print("⏳ Loading Whisper model...")
whisper_model = whisper.load_model("base")
print("✅ Whisper ready.")

# ── State ────────────────────────────────────────────────────────────────────
current_photo = None   # keep reference so GC doesn't collect it

# ── Core Functions ────────────────────────────────────────────────────────────
def record():
    """Record DURATION seconds of audio and save to output.wav."""
    set_status("🎙️  Recording… speak now!", "orange")
    btn_record.config(state="disabled")
    btn_play.config(state="disabled")

    def _do():
        audio = sd.rec(int(DURATION * SAMPLE_RATE),
                       samplerate=SAMPLE_RATE, channels=1, dtype="int16")
        sd.wait()
        write("output.wav", SAMPLE_RATE, audio)
        set_status("✅ Recording done — click 'Recognise & Show'", "green")
        btn_record.config(state="normal")
        btn_play.config(state="normal")
        btn_recognise.config(state="normal")

    threading.Thread(target=_do, daemon=True).start()


def play():
    """Play back the last recording."""
    if not os.path.exists("output.wav"):
        set_status("⚠️  No recording found.", "red")
        return

    def _do():
        set_status("🔊 Playing back…", "blue")
        rate, data = read("output.wav")
        sd.play(data, rate)
        sd.wait()
        set_status("✅ Done playing.", "green")

    threading.Thread(target=_do, daemon=True).start()


def transcribe_and_show():
    """Transcribe the WAV with Whisper then fetch a matching image."""
    if not os.path.exists("output.wav"):
        set_status("⚠️  Record something first.", "red")
        return

    btn_recognise.config(state="disabled")
    set_status("🧠 Transcribing with Whisper…", "purple")

    def _do():
        # 1. Transcribe
        result = whisper_model.transcribe("output.wav")
        text   = result["text"].strip()
        lbl_transcript.config(text=f'"{text}"')
        set_status(f"🔍 Searching images for: {text}", "blue")

        # 2. Fetch image from Unsplash
        query   = urllib.parse.quote(text)
        url     = (f"https://api.unsplash.com/search/photos"
                   f"?query={query}&per_page=1&orientation=landscape"
                   f"&client_id={UNSPLASH_ACCESS_KEY}")
        try:
            with urllib.request.urlopen(url, timeout=10) as r:
                data = json.loads(r.read())

            if not data["results"]:
                set_status("😕 No image found for that phrase.", "red")
                btn_recognise.config(state="normal")
                return

            img_url = data["results"][0]["urls"]["regular"]

            # 3. Download and display image
            with urllib.request.urlopen(img_url, timeout=15) as r:
                raw = r.read()

            img = Image.open(io.BytesIO(raw))
            img.thumbnail((700, 420), Image.LANCZOS)

            global current_photo
            current_photo = ImageTk.PhotoImage(img)
            lbl_image.config(image=current_photo, text="")
            set_status(f'✅ Showing image for: "{text}"', "green")

        except Exception as e:
            set_status(f"❌ Error: {e}", "red")

        btn_recognise.config(state="normal")

    threading.Thread(target=_do, daemon=True).start()


# ── Helpers ───────────────────────────────────────────────────────────────────
def set_status(msg, color="black"):
    lbl_status.config(text=msg, fg=color)
    root.update_idletasks()


# ── UI ────────────────────────────────────────────────────────────────────────
root = tk.Tk()
root.title("🎤 Voice → Image")
root.resizable(False, False)

BG       = "#0f0f11"
CARD     = "#1a1a1f"
ACCENT   = "#7c6af7"
BTN_FG   = "#ffffff"
LABEL_FG = "#c8c5e8"

root.configure(bg=BG)

# Title bar
frm_title = tk.Frame(root, bg=BG)
frm_title.pack(fill="x", padx=24, pady=(20, 4))
tk.Label(frm_title, text="Voice → Image", font=("SF Pro Display", 22, "bold"),
         bg=BG, fg=ACCENT).pack(side="left")
tk.Label(frm_title, text=f"  (records {DURATION}s)",
         font=("SF Pro Text", 11), bg=BG, fg="#555").pack(side="left", pady=4)

# Image canvas
frm_img = tk.Frame(root, bg=CARD, bd=0, relief="flat",
                   width=700, height=420)
frm_img.pack(padx=24, pady=(8, 8))
frm_img.pack_propagate(False)

lbl_image = tk.Label(frm_img, bg=CARD, fg="#444",
                     text="🎤  Say something and press  Record!",
                     font=("SF Pro Text", 14), wraplength=600, justify="center")
lbl_image.pack(expand=True)

# Transcript label
lbl_transcript = tk.Label(root, text="", font=("SF Pro Text", 13, "italic"),
                           bg=BG, fg=LABEL_FG, wraplength=660)
lbl_transcript.pack(pady=(0, 4))

# Status bar
lbl_status = tk.Label(root, text="Press Record to start.",
                      font=("SF Pro Text", 11), bg=BG, fg="#888")
lbl_status.pack(pady=(0, 10))

# Buttons
BTN_CFG = dict(font=("SF Pro Text", 13, "bold"), fg=BTN_FG,
               bd=0, padx=18, pady=9, cursor="hand2", relief="flat")

frm_btns = tk.Frame(root, bg=BG)
frm_btns.pack(pady=(0, 20))

btn_record    = tk.Button(frm_btns, text="🎙  Record",
                          bg="#e05252", activebackground="#c94444",
                          command=record, **BTN_CFG)
btn_play      = tk.Button(frm_btns, text="🔊  Play",
                          bg="#4a7fe5", activebackground="#3a6bcc",
                          command=play, **BTN_CFG)
btn_recognise = tk.Button(frm_btns, text="✨  Recognise & Show",
                          bg=ACCENT, activebackground="#6a59d9",
                          command=transcribe_and_show, state="disabled",
                          **BTN_CFG)

btn_record.grid   (row=0, column=0, padx=8)
btn_play.grid     (row=0, column=1, padx=8)
btn_recognise.grid(row=0, column=2, padx=8)

root.mainloop()