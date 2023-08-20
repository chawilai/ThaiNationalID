import tkinter as tk
import tkinter.messagebox
import webbrowser
import random

class ThaiNationalIDGenerator:
    def generate_number(self):
        random_num = random.randint(100000000000, 199999999999)
        temp = random_num
        sumall = 0

        for i in range(1, 13):
            sumall += (i + 1) * (random_num % 10)
            random_num = random_num // 10

        sumall = sumall % 11
        checksum = 11 - sumall
        result = (temp * 10) + checksum
        self.thai_id.set(result)

    def copy_button(self):
        clip = tk.Tk()
        clip.withdraw()
        clip.clipboard_clear()
        clip.clipboard_append(self.thai_id.get())
        clip.destroy()

    def open_github(self):
        webbrowser.open_new("https://github.com/coregameHD/ThaiNationalID")

    def about_box(self):
        tkinter.messagebox.showinfo("About", "Thai National ID Generator\
        \nโปรแกรมสุ่มเลขบัตรประชาชน\n\nBuilt with love by Coregame\nhttps://coregame-th.com")

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("สุ่มเลขบัตรประชาชน")

        menubar = tk.Menu(self.window)
        self.window.config(menu=menubar)

        commandmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Command", menu=commandmenu)
        commandmenu.add_command(label="Generate", command=self.generate_number)
        commandmenu.add_command(label="Copy to Clipboard", command=self.copy_button)
        commandmenu.add_separator()
        commandmenu.add_command(label="Exit", command=self.window.destroy)

        aboutmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="About", menu=aboutmenu)
        aboutmenu.add_command(label="Github", command=self.open_github)
        aboutmenu.add_separator()
        aboutmenu.add_command(label="About", command=self.about_box)

        tk.Label(self.window, text="Thai National ID Generator").grid(row=1, column=1, sticky=tk.W)
        tk.Label(self.window, text="Your number is ").grid(row=2, column=1, sticky=tk.W)

        self.thai_id = tk.StringVar()
        tk.Entry(self.window, textvariable=self.thai_id, justify=tk.RIGHT, state='readonly').grid(row=2, column=2, sticky=tk.E)

        tk.Button(self.window, text="Generate", command=self.generate_number).grid(row=4, column=2, sticky=tk.E)
        tk.Button(self.window, text="Copy to Clipboard", command=self.copy_button).grid(row=4, column=1, sticky=tk.W)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = ThaiNationalIDGenerator()
    app.run()
