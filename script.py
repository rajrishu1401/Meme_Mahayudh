import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import random

class GameModeSelector:
    def __init__(self, root):
        self.root = root
        self.root.title("maro par hass hasske")

        # Set the window to full screen
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))

        # Load the background image
        self.bg_image = Image.open("assets/images/background/str1.png")  # Replace with the path to your background image
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(root, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # Create a button to start the game
        self.start_button = tk.Button(root, text="Start Game", command=self.open_mode_selection, font=("Helvetica", 20), height=2, width=15, bg="#3498db", fg="white")
        self.start_button.place(relx=0.5, rely=0.5, anchor="center")  # Center the button

    def open_mode_selection(self):
        # Destroy the current window
        self.root.destroy()

        # Open a new window for mode selection
        mode_selector = ModeSelectorWindow()
        mode_selector.run()

class ModeSelectorWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Select Game Mode")

        # Set the window to full screen
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))

        # Load the background image
        self.bg_image = Image.open("assets/images/background/1.jpg")  # Replace with the path to your background image
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # Create a label to prompt the user
        self.label = tk.Label(self.root, text="Select a game mode:", font=("Helvetica", 16), bg="lightgray")
        self.label.pack(pady=10)

        # Create buttons for each mode with updated names
        mode_names = ["lappu v/s Rajpal", "Puneet v/s Systumm", "Rajpal v/s Puneet", "Puneet v/s Lappu", "Rajpal v/s Systumm", "Lappu v/s Systumm"]
        for mode, mode_name in enumerate(mode_names, start=1):
            button = tk.Button(self.root, text=mode_name, command=lambda m=mode: self.mode_button_clicked(m),
                               font=("Helvetica", 16), height=2, width=15, bg=random_color(), fg="white")
            button.pack(pady=5)

    def mode_button_clicked(self, mode):
        # Destroy the current window
        # self.root.destroy()

        # Start the selected game mode
        start_game(mode)

    def run(self):
        # Run the main loop for this window
        self.root.mainloop()

def start_game(mode):
    # Replace the following with the actual file names for each mode
    file_names = {
        1: "mode1.py",
        2: "mode2.py",
        3: "mode3.py",
        4: "mode4.py",
        5: "mode5.py",
        6: "mode6.py",
    }

    file_name = file_names.get(mode, None)

    if file_name:
        subprocess.run(["python", file_name])
    else:
        messagebox.showerror("Error", "Invalid mode selected.")

def random_color():
    # Generate a random RGB color
    return "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

if __name__ == "__main__":
    # Create the main window for game mode selection
    main_window = tk.Tk()
    game_mode_selector = GameModeSelector(main_window)

    # Run the main loop
    main_window.mainloop()