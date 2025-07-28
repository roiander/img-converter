import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image
import patoolib
import tempfile
import shutil
import zipfile

class ImageConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Free Image Converter")
        self.root.geometry("600x400")

        self.files = []
        self.output_format = tk.StringVar(value="webp")
        self.archive_type = tk.StringVar(value="zip")

        self.create_widgets()

    def create_widgets(self):
        # Label for dragging files
        label = tk.Label(self.root, text="Drag and drop images here", bg="lightgray", height=10)
        label.pack(fill="both", expand=True, padx=20, pady=20)
        label.drop_target_register(DND_FILES)
        label.dnd_bind("<<Drop>>", self.on_drop)

        # Output format selection
        format_label = tk.Label(self.root, text="Output format:")
        format_label.pack()
        formats = ["webp", "png", "jpeg", "jpg", "bmp", "gif"]
        format_combo = ttk.Combobox(self.root, textvariable=self.output_format, values=formats)
        format_combo.pack()

        # Output archive type selection
        archive_label = tk.Label(self.root, text="Output archive type:")
        archive_label.pack()
        archive_types = ["zip", "rar"]
        archive_combo = ttk.Combobox(self.root, textvariable=self.archive_type, values=archive_types)
        archive_combo.pack()

        # Convert button
        convert_button = tk.Button(self.root, text="Convert and Package", command=self.convert_and_package)
        convert_button.pack(pady=20)

    def on_drop(self, event):
        # Handle multiple dropped files
        files = self.root.tk.splitlist(event.data)
        for file in files:
            if file.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif", ".webp")):
                self.files.append(file)
        messagebox.showinfo("Files Added", f"{len(self.files)} images ready to convert.")

    def convert_and_package(self):
        if not self.files:
            messagebox.showerror("Error", "No images to convert.")
            return

        output_dir = tempfile.mkdtemp()
        converted_files = []

        try:
            for file in self.files:
                img = Image.open(file)
                base_name = os.path.splitext(os.path.basename(file))[0]
                output_path = os.path.join(output_dir, f"{base_name}.{self.output_format.get()}")
                img.save(output_path)
                converted_files.append(output_path)

            # Package
            output_file = filedialog.asksaveasfilename(defaultextension=f".{self.archive_type.get()}", filetypes=[(self.archive_type.get().upper(), f".{self.archive_type.get()}")])
            if not output_file:
                return

            if self.archive_type.get() == "zip":
                with zipfile.ZipFile(output_file, 'w') as zipf:
                    for file in converted_files:
                        zipf.write(file, os.path.basename(file))
            else:  # rar
                current_dir = os.getcwd()
                os.chdir(output_dir)
                temp_archive = 'temp.rar'
                relative_names = [os.path.basename(file) for file in converted_files]
                patoolib.create_archive(temp_archive, relative_names, program="rar")
                os.chdir(current_dir)
                shutil.move(os.path.join(output_dir, temp_archive), output_file)

            messagebox.showinfo("Success", f"Files converted and packaged in {output_file}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            shutil.rmtree(output_dir)
            self.files = []

if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app = ImageConverterApp(root)
    root.mainloop()