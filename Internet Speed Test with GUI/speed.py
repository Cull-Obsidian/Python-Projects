from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3)) + "Mbps"
    up = str(round(sp.upload()/ (10**6) , 3)) + "Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)



sp = Tk()

sp.title(" Internet Speed  Test")
sp.geometry("500x700")
sp.config(bg="#0af")

lab = Label(sp, text="Internet Speed Test", font=("Poppins", 30), bg="#0af", fg="#fff")
lab.place(x=50, y=40, height=50, width=380)

lab = Label(sp, text="Downloading Speed", font=("Poppins", 27) )
lab.place(x=50, y=130, height=50, width=380)


lab_down = Label(sp, text="00", font=("Poppins", 30))
lab_down.place(x=50, y=200, height=50, width=380)


lab = Label(sp, text="Upload Speed", font=("Poppins", 30))
lab.place(x=50, y=290, height=50, width=380)

lab_up = Label(sp, text="00", font=("Poppins", 30))
lab_up .place(x=50, y=360, height=50, width=380)


button = Button(sp, text="CHECK SPEED", font=("Poppins", 15, "bold"), relief=RAISED, command=speedcheck)
button.place(x=160, y=460, height=50, width=200)

sp.mainloop()


#unistall speedtext module and then install speedtest-cli if the above code doesn't Works

#open cmd and write pip install speedtest-cli

# I Encountered this problem too above solution fixed it