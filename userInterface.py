import tkinter as tk
from tkinter import filedialog

class FileParameterUI:
    def __init__(self, master):
        self.master = master
        self.master.iconbitmap('.\\cora.ico')
        self.master.title("TIA Project Generator")

        self.xml_path = ""
        self.project_path = ""
        self.project_name = ""

        self.file_label = tk.Label(master, text="Tia Selection Tool:")
        self.file_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        self.file_label = tk.Label(master, text="Select File (.tia):")
        self.file_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)

        self.file_entry = tk.Entry(master, width=50)
        self.file_entry.grid(row=1, column=1, padx=10, pady=5)

        self.browse_button = tk.Button(master, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=1, column=2, padx=10, pady=5)

        self.parameter_label = tk.Label(master, text="Enter Parameter:")
        self.parameter_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)

        self.parameter_entry = tk.Entry(master, width=50)
        self.parameter_entry.grid(row=2, column=1, padx=10, pady=5)

        self.submit_button = tk.Button(master, text="Submit", command=self.submit)
        self.submit_button.grid(row=3, columnspan=3, padx=10, pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        self.file_entry.delete(0, tk.END)
        self.file_entry.insert(0, file_path)

    def submit(self):
        file_path = self.file_entry.get()
        parameter = self.parameter_entry.get()
        # Do something with the file and parameter, e.g., process the file using the parameter
        print("File:", file_path)
        print("Parameter:", parameter)

def main():
    root = tk.Tk()
    app = FileParameterUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
