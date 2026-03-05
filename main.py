import os
import threading
import customtkinter as ctk
from tkinter import filedialog, messagebox
from splitter import split_file

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("TEXT FILE SPLITTER v1.0")
        self.geometry("650x520")
        self.resizable(False, False)
        
        # Set icon
        if os.path.exists("app_icon.ico"):
            self.iconbitmap("app_icon.ico")
        
        # Retro color scheme (Classic Windows style)
        # Background: #c0c0c0 (Grey)
        # Accents: #000080 (Navy Blue)
        
        ctk.set_appearance_mode("Light")
        
        # Customizing the retro look
        self.configure(fg_color="#d4d0c8")
        
        # Font settings
        self.retro_font_bold = ctk.CTkFont(family="Courier New", size=18, weight="bold")
        self.retro_font = ctk.CTkFont(family="Courier New", size=14)
        self.retro_font_small = ctk.CTkFont(family="Courier New", size=12)

        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(5, weight=1)

        # Main Border Frame
        self.main_frame = ctk.CTkFrame(self, fg_color="#d4d0c8", border_width=2, border_color="#808080", corner_radius=0)
        self.main_frame.grid(row=0, column=0, rowspan=7, sticky="nsew", padx=4, pady=4)
        self.main_frame.grid_columnconfigure(0, weight=1)

        # Title Label with classic blue background effect
        self.title_bg = ctk.CTkFrame(self.main_frame, fg_color="#000080", height=32, corner_radius=0)
        self.title_bg.grid(row=0, column=0, sticky="ew", padx=2, pady=2)
        
        self.title_label = ctk.CTkLabel(self.title_bg, text="[ TEXT_FILE_SPLITTER.EXE ]", font=self.retro_font_bold, text_color="white")
        self.title_label.pack(pady=4)

        # Input File Section
        self.input_frame = ctk.CTkFrame(self.main_frame, fg_color="#d4d0c8", border_width=1, border_color="#808080", corner_radius=0)
        self.input_frame.grid(row=1, column=0, padx=20, pady=15, sticky="ew")
        self.input_frame.grid_columnconfigure(1, weight=1)

        self.input_label = ctk.CTkLabel(self.input_frame, text="SOURCE PATH:", font=self.retro_font)
        self.input_label.grid(row=0, column=0, padx=10, pady=15)
        
        self.input_entry = ctk.CTkEntry(self.input_frame, placeholder_text="C:\\PATH\\TO\\FILE.TXT", 
                                       fg_color="white", text_color="black", border_color="#808080", 
                                       corner_radius=0, font=self.retro_font)
        self.input_entry.grid(row=0, column=1, padx=5, pady=15, sticky="ew")
        
        self.input_button = ctk.CTkButton(self.input_frame, text="BROWSE", width=90, 
                                         fg_color="#d4d0c8", text_color="black", border_width=2, 
                                         border_color="#ffffff", hover_color="#c0c0c0",
                                         corner_radius=0, font=self.retro_font, command=self.browse_input)
        self.input_button.grid(row=0, column=2, padx=10, pady=15)

        # Chunk Size Section
        self.size_frame = ctk.CTkFrame(self.main_frame, fg_color="#d4d0c8", border_width=1, border_color="#808080", corner_radius=0)
        self.size_frame.grid(row=2, column=0, padx=20, pady=5, sticky="ew")
        
        self.size_label = ctk.CTkLabel(self.size_frame, text="LINES_PER_CHUNK:", font=self.retro_font)
        self.size_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.size_entry = ctk.CTkEntry(self.size_frame, width=120, fg_color="white", text_color="black", 
                                      border_color="#808080", corner_radius=0, font=self.retro_font)
        self.size_entry.insert(0, "4900")
        self.size_entry.grid(row=0, column=1, padx=10, pady=10)

        # Output Dir Section
        self.output_frame = ctk.CTkFrame(self.main_frame, fg_color="#d4d0c8", border_width=1, border_color="#808080", corner_radius=0)
        self.output_frame.grid(row=3, column=0, padx=20, pady=15, sticky="ew")
        self.output_frame.grid_columnconfigure(1, weight=1)

        self.output_label = ctk.CTkLabel(self.output_frame, text="TARGET DIR:", font=self.retro_font)
        self.output_label.grid(row=0, column=0, padx=10, pady=15)
        
        self.output_entry = ctk.CTkEntry(self.output_frame, placeholder_text="C:\\OUTPUT\\DIRECTORY", 
                                        fg_color="white", text_color="black", border_color="#808080", 
                                        corner_radius=0, font=self.retro_font)
        self.output_entry.grid(row=0, column=1, padx=5, pady=15, sticky="ew")
        
        self.output_button = ctk.CTkButton(self.output_frame, text="BROWSE", width=90, 
                                          fg_color="#d4d0c8", text_color="black", border_width=2, 
                                          border_color="#ffffff", hover_color="#c0c0c0",
                                          corner_radius=0, font=self.retro_font, command=self.browse_output)
        self.output_button.grid(row=0, column=2, padx=10, pady=15)

        # Split Button
        self.split_button = ctk.CTkButton(self.main_frame, text="[ EXECUTE SPLIT ]", height=45, 
                                         fg_color="#d4d0c8", text_color="black", border_width=3, 
                                         border_color="#ffffff", hover_color="#c0c0c0",
                                         corner_radius=0, font=self.retro_font_bold, command=self.start_split)
        self.split_button.grid(row=4, column=0, padx=20, pady=20, sticky="ew")

        # Status and Progress
        self.status_label = ctk.CTkLabel(self.main_frame, text="SYSTEM READY", font=self.retro_font_small, text_color="black")
        self.status_label.grid(row=5, column=0, padx=20, pady=(5, 0), sticky="s")
        
        self.progress_bar = ctk.CTkProgressBar(self.main_frame, fg_color="#808080", progress_color="#000080", 
                                             border_width=1, border_color="black", corner_radius=0)
        self.progress_bar.grid(row=6, column=0, padx=40, pady=(5, 25), sticky="ew")
        self.progress_bar.set(0)

    def browse_input(self):
        filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if filename:
            self.input_entry.delete(0, "end")
            self.input_entry.insert(0, filename)

    def browse_output(self):
        directory = filedialog.askdirectory()
        if directory:
            self.output_entry.delete(0, "end")
            self.output_entry.insert(0, directory)

    def start_split(self):
        input_file = self.input_entry.get()
        chunk_size_str = self.size_entry.get()
        output_dir = self.output_entry.get()

        if not input_file:
            messagebox.showerror("IO_ERROR", "NO SOURCE FILE SELECTED.")
            return

        try:
            chunk_size = int(chunk_size_str)
            if chunk_size <= 0:
                raise ValueError()
        except ValueError:
            messagebox.showerror("VAL_ERROR", "INVALID CHUNK SIZE DETECTED.")
            return

        if not output_dir:
            output_dir = os.path.dirname(input_file)

        # Disable UI
        self.split_button.configure(state="disabled")
        self.input_button.configure(state="disabled")
        self.output_button.configure(state="disabled")
        self.input_entry.configure(state="disabled")
        self.output_entry.configure(state="disabled")
        self.size_entry.configure(state="disabled")

        # Run in thread
        threading.Thread(target=self.run_split, args=(input_file, output_dir, chunk_size), daemon=True).start()

    def run_split(self, input_file, output_dir, chunk_size):
        try:
            split_file(input_file, output_dir, chunk_size, self.update_progress)
            self.after(0, lambda: self.finish_split(True, "OPERATION SUCCESSFUL."))
        except Exception as e:
            self.after(0, lambda: self.finish_split(False, f"FATAL ERROR: {str(e).upper()}"))

    def update_progress(self, message, progress):
        self.after(0, lambda: self.status_label.configure(text=message.upper()))
        self.after(0, lambda: self.progress_bar.set(progress))

    def finish_split(self, success, message):
        # Re-enable UI
        self.split_button.configure(state="normal")
        self.input_button.configure(state="normal")
        self.output_button.configure(state="normal")
        self.input_entry.configure(state="normal")
        self.output_entry.configure(state="normal")
        self.size_entry.configure(state="normal")
        
        self.status_label.configure(text=message)
        if success:
            self.progress_bar.set(1)
            messagebox.showinfo("SUCCESS", message)
        else:
            self.progress_bar.set(0)
            messagebox.showerror("FAILURE", message)

if __name__ == "__main__":
    app = App()
    app.mainloop()
