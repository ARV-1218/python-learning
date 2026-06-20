import requests #for creating request to the server
import tkinter as tk #basic gui


print("Definitions Generator :)")

# ---------------------------
# Create Main Window
# ---------------------------
root = tk.Tk()
root.title("Dictionary App")
root.state("zoomed")

# ---------------------------
# Input Label
# ---------------------------
lab = tk.Label(root, text="Enter a word:",font=("Arial",12))
lab.pack(pady=5)

# ---------------------------
# Entry Widget
# ---------------------------
entry = tk.Entry(root, width=30,font=("Arial",20))
entry.pack(pady=5)



frame = tk.Frame(root)

# ---------------------------
# Text Widget for Output
# ---------------------------
text_box = tk.Text(
    frame,
    width=100,
    height=30,
    fg="black",
    wrap="word" ,
    font=("Arial",12)
    # Prevents words from being cut in half
)
text_box.pack(pady=10,side="left",fill="both",expand=True)

scrollbar = tk.Scrollbar(frame,width=20)
scrollbar.pack(side="right", fill="y")

text_box.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_box.yview)

frame.pack()


# Make text box read-only initially
text_box.config(state="disabled")
def fetch(word):
    """
    Fetches definitions from dictionaryapi.dev
    and displays them inside the text box.
    """

    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    try:
        # Added timeout so the program doesn't hang forever
        response = requests.get(url, timeout=5)

    except requests.RequestException:
        # If internet connection fails
        text_box.config(state="normal")
        text_box.insert(tk.END, "Connection Error.\n")
        text_box.config(state="disabled")
        return

    # API returned data successfully
    if response.status_code == 200:

        data = response.json()
        wrd = data[0]['word']
        phonetic = data[0]['phonetic']
        
        audio_url = None

        for item in data[0]["phonetics"]:
            if item["audio"]:
                audio_url = item["audio"]
                break
            
        print(audio_url)
        if audio_url:
            re2 =  requests.get(audio_url,timeout=1)
            
            with open("word.mp3","wb") as f:
                f.write(re2.content)
            
        
        else:
            pass

        text_box.delete("1.0", tk.END)   # Clear previous search results
        
        text_box.config(state="normal")
         
        text_box.insert(tk.END,f"\n Word = {wrd} \n")
        text_box.insert(tk.END,f"\n Phonetic = {phonetic} \n")
        # Enable text box so we can write into it
       

    
       

        # Enumerate automatically creates numbering
        for index, meaning in enumerate(data[0]["meanings"], start=1):

            # Part of speech (noun, verb, adjective...)
            text_box.insert(tk.END,f"\n{index}. {meaning['partOfSpeech'].capitalize()}\n")
            

            # Definitions for that part of speech
            for definition in meaning["definitions"]:
                text_box.insert(
                    tk.END,
                    f"   → {definition['definition']}\n"
                )

        # Make text box read-only again
        text_box.config(state="disabled")

    else:
        text_box.config(state="normal")
        text_box.delete("1.0", tk.END)

        # Better error message for invalid words
        text_box.insert(
            tk.END,
            f"No definition found for '{word}'."
        )

        text_box.config(state="disabled")


def pressed():
    """
    Called when Enter is pressed.
    """

    # Remove accidental spaces
    word = entry.get().strip()

    if not word:
        return

    # Disable entry while request is processing
    entry.config(state="disabled")
    root.update()

    fetch(word)

    # Re-enable entry afterwards
    entry.config(state="normal")
    entry.focus()  # Places cursor back in entry box


# ----------------------------------------
# Better than keyboard.add_hotkey()
#
# This only triggers when Enter is pressed
# while the entry widget is focused.
# ----------------------------------------
entry.bind("<Return>", lambda event: pressed())

# Give cursor focus to entry immediately
entry.focus()

root.mainloop()