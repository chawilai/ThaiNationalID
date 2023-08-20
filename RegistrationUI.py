import tkinter as tk
from tkinter import messagebox

class RegistrationUI(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("สุ่มเลขบัตรประชาชน - ลงทะเบียนเข้าสู่ระบบ")
        self.parent.geometry('600x700+200+100')

        # Define religion_list as an instance variable
        self.religion_list = ["Christianity", "Buddhism", "Islam", "Sikh", "Hindu"]

        # Create a BooleanVar to track the check state
        self.religion_status_var = tk.BooleanVar()

        self.init_ui()

    def init_ui(self):
        self.pack(fill=tk.BOTH, expand=1)

        # New contact grid
        tk.Label(self, text="Generated Citizen ID: ").grid(row=0, column=2, columnspan=2, sticky=tk.W)
        tk.Label(self, text="First Name:").grid(row=1, column=1, sticky=tk.E)
        tk.Label(self, text="Last Name:").grid(row=2, column=1, sticky=tk.E)
        tk.Label(self, text="Address").grid(row=3, column=1, sticky=tk.E)

        self.entry1 = tk.Entry(self)
        self.entry2 = tk.Entry(self)
        self.entry3 = tk.Entry(self)
        self.entry1.grid(row=1, column=2)
        self.entry2.grid(row=2, column=2)
        self.entry3.grid(row=3, column=2)

        religion_status_check = tk.IntVar()
        religion_status_check = tk.Checkbutton(self, variable=self.religion_status_var,
                                        command=self.require_religion,
                                        text="Specify Religion?")
        religion_status_check.grid(row=4, column=2, columnspan=2)

        tk.Label(self, text="Birthday:").grid(row=5, column=1, sticky=tk.E)
        tk.Label(self, text="Religion:").grid(row=6, column=1, sticky=tk.E)

        self.entry4 = tk.Entry(self)
        self.entry5 = tk.Entry(self)

        self.entry4.grid(row=5, column=2)
        self.entry5.grid(row=6, column=2)

        religion_list = tk.Listbox(self, width=20, height=len(self.religion_list))
        religion_list.grid(row=0, column=1)
        for religion in self.religion_list:
            religion_list.insert(tk.END, religion)

        religion_list.bind("<<ListboxSelect>>", self.on_select)
        religion_list.place(x=20, y=210)

    def on_select(self, event):
        sender = event.widget
        selected_index = sender.curselection()
        if selected_index:
            selected_value = sender.get(selected_index[0])
            self.entry5.delete(0, tk.END)
            self.entry5.insert(0, selected_value)

    def require_religion(self):
        if self.religion_status_var.get():  # Check the state using get()
            self.entry5.config(state='disabled')
        else:
            self.entry5.config(state='normal')

def main():
    root = tk.Tk()
    ex = RegistrationUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()