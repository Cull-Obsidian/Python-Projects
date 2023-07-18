from tkinter import *
import qrcode

root = Tk()
root.title("Qr generator")
root.geometry("1000x550")
root.config(bg="#0af")
root.resizable(False, False)

#icon image
image_icon=PhotoImage(file="icon.png")
root.iconphoto(False,image_icon)

def generate():
    name=title.get()
    text=entry.get()
    qr=qrcode.make(text)
    qr.save("Qrcode/"+ str(name)+".png")
    
    global Image
    Image=PhotoImage(file="Qrcode/"+ str(name)+".png")
    Image_view.config(image=Image)


Image_view = Label(root,bg="#0af")
Image_view.pack(padx=50,pady=10,side=RIGHT)


Label(root, text="Title", fg="white",bg="#0af",font=15).place(x=50,y=170)

title=Entry(root,width=13,font='Poppins 15')
title.place(x=50,y=200)

entry=Entry(root,width=28,font="Poppins 15")
entry.place(x=50,y=250)

Button(root,text="Generate",width=10,height=1,bg="black",fg="white",command=generate,font='Poppins').place(x=50,y=300)



root.mainloop()


#https://youtu.be/sV52RXpR2P8
#https://www.youtube.com/@l_graphics/featured


#to convert py to exe first - pip install pyinstaller
#second - pip install auto-py-to-exe
#third - auto-py-to-exe