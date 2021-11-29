from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("Youtube Video Downloader")

Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()
Label(root, text = '*NOTE* "Not Responding" is a normal occurence.', font = 'arial 10 bold').place(x = 90 , y = 200)

link = StringVar()
Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x = 160 , y = 60)
link_enter = Entry(root, width = 70, textvariable = link).place(x = 32, y = 100)



def Downloader():     
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download()
    Label(root, text = 'Your video has been downloaded!', font = 'arial 15').place(x = 90 , y = 250)

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' , bg = 'turquoise', padx = 2, command = Downloader).place(x = 180 , y = 150)

root.mainloop()