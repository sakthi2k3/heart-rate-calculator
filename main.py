from tkinter import *
import time
from tkinter import filedialog as fd
from calculation import hearbeat

root = Tk()
root.resizable(width=False,height=False)
root.title('heartbeat calculator')
root.iconbitmap('heart.ico')

app_width=600
app_height=500
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
x=(screen_width/2)-(app_width/2)
y=(screen_height/2)-(app_height/2)
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
root.configure(bg='black')

frameCnt = 10
frames = [PhotoImage(file='1.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]
def a():
    filename = fd.askopenfilename()
    hr=hearbeat(filename)
    heartrate=Label(root,text="heartrate: "+str(hr)+"  BPM",bg='black',fg='red',font=("bold",12,"bold")).place(x = 218,y=400)



b1=Button(root,text="open",bg='white',fg='black',command=a)

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(100, update, ind)
label = Label(root,bg="black")

label.place(x=200,y=50)
b1.place(x=283,y=350)
procedure = Label(root, 
text = "Cover your phone's tourch and camera with your finger then trun your\n camera and tourch light on and take a shortvideo and save it in your device,\nthen click open and choose that file to find your heartrate."
,bg='black',fg='yellow',font=("bold",12,"bold")).place(x = 5,y = 280)  
root.after(0, update, 0)

root.mainloop()
