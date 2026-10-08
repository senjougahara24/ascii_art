import tkinter as tk

root = tk.Tk()
text_widget = tk.Text(root, font=("Consolas", 8), bg = "black", fg = "white")
text_widget.pack(expand=True, fill="both")
text_widget.insert("1.0", "hello")
text_widget.pack(expand=True, fill="both")

print("가로픽셀: ", text_widget.winfo_width())
print("세로픽셀: ", text_widget.winfo_height())

root.mainloop()