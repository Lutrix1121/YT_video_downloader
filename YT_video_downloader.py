# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 20:16:42 2024

@author: Lutrix
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from pytubefix import YouTube
from pytubefix.cli import on_progress
import glob
import os


class YouTubeDownloader:
    def __init__(self):
        self.save_location = ""
        self.ui()

    def select_location(self):
        self.save_location = filedialog.askdirectory()
        return self.save_location

    def download_video(self):
        link = self.link_entry.get()
        if not link.strip():
            messagebox.showwarning("No Link", "Please provide a YouTube video link!")
            return

        try:
            yt = YouTube(link, on_progress_callback=on_progress)
            ys = yt.streams.get_highest_resolution()
            ys.download(self.select_location())
            messagebox.showinfo("Success", f"Downloaded: {yt.title}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to download video: {e}")

    def latest_downloaded_file(self):
        try:
            file_list = glob.glob(f'{self.save_location}/*.mp4')
            if not file_list:
                messagebox.showinfo("No Files", "No video files found.")
                return
            latest_file = max(file_list, key=os.path.getctime)
            file_name = os.path.basename(latest_file)
            messagebox.showinfo("Latest File", f"Latest file: {file_name}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to find file: {e}")

    def ui(self):
        self.root = tk.Tk()
        self.root.title("YouTube Video Downloader")
        self.root.geometry("400x200")

        # Label and input field for link
        self.link_label = tk.Label(self.root, text="Enter YouTube video link:")
        self.link_label.pack(pady=5)
        self.link_entry = tk.Entry(self.root, width=50)
        self.link_entry.pack(pady=5)

        # Buttons
        self.download_button = tk.Button(self.root, text="Download Video", command=self.download_video)
        self.download_button.pack(pady=10)

        self.latest_file_button = tk.Button(self.root, text="Show Latest File", command=self.latest_downloaded_file)
        self.latest_file_button.pack(pady=10)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = YouTubeDownloader()
    app.run()