from tkinter import *
from pytube import YouTube

# Function to download YouTube video
def downloadYT():
    link = enterurl.get()
    try:
        youtube_object = YouTube(link)
        
        # Example: Get the first progressive stream available
        youtube_stream = youtube_object.streams.filter(progressive=True).first()
        
        if youtube_stream:
            lblfeedback.config(text="Downloading...", fg='blue')
            youtube_stream.download()
            lblfeedback.config(text="Video downloaded successfully", fg='green')
        else:
            lblfeedback.config(text="No suitable stream found", fg='red')
    except Exception as e:
        lblfeedback.config(text=f"Error: {str(e)}", fg='red')


# Create the window
root = Tk()
root.title("YouTube Video Downloader")
root.geometry("700x400")

# Mainframe
mainframe = Frame(root, bd=10, relief=RIDGE)
mainframe.pack(pady=20)

# Topframe1
topframe1 = Frame(mainframe, bd=10, relief=RIDGE)
topframe1.grid(row=0, column=0, pady=20)

# Topframe2
topframe2 = Frame(mainframe, bd=0, relief=RIDGE)
topframe2.grid(row=1, column=0, padx=20, pady=20)

# Labels, Entry, Button initialization
ibltitle = Label(topframe1, font=("arial", 30, 'bold', 'underline'), text="YouTube Video Downloader")
ibltitle.grid(row=0, column=0)

lblurl = Label(topframe2, font=("arial", 24, 'bold'), text="Enter the URL of the video:", pady=20)
lblurl.grid(row=0, column=0)

enterurl = Entry(topframe2, font=("arial", 18), width=50, bd=5)
enterurl.grid(row=1, column=0, padx=20, pady=10)

downloadbutton = Button(topframe2, font=("arial", 18, 'bold'), text="Download Video", command=downloadYT)
downloadbutton.grid(row=2, column=0, pady=20)

lblfeedback = Label(topframe2, font=("arial", 18, 'bold'), text="", fg='black')
lblfeedback.grid(row=3, column=0)

root.mainloop()
