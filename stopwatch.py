import customtkinter as ctk
import datetime
import time
from tkinter import ttk



class App:
    def __init__(self, master) -> None:
        self.master = master
        self.master.geometry('800x500')
        self.master.wm_title('Stopwatch')

        self.miliseconds = 0
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.running = False
        

        self.timerLabel = ctk.CTkLabel(self.master, text=f"{'{:02d}'.format(self.hours)}:{'{:02d}'.format(self.minutes)}:{'{:02d}'.format(self.seconds)}:{'{:02d}'.format(self.miliseconds)}", font=('Arial bold', 28))
        self.timerLabel.place(relx=0.425, rely=0.1)


        self.button = ctk.CTkButton(self.master,
                                    fg_color='green',
                                    hover_color='darkgreen',
                                    text="Start",
                                    font=('Arial bold', 28),
                                    command=self.start_timer,
                                    width=300, height=100,
                                    border_width=5,
                                    border_color='black',
                                    corner_radius=30)
        self.button.place(relx=0.5, rely=0.6, anchor='center')

    def timer(self):
        if self.running:
            self.timerLabel.after(10, self.timer)
           
            
            if self.miliseconds == 99:
                self.miliseconds = -1
                if self.seconds == 59:
                    self.seconds = -1
                    if self.minutes == 59:
                        self.minutes = -1
                        self.hours += 1
                    self.minutes += 1
                self.seconds += 1
            self.miliseconds += 1
            self.timerLabel.configure(text=f"{'{:02d}'.format(self.hours)}:{'{:02d}'.format(self.minutes)}:{'{:02d}'.format(self.seconds)}:{'{:02d}'.format(self.miliseconds)}")


    def start_timer(self):
        self.start_time = int(time.time())
        self.running = True
        self.button._fg_color='darkred'
        self.button._hover_color='red'
        self.button.configure(text='Stop')
        self.button.configure(command=self.stop_timer)
        self.timer()

    def stop_timer(self):
        self.running = False
        self.button._fg_color='green'
        self.button._hover_color='darkgreen'
        self.button.configure(text='Start')
        self.button.configure(command=self.start_timer)
        
        

if __name__=='__main__':
   app = ctk.CTk()
   gui = App(master=app)
   app.mainloop()