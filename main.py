# Youtube Video Downloader: This application helps users to download youtube video with its link
# Note : This is for educational purposes only
# Author: Manu S Rao
# Date: 25-06-2021

# Colors used in the application
BACKGROUND_COLOR = "#ffde59"
BUTTON_COLOR = "#FB9300"
HEADING_COLOR = "#000000"
HEADING_FONT = "Helvetica"
LINK_FONT = "calibre"

# Importing Pytube and Tkinter Module
from pytube import YouTube
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

# Window code
window = Tk()
window.title("Youtube Video Download")
window.config(bg=BACKGROUND_COLOR)
window.geometry("400x300")
window.columnconfigure(0, weight=1) # To Center all the elements

# Folder Name
FOLDER_NAME = ""

# 1. Heading Label
heading = Label(text="Youtube Video Downloader", font=(HEADING_FONT, 20, "bold"))
heading.config(fg=HEADING_COLOR, bg=BACKGROUND_COLOR)
heading.grid()

# 2. Link entry
link_label = Label(text="Please Enter the Link here", font=(LINK_FONT, 10, "bold"))
link_label.config(fg=HEADING_COLOR, bg=BACKGROUND_COLOR)
link_label.grid()
video_link = StringVar()
link = Entry(window, width=50, textvariable=video_link)
link.grid()
link_error = Label(text="", font=(LINK_FONT, 10, "bold"))
link_error.config(fg=HEADING_COLOR, bg=BACKGROUND_COLOR)
link_error.grid()


# 4. Location Selection
# Function for selecting folder location
def select_location():
    global FOLDER_NAME
    FOLDER_NAME = filedialog.askdirectory()
    if len(FOLDER_NAME) > 0:
        location_error.config(text=f"Chosen folder:{FOLDER_NAME}", fg="green")
    else:
        location_error.config(text="Please Choose a Folder To download", fg="red")


location_label = Label(text="Please choose the download folder", font=(LINK_FONT, 10, "bold"))
location_label.config(fg=HEADING_COLOR, bg=BACKGROUND_COLOR, padx=20)
location_label.grid()
location = Button(text="Location", command=select_location)
location.config(bg=BUTTON_COLOR, fg=HEADING_COLOR, padx=10, pady=10)
location.grid()
location_error = Label(text="", font=(LINK_FONT, 10, "bold"))
location_error.config(fg=HEADING_COLOR, bg=BACKGROUND_COLOR)
location_error.grid()


# 5. Quality Selection
choices_list = ["1080p", "720p", "480p", "360p", "240p", "144p", "Audio Only"]
choices = ttk.Combobox(window, values=choices_list)
choices.grid()


# Using Pytube to download video
def download_video():
    choice = choices.get()
    url = link.get()
    if len(url) > 0:
        yt = YouTube(url)
        if choice == choices_list[-1]:
            stream = yt.streams.get_audio_only()
        else:
            stream = yt.streams.get_by_resolution(choice)
        stream.download(FOLDER_NAME)
    else:
        link_error.config(text="Please Enter the URL", fg='red')
        download_error.config(text="Please Enter the URL once again", fg='red')


# 5. Download Button
a = Label(text="", font=(LINK_FONT, 20, "bold"))
a.config(fg=HEADING_COLOR, bg=BACKGROUND_COLOR)
a.grid()
download = Button(text="Download", width=20, command=download_video)
download.config(bg="#32cd32", fg=HEADING_COLOR, pady=10)
download.grid()
download_error = Label(text="", font=(LINK_FONT, 10, "bold"))
download_error.config(fg=HEADING_COLOR, bg=BACKGROUND_COLOR)
download_error.grid()

# Code to keep the window running
window.mainloop()
