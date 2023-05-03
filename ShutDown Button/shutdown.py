from tkinter import  *   #for Gui
import os   #for Accessing the os programs

def restart ():
    os.system("shutdown /r /t 1")  #for restart instantly

def restart_time():
   os.system("shutdown /r /t 20")   #20 means it will restart after 20 Seconds

def logout():
   os.system("shutdown -l")  #-l for logout

def shutdown():
    os.system("shutdown /s /t 1")



st = Tk()                   #to show Gui


st.title("Shutdown App")  #to Change the title bar name of gui
st.geometry("500x500")  #Dimension of the Window
st.config(bg="#0af")     #background Color

r_button = Button(st, text = "Restart", font = ("Poppins",16), relief= RAISED, cursor="plus", command=restart)  #button and it's customization  #restart Button
r_button.place(x=150 , y = 60,height=50, width=200)   #Size and postion of the button


rt_button = Button(st, text = "Restart In 20s", font = ("Poppins",16), relief= RAISED, cursor="plus", command = restart_time)  #button and it's customization  #restart with time button   
rt_button.place(x=150 , y = 170,height=50, width=200)   #Size and postion of the button


lg_button = Button(st, text = "Log-Out", font = ("Poppins",16), relief= RAISED, cursor="plus" ,command=logout)  #button and it's customization  #logout button
lg_button.place(x=150 , y = 270,height=50, width=200)   #Size and postion of the button



st_button = Button(st, text = "Shut-Down", font = ("Poppins",16), relief= RAISED, cursor="plus", command=shutdown)  #button and it's customization  #shutdown Button
st_button.place(x=150 , y = 370,height=50, width=200)   #Size and postion of the button


st.mainloop()        #to Show Gui



