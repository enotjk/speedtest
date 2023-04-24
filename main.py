from tkinter import *
from speedtest import Speedtest

def runButt():
    st = speedtest.Speedtest()
    st.get_best_server()

    download_label.config(text="Download speed: \n" + str(round(st.download() / (10**6), 2)) + "MbPs")
    upload_label.config(text="Upload speed: \n" + str(round(st.upload() / (10**6), 2)) + "MbPs")
    ping_label.config(text="Ping: \n" + str(round(st.results.ping, 2)) + "Ms")


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

