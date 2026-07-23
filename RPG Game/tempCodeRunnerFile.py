
    def clear_screen(self):
        for widget in root.winfo_children():
            widget.destroy()