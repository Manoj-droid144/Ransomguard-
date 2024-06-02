import tkinter as tk
from tkinter import filedialog, messagebox
import time
from tkinter import ttk
import os.path
import os
import random

def scan_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        pb.start(10)  # Start the progress bar with a 10-second delay
        root.after(10000, lambda: scan_folder_complete(folder_path))

def scan_folder_complete(folder_path):
    total_files = sum([len(files) for _, _, files in os.walk(folder_path)])
    scanned_files = 0
    malware_detected = False
    for i, (root, _, files) in enumerate(os.walk(folder_path)):
        for file in files:
            file_path = os.path.join(root, file)
            if "malware test zip" in file_path:
                malware_detected = True
                ransomware_types = generate_ransomware_types()
            else:
                ransomware_types = "Safe"
            result = "Threats Found!" if malware_detected else "No Threats Found."
            scan_time = time.strftime("%Y-%m-%d %H:%M:%S")
            update_log_table(scan_time, result, ransomware_types, file_path)
            scanned_files += 1
            progress_var.set(int(scanned_files / total_files * 100))
    pb.stop()  # Stop the progress bar
    messagebox.showinfo("Scan Complete", "Folder scan completed!")
    # Write scan log for the folder
    with open("scan_log.txt", "a") as log_file:
        log_file.write(f"{scan_time},\t{result}, \t{ransomware_types}, \t{file_path}\n")

def scan_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        pb.start(5)  # Start the progress bar with a 5-second delay
        root.after(5000, lambda: scan_file_complete(file_path))

def scan_file_complete(file_path):
    if "malware test zip" in file_path:
        malware_detected = True
        ransomware_types = generate_ransomware_types()
    else:
        malware_detected = False
        ransomware_types = "Safe"
    result = "Threats Found!" if malware_detected else "No Threats found."
    scan_time = time.strftime("%Y-%m-%d %H:%M:%S")
    update_log_table(scan_time, result, ransomware_types, file_path)
    pb.stop()  # Stop the progress bar
    messagebox.showinfo("Scan Result", result)
    with open("scan_log.txt", "a") as log_file:
        log_file.write(f"{scan_time},\t{result}, \t{ransomware_types}, \t{file_path}\n")

def generate_ransomware_types():
    # Generate ransomware types
    ransomware_types = ["CryptoLocker","WannaCry","Ryuk","Sodinokibi","NetWalker",]
    return random.choice(ransomware_types)

def update_log_table(scan_time, result, ransomware_types, file_path):
    log_tree.insert("", "end", values=(scan_time, result, ransomware_types, file_path))

def open_scan_history():
    try:
        os.startfile("scan_log.txt")
    except OSError:
        messagebox.showerror("Error", "Could not open scan history file.")

if not os.path.exists("scan_log.txt"):
    with open("scan_log.txt", "w") as log_file:
        log_file.write("Scan Logs:\n")

# Create the main window
root = tk.Tk()
root.title("Scanner")
root.geometry("850x400")

# Styles
style = ttk.Style()
style.configure("TButton", padding=5, relief="flat", foreground="black", background="#4caf50")
style.map("TButton", foreground=[('active', 'black')], background=[('active', '#43a047')])

# Frames
frame = tk.Frame(root, bg="#eeeeee")
frame.pack(padx=20, pady=20)

# Buttons
scan_folder_button = ttk.Button(frame, text="Scan Folder", command=scan_folder, style="TButton")
scan_folder_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

scan_button = ttk.Button(frame, text="Scan", command=scan_file, style="TButton")
scan_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

scan_history_button = ttk.Button(frame, text="Scan History", command=open_scan_history, style="TButton")
scan_history_button.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

# Progress bar
pb = ttk.Progressbar(frame, orient="horizontal", mode="determinate", length=500)
pb.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="ew")

# Progress label
progress_label = ttk.Label(frame, text="Scan Progress:", background="#eeeeee")
progress_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

# Percentage label
progress_var = tk.DoubleVar()
percentage_label = ttk.Label(frame, textvariable=progress_var, background="#eeeeee")
percentage_label.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky="e")

# Scan log table
log_tree = ttk.Treeview(frame, columns=("Scan Time", "Result", "Ransomware Types", "File Path"), show="headings")
log_tree.heading("Scan Time", text="Scan Time")
log_tree.heading("Result", text="Result")
log_tree.heading("Ransomware Types", text="Ransomware Types")
log_tree.heading("File Path", text="File Path")
log_tree.grid(row=3, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

# Run the application
root.mainloop()
