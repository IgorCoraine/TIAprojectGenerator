import os
import tkinter as tk
from tkinter import filedialog
from openness import TIAProject
from xmlHandler import extract_info

class ProjectGeneratorUI:
    def __init__(self, master):
        self.master = master
        self.master.iconbitmap('.\\cora.ico')
        self.master.title("TIA Project Generator")

        self.tia_project = TIAProject()

        self.xml_path = ""
        self.project_path = ""
        self.project_name = ""
        self.devices = []

        self.file_label = tk.Label(master, text="1. Choose the HW file (TIA Selection Tool|*.tia):")
        self.file_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        self.file_entry = tk.Entry(master, width=50)
        self.file_entry.grid(row=0, column=1, padx=10, pady=5)

        self.browse_button = tk.Button(master, text="Search", command=self.browse_xml)
        self.browse_button.grid(row=0, column=2, padx=10, pady=5)

        self.project_label = tk.Label(master, text="2. Choose how to save the project:")
        self.project_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)

        self.project_entry = tk.Entry(master, width=50)
        self.project_entry.grid(row=1, column=1, padx=10, pady=5)

        self.browse_project_button = tk.Button(master, text="Search", command=self.browse_project)
        self.browse_project_button.grid(row=1, column=2, padx=10, pady=5)

        self.create_button = tk.Button(master, text="Create Project", command=self.create_project)
        self.create_button.grid(row=3, columnspan=3, padx=10, pady=10)

        self.output_label = tk.Label(master, text="Progress:")
        self.output_label.grid(row=4, column=0, sticky="w", padx=10, pady=5)

        self.output_text = tk.Text(master, width=50, height=10)
        self.output_text.grid(row=5, columnspan=3, padx=10, pady=5)

    def browse_xml(self):
        file_path = filedialog.askopenfilename(filetypes=[("TIA Selection Tools Files", "*.tia")])
        self.xml_path = file_path
        self.devices = extract_info(self.xml_path)
        self.file_entry.delete(0, tk.END)
        self.file_entry.insert(0, self.xml_path)

    def browse_project(self):
        project_path = filedialog.asksaveasfilename()
        self.project_path = os.path.dirname(project_path)
        self.project_name = os.path.basename(project_path)
        self.project_entry.delete(0, tk.END)
        self.project_entry.insert(0, project_path)

    def create_project(self):
        self.output_text.delete(1.0, tk.END)  # Clear previous output
        if not self.xml_path or not self.project_path or not self.project_name:
            self.output_text.insert(tk.END, "Please, fill in all fields.\n")
            return
        
        #start tia
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, "Inicializing TIA Portal without UI...\n")
        self.output_text.see(tk.END)
        self.master.update()
        try:
            self.tia_project.startTIA(False)
        except Exception as e:
            self.output_text.insert(tk.END, f"❌ Error to open TIA: {e}\n")
            self.output_text.see(tk.END)
            return
        else:
            self.output_text.insert(tk.END, f"✔ TIA started successfully\n")
            self.output_text.see(tk.END)
            self.master.update()

        #create project
        self.output_text.insert(tk.END, f"Creating the project {self.project_name}...\n")
        self.output_text.see(tk.END)
        self.master.update()
        try:
            self.tia_project.create_project(self.project_path, self.project_name)
        except Exception as e:
            self.output_text.insert(tk.END, f"❌ Error to create the project: {e}\n")
            self.output_text.see(tk.END)
            return
        else:
            self.output_text.insert(tk.END, f"✔ Project created successfully\n")
            self.output_text.see(tk.END)
            self.master.update()
        
        #create devices
        self.output_text.insert(tk.END, f"Creating devices...\n")
        self.master.update()
        for idx, device in enumerate(self.devices, start=1):
            self.output_text.insert(tk.END, f"Creating Device {idx}: {device.name}\n")
            self.output_text.see(tk.END)
            self.master.update()
            try:
                self.tia_project.create_device(device.name, device.modules[0], 10.0)
            except Exception as e:
                self.output_text.insert(tk.END, f"❌ Error to create the device: {e}\n")
                self.output_text.see(tk.END)
                return
            else:
                self.output_text.insert(tk.END, f"✔ Device created successfully\n")
                self.output_text.see(tk.END)
                self.master.update()
    # def output_animated_text(self, text):
    #     self.output_text.delete(1.0, tk.END) 
    #     if count <= 3:
    #         dots = "." * count
    #         self.output_text.insert(tk.END, f"{text}{dots}")
    #         count += 1
    #     elif self.animateText:
    #         count = 0
    #         self.output_text.insert(tk.END, text)
    #     else:
    #         return
    #     self.master.after(500, lambda: self.output_animated_text(text))

def main():
    root = tk.Tk()
    app = ProjectGeneratorUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
