import yt_dlp
import tkinter as tk
from tkinter import filedialog, messagebox
import os

def download_video(video_url, output_path, filename):
    ydl_opts = {
        'format': 'bestvideo[height<=360]+bestaudio/best[height<=360]',
        'outtmpl': f'{output_path}/{filename}'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    print(f'Downloaded: {video_url}')

def on_submit():
    video_url = url_entry.get()
    filename = filename_entry.get()
    
    if not video_url or not filename:
        messagebox.showerror("Error", "Please enter both URL and filename")
        return
    # Ensure filename has an extension
    if not os.path.splitext(filename)[1]:
        filename += '.webm' #faster than mp4
    
    output_path = os.path.join('./videos', filename)
    
    try:
        print(f"Downloading video from {video_url} to {output_path}")
        download_video(video_url, './videos', filename)
        messagebox.showinfo("Success", f"Video downloaded successfully to {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# Create and pack the URL input
url_label = tk.Label(root, text="YouTube URL:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# Create and pack the filename input
filename_label = tk.Label(root, text="Filename:")
filename_label.pack()
filename_entry = tk.Entry(root, width=50)
filename_entry.pack()

# Create and pack the submit button
submit_button = tk.Button(root, text="Download", command=on_submit)
submit_button.pack()

# Start the GUI event loop
root.mainloop()
