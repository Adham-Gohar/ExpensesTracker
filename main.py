""" PY Expense Tracker """

""" Modules in this app"""
import tkinter as tk
import customtkinter
from PIL import Image, ImageTk
import os
import ui

""" Some necessary initialozations """
PATH = os.path.dirname(os.path.realpath(__file__))

#These are required in order to use the custom tkinter library
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

""" Start app class"""

class App(customtkinter.CTk):
    WIDTH = 340
    HEIGHT = 650

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        """App location, title, and sizing"""

        self.title("Expense Tracker")
        self.resizable(False, False)

        screenHeight = self.winfo_screenheight()
        screenWidth = self.winfo_screenwidth()

        x = (screenWidth / 2) - (App.WIDTH / 2)
        y = (screenHeight / 2) - (App.HEIGHT / 2)

        self.geometry(f"{App.WIDTH}x{App.HEIGHT}+{int(x)}+{int(y)}")

        self.config(background=ui.Color.MAIN)

        self.setup_ui()

        self.InsertButton = customtkinter.CTkButton(
        self,
        text=None,
        fg_color=ui.Color.PURPLE,
        corner_radius=50,
        text_font=ui.Font.MID,
        width=30,
        height=30,
        hover=False,
        command=self.EntryAnimation,
        )
        self.InsertButton.pack(
            side=tk.BOTTOM, fill=tk.Y, expand=False, pady=20, ipady=10, ipadx=10
        )



        self.PlusLabel = tk.Label(
            self.InsertButton,
            bg=ui.Color.PURPLE,
            text="+",
            font=ui.Font.BTN,
        )
        self.PlusLabel.place(relx=0.5, rely=0.5, anchor="center")


        """space fram above the button"""
        self.space = customtkinter.CTkFrame(
            self, fg_color=ui.Color.MAIN, height=1,corner_radius=0
        )
        self.space.pack(side=tk.BOTTOM, fill=tk.X, expand=False, padx=40)

        """Border spaces for the app"""
        self.space = customtkinter.CTkFrame(
            self, fg_color=ui.Color.MAIN, width=20, corner_radius=0
        )
        self.space.pack(side=tk.LEFT, fill=tk.Y, expand=False)

        self.space = customtkinter.CTkFrame(
            self, fg_color=ui.Color.MAIN, width=20, corner_radius=0
        )
        self.space.pack(side=tk.RIGHT, fill=tk.Y, expand=False)

        self.space = customtkinter.CTkFrame(
            self, fg_color=ui.Color.MAIN, height=20, corner_radius=0
        )
        self.space.pack(side=tk.TOP, fill=tk.X, expand=False)

        """Title in the app"""

        self.NameFrame = customtkinter.CTkFrame(self, fg_color=ui.Color.MAIN)
        self.NameFrame.pack(side=tk.TOP, fill=tk.X, expand=False)

        self.NameLabel = customtkinter.CTkLabel(
            self.NameFrame,
            bg=ui.Color.MAIN,
            text="Hi, Adham",
            justify=tk.LEFT,
            font=ui.Font.NAME,
        )

        self.NameLabel.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

        self.space = customtkinter.CTkFrame(
            self, fg_color=ui.Color.MAIN, height=40, corner_radius=0
        )
        self.space.pack(side=tk.TOP, fill=tk.X, expand=False)

        """Card with information"""

        self.CardFrame = customtkinter.CTkFrame(self, fg_color=ui.Color.PURPLE)
        self.CardFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=False)


        self.space = customtkinter.CTkFrame(self.CardFrame, fg_color=ui.Color.PURPLE, height=20)
        self.space.pack(side=tk.TOP, fill=tk.X, expand=False, pady=3, padx=3)


        """Card title and other subtitles"""
        self.TitleFrame = customtkinter.CTkFrame(
            self.CardFrame, width=60, height=60, fg_color=ui.Color.PURPLE
            )
        self.TitleFrame.pack(side=tk.TOP, fill=tk.X, expand=False, padx=10)
        self.Title = tk.Label(
            self.TitleFrame,
            bg=ui.Color.PURPLE,
            text="BALANCE",
            fg="#e5e5e5"
        )
        self.Title.pack(side=tk.LEFT, padx=10)

        self.BalanceFrame = customtkinter.CTkFrame(
            self.CardFrame, width=60, height=60, fg_color=ui.Color.PURPLE
        )
        self.BalanceFrame.pack(side=tk.TOP, fill=tk.X, expand=False, padx=10)
        
        self.Balance = tk.Label(
            self.BalanceFrame,
            bg=ui.Color.PURPLE,
            text="$1,700.00",
            font=ui.Font.BALANCE,
        )
        self.Balance.pack(side=tk.LEFT, padx=10)

        self.space = customtkinter.CTkFrame(self.CardFrame, fg_color=ui.Color.PURPLE, height=20)
        self.space.pack(side=tk.TOP, fill=tk.X, expand=False)

        self.space = customtkinter.CTkFrame(self.CardFrame, fg_color=ui.Color.PURPLE, height=20)
        self.space.pack(side=tk.BOTTOM, fill=tk.X, expand=False, pady=5, padx=3)

        self.InFrame = customtkinter.CTkFrame(
            self.CardFrame,
            width=0,
            height=60,
            fg_color=ui.Color.PURPLE,
        )
        self.InFrame.pack(side=tk.LEFT, fill=tk.X, expand=False, padx=10)

        """Spent and income labels"""
        self.SpentLabel = tk.Label(
            self.InFrame,
            text="INCOME",
            bg=ui.Color.PURPLE,
            justify="left",
            font=ui.Font.MID,
            fg="#e5e5e5",
        )
        self.SpentLabel.pack(side=tk.TOP,fill=tk.X,expand=False,anchor="w", padx=10)

        self.SpentValueLabel = tk.Label(
            self.InFrame,
            text="+$1,500.00",
            bg=ui.Color.PURPLE,
            justify="left",
            font=ui.Font.BTN,
        )
        self.SpentValueLabel.pack(side=tk.TOP, fill=tk.X, expand=True, anchor="w", padx=10)

        self.OutFrame = customtkinter.CTkFrame(
            self.CardFrame, width=0, height=60, fg_color=ui.Color.PURPLE
        )
        self.OutFrame.pack(
            side=tk.LEFT,
            fill=tk.X,
            expand=False,
            padx=5,
        )

        self.ExpensesLabel = tk.Label(
            self.OutFrame,
            text="EXPENSES",
            bg=ui.Color.PURPLE,
            justify="left",
            font=ui.Font.MID,
            fg="#e5e5e5",
        )
        self.ExpensesLabel.pack(
            side=tk.TOP, fill=tk.X, expand=False, anchor="w", padx=10
        )

        self.ExpensesValueLabel = tk.Label(
            self.OutFrame,
            text="-$800.00",
            bg=ui.Color.PURPLE,
            justify="left",
            font=ui.Font.BTN,
            width=0
        )
        self.ExpensesValueLabel.pack(
            side=tk.TOP, fill=tk.X, expand=True, anchor="w", padx=10
        )

        self.space = customtkinter.CTkFrame(
            self, fg_color=ui.Color.MAIN, height=40, corner_radius=0
        )
        self.space.pack(side=tk.TOP, fill=tk.X, expand=False)

        """Analytics Section"""

        self.ButtonFrame = customtkinter.CTkFrame(self, fg_color=ui.Color.MAIN)
        self.ButtonFrame.pack(side=tk.TOP, fill=tk.X, expand=False)

        self.ButtonTop = customtkinter.CTkFrame(self.ButtonFrame, fg_color="purple", height=50)
        self.ButtonTop.pack(side=tk.TOP, fill=tk.X, expand=False)


        self.ExpenseLabel = tk.Label(
            self.ButtonTop,
            text="Expenses",
            bg=ui.Color.MAIN,
            font=ui.Font.LABEL,
            fg=ui.Color.PURPLE,
        )
        self.ExpenseLabel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.TransactionLabel = tk.Label(
            self.ButtonTop,
            text="Transactions",
            bg=ui.Color.MAIN,
            font=ui.Font.LABEL,
            fg="#e5e5e5",
        )
        self.TransactionLabel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        
        self.LineFrame = customtkinter.CTkFrame(
            self.ButtonFrame, fg_color=ui.Color.MAIN, height=20
        )
        self.LineFrame.pack(
            side=tk.TOP,
            fill=tk.X,
            expand=False,
        )


        self.InFrame = customtkinter.CTkFrame(
            self.LineFrame, fg_color=ui.Color.MAIN, width=0,height=20
        )
        self.InFrame.pack(
            side=tk.LEFT,
            fill=tk.X,
            expand=True,      
        )


        self.ExpenseLine = customtkinter.CTkFrame(
            self.InFrame, height=3, fg_color=ui.Color.PURPLE, width=0
        )
        self.ExpenseLine.pack(side=tk.LEFT, fill=tk.X, expand=True, pady=10)
        
        self.InFrame1 = customtkinter.CTkFrame(
            self.LineFrame, fg_color=ui.Color.MAIN, width=0, height=20
        )
        self.InFrame1.pack(
            side=tk.RIGHT,
            fill=tk.X,
            expand=True,
        )
        
        self.TransactionLine = customtkinter.CTkFrame(
            self.InFrame1, height=3, fg_color="#bbbbbb", width=0
        )
        self.TransactionLine.pack(side=tk.LEFT, fill=tk.X, expand=True, pady=10)

        """Entry Form UI"""
        self.EntryForm = customtkinter.CTkFrame(self, fg_color=ui.Color.CARD)
        self.EntryForm.grid_columnconfigure((0, 3), minsize=40)


        self.EntryForm.grid_rowconfigure((0, 12), minsize=20)

        self.EntryForm.grid_rowconfigure((3, 6, 8, 10), minsize=20)

        self.EntryForm.grid_columnconfigure((1, 2), weight=1)
        self.EntryForm.grid_rowconfigure((1, 2, 4, 5, 7, 9, 11), weight=1)

        self.DiscriptionLabel = tk.Label(
            self.EntryForm,
            text="Description",
            bg=ui.Color.CARD,
            font=ui.Font.SMALL,
            justify="left",
            fg="grey75"
        )
        self.DiscriptionLabel.grid(row=1, column=1, columnspan=2, sticky="w")

        self.DiscriptionEntry = customtkinter.CTkEntry(
            self.EntryForm, fg_color=ui.Color.CARD, border_width=0, justify="left"
        )
        self.DiscriptionEntry.grid(row=2, column=1, columnspan=2, sticky="swe")

        self.UnderLineEntry = customtkinter.CTkFrame(
            self.DiscriptionEntry, fg_color="white", height=1
        )
        self.UnderLineEntry.pack(row=0, column=0, sticky="swe")

        self.QuantityLabel = tk.Label(
            self.EntryForm,
            text="Amount",
            bg=ui.Color.CARD,
            font=ui.Font.SMALL,
            justify="left",
            fg="grey75",
        )
        self.QuantityLabel.grid(row=4, column=1, sticky="w")

        self.QuantityEntry = customtkinter.CTkEntry(
            self.EntryForm, fg_color=ui.Color.CARD, border_width=0, justify="left"
        )
        self.QuantityEntry.grid(row=5, column=1, sticky="swe")

        self.underLineEntry = customtkinter.CTkFrame(
            self.QuantityEntry, fg_color="white", height=1
        )
        self.underLineEntry.grid(row=0, column=0, sticky="swe")

        self.TypeMenu = customtkinter.CTkOptionMenu(
            self.EntryForm,
            state="readonly",
            fg_color=ui.Color.MENU,
            button_color=ui.Color.MENU,
            values=["Spent", "Income"],
        )
        self.TypeMenu.grid(row=7, column=1, sticky="we")
        self.TypeMenu.set("Select type...")

        self.TypeMenu = customtkinter.CTkOptionMenu(
            self.EntryForm,
            state="readonly",
            fg_color=ui.Color.MENU,
            button_color=ui.Color.MENU,
            values=["Food and drink", "Entertaiment", "Finances", "Utilities", "Income"],
        )
        self.TypeMenu.grid(row=9, column=1, columnspan=1, sticky="we")
        self.TypeMenu.set("Select expense...")

        self.ButtonFrame = customtkinter.CTkFrame(self.EntryForm, fg_color=ui.Color.CARD)
        self.ButtonFrame.grid(row=11, column=1, columnspan=2, sticky="nswe")

        self.InsertButton = customtkinter.CTkButton(
            self.ButtonFrame,
            text="Submit",
            fg_color=ui.Color.MENU,
            corner_radius=10,
            width=0,
            hover=None,
        )
        self.InsertButton.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, ipadx=10)

        self.InsertButton = customtkinter.CTkButton(
            self.ButtonFrame,
            text="Cancel",
            fg_color=ui.Color.MENU,
            corner_radius=10,
            width=0,
            command=self.RemoveEntryForm,
            hover=None,
        )
        self.InsertButton.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, ipadx=10)


        self.AddExpense()

        self.keyBindings()

        """ Gather all jey bindings in one function"""
    def keyBindings(self):
        """ There commands bind the expense and transaction buttons to change color  and moce line when clicked"""
        self.TransactionLabel.bind("<Button-1>", lambda e: self.moveRight(e))
        self.ExpensesLabel.bind("<Button-1>", lambda e: self.moveLeft(e))

    def RemoveEntryForm(self):
        for y in range(21, 31, 1):
            self.EntryForm.update()
            self.EntryForm.place(relx=0.5, y=y**2, anchor="center")

    def EntryAnimation(self):
        for y in range (-31, -22, 1):
            self.EntryForm.update()
            self.EntryForm.place(relx=0.5, y=y**2 - 20, anchor="center")



    

    """Both therse functions carry out the UI fot the tab changes
      when opposite button is clicked, we simply switch the colors to the side being clicked"""
    def moveRight(self, event):
        self.TransactionLine.configure(fg_color="#bbbbbb")
        self.TransactionLabel.configure(fg="#bbbbbb")
        self.ExpenseLine.configure(fg_color=ui.Color.PURPLE)
        self.ExpenseLabel.configure(fg=ui.Color.PURPLE)
    
    def moveLeft(self, event):
        self.TransactionLine.configure(fg_color=ui.Color.PURPLE)
        self.TransactionLabel.configure(fg=ui.Color.PURPLE)
        self.ExpenseLine.configure(fg_color="#bbbbbb")
        self.ExpenseLabel.configure(fg="#bbbbbb")



    
    """The add expense function adds new entries to the main UI display """

    def AddExpense(self):
        self.space = customtkinter.CTkFrame(self, height=5, fg_color=ui.Color.MAIN)
        self.space.pack(side=tk.TOP, fill=tk.X, expand=False)
        self.space.lower()

        self.TitleLabel = ["Finances", "Food & Drinks", "Entertaiment"]
        self.SubtitleLabel = ["23 transactions", "10 transactions", "5 transactions"]
        self.ValueLabel = ["-$800.00", "-$500.00", "-$200.00"]

        for i in range(1, 4):
            self.frame = customtkinter.CTkFrame(
                self,
                fg_color=ui.Color.MAIN,
                corner_radius=10,
                )
            self.frame.pack(side=tk.TOP, fill=tk.X, expand=False)

            self.frame.grid_rowconfigure(1, minsize=0)
            self.frame.grid_rowconfigure((2, 3), weight=1)
            self.frame.grid_rowconfigure((0, 4), minsize=5)

            self.frame.grid_columnconfigure((0, 2, 6), minsize=8)
            self.frame.grid_columnconfigure((1, 3, 5), weight=0)
            self.frame.grid_columnconfigure((4), weight=1)

            """We can call some images to use in the app"""    

            if i == 1 or i == 2 or i == 3:
                self.img = self.LoadImage(f"/{i}.png", 22)

                self.CardTypeLabel = customtkinter.CTkButton(
                    self.frame,
                    fg_color=ui.Color.MAIN,
                    width=0,
                    height=0,
                    corner_radius=15,
                    text=None,
                    image=self.img,
                    hover="disabled",
                )
                self.CardTypeLabel.grid(
                    row=2,
                    column=1,
                    rowspan=2,
                    sticky="nsw",
                )

                self.one = customtkinter.CTkLabel(
                    self.frame,
                    width=0,
                    height=0,
                    fg_color=ui.Color.MAIN,
                    text_font=ui.Font.LABEL,
                    justify="left",
                )
                self.one.grid(row=2, column=3, sticky="w")

                self.two = customtkinter.CTkLabel(
                    self.frame,
                    width=0,
                    height=0,
                    fg_color=ui.Color.MAIN,
                    text_font=ui.Font.VALUE,
                    justify="right",
                )
                self.two.grid(row=2, column=5, sticky="e")

                self.three = customtkinter.CTkLabel(
                    self.frame,
                    width=0,
                    height=0,
                    fg_color=ui.Color.MAIN,
                    text_font=ui.Font.MID,
                    text_color = "#e5e5e5",
                )
                self.three.grid(row=3, column=3, sticky="w")

                """we add a space frame after each entery frame for etter visualizations"""
                self.space = customtkinter.CTkFrame(self, fg_color=ui.Color.MAIN, height=10)
                self.space.pack(side=tk.TOP, fill=tk.X, expand=False)

                self.one.configure(text=self.TitleLabel[i - 1])
                self.two.configure(text=self.ValueLabel[i - 1])
                self.three.configure(text=self.SubtitleLabel[i - 1])

                self.space.lower()
                self.frame.lower()
                
                   

    """Load image function that returns a path"""
    def LoadImage(self, path, image_size):
        return ImageTk.PhotoImage(
            Image.open(PATH + path).resize((image_size, image_size))
        )


    
    def setup_ui(self):
        ui.setup_ui(self)
    

    #Application ==> close window when user quits
    def on_closing(self, event=0):
        self.destroy()

    #Application ==> start app mainloop
    def start(self):
        self.mainloop()

if __name__ == "__main__":
    app = App()
    app.start() #calls the start method        