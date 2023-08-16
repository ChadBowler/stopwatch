import customtkinter as ctk
import datetime

class App:
    def __init__(self, master) -> None:
        self.master = master
        self.master.geometry('800x500')
        self.master.wm_title('Stopwatch')

        self.timer = '00:00:00'

        self.label = ctk.CTkLabel(self.master, text=self.timer, font=('Arial bold', 28))
        self.label.place(relx=0.425, rely=0.2)

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


    def start_timer(self):
        now = datetime.datetime.now
        self.button._fg_color='darkred'
        self.button._hover_color='red'
        self.button.configure(text='Stop')
        self.button.configure(command=self.stop_timer)
        print(self.button)

    def stop_timer(self):
        self.button._fg_color='green'
        self.button._hover_color='darkgreen'
        self.button.configure(text='Start')
        self.button.configure(command=self.start_timer)
        

if __name__=='__main__':
   app = ctk.CTk()
   gui = App(master=app)
   app.mainloop()