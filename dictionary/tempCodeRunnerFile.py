            # 1. Change state to normal so Python is allowed to edit it
        text_box.config(state="normal")

        # 2. Clear all the text from the start to the end
        text_box.delete("1.0", tk.END)

        # 3. Change state back to disabled so the user can't type in it
        text_box.config(state="disabled")   # Clear previous search results