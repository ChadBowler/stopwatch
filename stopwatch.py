import customtkinter as ctk

class App:
    def __init__(self, master) -> None:
        self.master = master
        self.master.geometry('800x500')
        self.master.wm_title('Stopwatch')

        self.button = ctk.CTkButton(self.master,
                                    fg_color='green',
                                    hover_color='darkgreen',
                                    text="Start",
                                    font=('Arial bold', 28),
                                    command=self.button_event,
                                    width=300, height=100,
                                    corner_radius=30)
        self.button.place(relx=0.5, rely=0.4, anchor='center')


    def button_event(self):
        print("button pressed")

if __name__=='__main__':
   app = ctk.CTk()
   gui = App(master=app)
   app.mainloop()