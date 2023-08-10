import tkinter as tk

def on_button_click(event):
    current_text = result_label["text"]
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(current_text)
            result_label.config(text=str(result))
        except Exception as e:
            result_label.config(text="Error")
    elif button_text == "C":
        result_label.config(text="")
    else:
        result_label.config(text=current_text + button_text)

root = tk.Tk()
root.title("Calculator")

result_label = tk.Label(root, text="", anchor="e", bg="white", font=("Arial", 24))
result_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

for button_text, row, col in buttons:
    button = tk.Button(root, text=button_text, font=("Arial", 18), padx=20, pady=20)
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", on_button_click)

root.mainloop()
