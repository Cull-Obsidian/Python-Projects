from plyer import notification
import time

if __name__ == '__main__':
   while True:
     notification.notify(
        title="*** Take Rest ***",
        message="Rest is vital for better mental health, It increases concentration and memory, a healthier immune system, reduces stress, improve mood and even a better metabolism",
        app_icon="letter-c.ico",
        timeout=5)
     time.sleep(10)


#Run python in the background using pythonw main.py
#open task manager and close the python process in the processes to close the annoying notifications