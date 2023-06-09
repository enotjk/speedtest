from tkinter import *
from speedtest import Speedtest

def runButt():
    download = Speedtest().download()
    upload = Speedtest().upload()
    download_speed = round(download / (10**6), 2)
    upload_speed = round(upload / (10**6), 2)
    ping = Speedtest()
    ping.get_best_server()
    ping_test = round(ping.results.ping, 2)

    download_label.config(text="Download speed: \n" + str(download_speed) + "MbPs")
    upload_label.config(text="Upload speed: \n" + str(upload_speed) + "MbPs")
    ping_label.config(text="Ping: \n" + str(ping_test) + "Ms")


root = Tk()

root.title("SpeedTest")
root.geometry('300x400')

download_label = Label(root, text="Download speed: \n-", font=35)
download_label.pack(pady=(50, 0))
upload_label = Label(root, text="Upload speed: \n-", font=35)
upload_label.pack(pady=(10, 0))
ping_label = Label(root, text="Ping: \n-", font=35)
ping_label.pack(pady=(5, 0))



button = Button(root, text="Start", font=40, command=runButt)
button.pack(side=BOTTOM, pady=40)

root.mainloop()