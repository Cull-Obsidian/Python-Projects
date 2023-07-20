import tkinter as tk
from tkinter import ttk
from gtts import gTTS
from tkinter import filedialog
import pygame
import os

# Custom color scheme hexadecimal codes
PRIMARY_COLOR = '#2E86C1'
DARK_COLOR = '#1B4F72'
LIGHT_COLOR = '#D6EAF8'
BLACK = '#000000'
WHITE = '#FFFFFF'

def text_to_speech():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        language = 'en'  # You can change the language code here if needed.
        tts = gTTS(text=text, lang=language)
        tts.save("output.mp3")

        # Play the audio using pygame
        pygame.mixer.init()
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()

def download_audio():
    file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
    if file_path:
        text_to_speech()
        os.rename("output.mp3", file_path)

# Create the main application window
root = tk.Tk()
root.title("Text-to-Speech Translator")
root.geometry("550x550")
root.configure(bg=PRIMARY_COLOR)

# Custom Fonts
header_font = ("Poppins", 24, "bold")
button_font = ("Poppins", 14)

# Create a custom style with rounded button appearance
style = ttk.Style()
style.configure('Rounded.TButton', font=button_font, background=DARK_COLOR, foreground=BLACK, padding=10)
style.map('Rounded.TButton', background=[('active', LIGHT_COLOR), ('pressed', PRIMARY_COLOR)])

# Create and style the widgets
header_label = tk.Label(root, text="Text-to-Speech Translator", font=header_font, bg=PRIMARY_COLOR, fg=WHITE)
header_label.pack(pady=20)

text_entry = tk.Text(root, wrap=tk.WORD, font=("Poppins", 14), height=6, width=40, bg=LIGHT_COLOR, fg=BLACK)
text_entry.pack(pady=20)

convert_button = ttk.Button(root, text="Convert to Speech", command=text_to_speech, style='Rounded.TButton')
convert_button.pack(pady=10)

download_button = ttk.Button(root, text="Download Audio", command=download_audio, style='Rounded.TButton')
download_button.pack(pady=10)

# Start the main loop
root.mainloop()
