import customtkinter as ctk
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

        self.start_button = ctk.CTkButton(self.master,
                                    fg_color='green',
                                    hover_color='darkgreen',
                                    text="Start",
                                    font=('Arial bold', 28),
                                    command=self.start_timer,
                                    width=300, height=100,
                                    border_width=5,
                                    border_color='black',
                                    corner_radius=30)
        self.start_button.place(relx=0.3, rely=0.6, anchor='center')

        self.reset_button = ctk.CTkButton(self.master,
                                    fg_color='yellow',
                                    hover_color='#F2B705',
                                    text_color='black',
                                    text="Reset",
                                    font=('Arial bold', 28),
                                    command=self.reset_timer,
                                    width=300, height=100,
                                    border_width=5,
                                    border_color='black',
                                    corner_radius=30)
        self.reset_button.place(relx=0.7, rely=0.6, anchor='center')

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
        self.running = True
        self.start_button._fg_color='darkred'
        self.start_button._hover_color='red'
        self.start_button.configure(text='Stop')
        self.start_button.configure(command=self.stop_timer)
        self.reset_button._state='disabled'
        self.timer()

    def stop_timer(self):
        self.running = False
        self.start_button._fg_color='green'
        self.start_button._hover_color='darkgreen'
        self.start_button.configure(text='Start')
        self.start_button.configure(command=self.start_timer)
        self.reset_button._state='normal'

    def reset_timer(self):
        self.miliseconds = 0
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.timerLabel.configure(text=f"{'{:02d}'.format(self.hours)}:{'{:02d}'.format(self.minutes)}:{'{:02d}'.format(self.seconds)}:{'{:02d}'.format(self.miliseconds)}")
        
if __name__=='__main__':
   app = ctk.CTk()
   gui = App(master=app)
   app.mainloop()