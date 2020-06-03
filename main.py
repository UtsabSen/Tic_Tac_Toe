from tkinter import *
from tkinter import messagebox

if __name__ == '__main__':
    root = Tk()
    root.geometry("425x380")
    root.title("TIC TAC TOE")
    root.resizable(FALSE, FALSE)


    class TicTacToe:
        plr1_name = "PLAYER 1"
        plr2_name = "PLAYER 2"
        player_1 = [0] * 9
        player_2 = [0] * 9
        player = 1


        def body(self, home):

            self.menu_bar = Menu(home)

            self.options = Menu(self.menu_bar, tearoff=0)
            self.options.add_command(label="New Game", command=self.player_name)
            self.options.add_command(label="Scoreboard")
            # self.options.add_command(label="Player Name")

            self.menu_bar.add_cascade(label="Menu", menu=self.options)
            home.config(menu=self.menu_bar)



            main_frame = Frame(home, bg="WHITE")

            self.pos_0 = Button(main_frame, text="    ", height=2, width=6, bg="WHITE",
                                font=("times new roman", 30), relief=RAISED, command=lambda: self.update_game(0))
            self.pos_0.grid(row=0, column=0)

            self.pos_1 = Button(main_frame, text="    ", height=2, width=6, bg="WHITE",
                                font=("times new roman", 30), relief=RAISED, command=lambda: self.update_game(1))
            self.pos_1.grid(row=0, column=1)

            self.pos_2 = Button(main_frame, text="    ", height=2, width=6, bg="WHITE",
                                font=("times new roman", 30), relief=RAISED, command=lambda: self.update_game(2))
            self.pos_2.grid(row=0, column=2)

            self.pos_3 = Button(main_frame, text="    ", height=2, width=6, bg="WHITE",
                                font=("times new roman", 30), relief=RAISED, command=lambda: self.update_game(3))
            self.pos_3.grid(row=1, column=0)

            self.pos_4 = Button(main_frame, text="    ", height=2, width=6, bg="WHITE",
                                font=("times new roman", 30), relief=RAISED, command=lambda: self.update_game(4))
            self.pos_4.grid(row=1, column=1)

            self.pos_5 = Button(main_frame, text="    ", height=2, width=6, bg="WHITE",
                                font=("times new roman", 30), relief=RAISED, command=lambda: self.update_game(5))
            self.pos_5.grid(row=1, column=2)

            self.pos_6 = Button(main_frame, text="    ", height=2, width=6, bg="WHITE",
                                font=("times new roman", 30), relief=RAISED, command=lambda: self.update_game(6))
            self.pos_6.grid(row=2, column=0)

            self.pos_7 = Button(main_frame, text="    ", height=2, width=6, bg="WHITE",
                                font=("times new roman", 30), relief=RAISED, command=lambda: self.update_game(7))
            self.pos_7.grid(row=2, column=1)

            self.pos_8 = Button(main_frame, text="    ", height=2, width=6, bg="WHITE",
                                font=("times new roman", 30), relief=RAISED, command=lambda: self.update_game(8))
            self.pos_8.grid(row=2, column=2)

            main_frame.pack(expand=True, fill=BOTH)

            self.player_name()

        def update_game(self, pos):
            if self.player == 1:
                self.player_1[pos] = 1
                if pos == 0:
                    self.pos_0.config(text="\u26CC", state=DISABLED)
                elif pos == 1:
                    self.pos_1.config(text="\u26CC", state=DISABLED)
                elif pos == 2:
                    self.pos_2.config(text="\u26CC", state=DISABLED)
                elif pos == 3:
                    self.pos_3.config(text="\u26CC", state=DISABLED)
                elif pos == 4:
                    self.pos_4.config(text="\u26CC", state=DISABLED)
                elif pos == 5:
                    self.pos_5.config(text="\u26CC", state=DISABLED)
                elif pos == 6:
                    self.pos_6.config(text="\u26CC", state=DISABLED)
                elif pos == 7:
                    self.pos_7.config(text="\u26CC", state=DISABLED)
                elif pos == 8:
                    self.pos_8.config(text="\u26CC", state=DISABLED)

                self.player = 2
            else:
                self.player_2[pos] = 1
                if pos == 0:
                    self.pos_0.config(text="\u25EF", state=DISABLED)
                elif pos == 1:
                    self.pos_1.config(text="\u25EF", state=DISABLED)
                elif pos == 2:
                    self.pos_2.config(text="\u25EF", state=DISABLED)
                elif pos == 3:
                    self.pos_3.config(text="\u25EF", state=DISABLED)
                elif pos == 4:
                    self.pos_4.config(text="\u25EF", state=DISABLED)
                elif pos == 5:
                    self.pos_5.config(text="\u25EF", state=DISABLED)
                elif pos == 6:
                    self.pos_6.config(text="\u25EF", state=DISABLED)
                elif pos == 7:
                    self.pos_7.config(text="\u25EF", state=DISABLED)
                elif pos == 8:
                    self.pos_8.config(text="\u25EF", state=DISABLED)

                self.player = 1

            self.check_winner()

        def check_winner(self):
            if (
                    self.player_1[0] == self.player_1[1] == self.player_1[2] == 1 or
                    self.player_1[3] == self.player_1[4] == self.player_1[5] == 1 or
                    self.player_1[6] == self.player_1[7] == self.player_1[8] == 1 or
                    self.player_1[0] == self.player_1[3] == self.player_1[6] == 1 or
                    self.player_1[1] == self.player_1[4] == self.player_1[7] == 1 or
                    self.player_1[2] == self.player_1[5] == self.player_1[8] == 1 or
                    self.player_1[0] == self.player_1[4] == self.player_1[8] == 1 or
                    self.player_1[2] == self.player_1[4] == self.player_1[6] == 1
            ):
                # print("PLAYER 1 WINS")
                messagebox._show(title="WINNER", message=self.plr1_name+" WINS")
                self.reset_board()
            elif (
                    self.player_2[0] == self.player_2[1] == self.player_2[2] == 1 or
                    self.player_2[3] == self.player_2[4] == self.player_2[5] == 1 or
                    self.player_2[6] == self.player_2[7] == self.player_2[8] == 1 or
                    self.player_2[0] == self.player_2[3] == self.player_2[6] == 1 or
                    self.player_2[1] == self.player_2[4] == self.player_2[7] == 1 or
                    self.player_2[2] == self.player_2[5] == self.player_2[8] == 1 or
                    self.player_2[0] == self.player_2[4] == self.player_2[8] == 1 or
                    self.player_2[2] == self.player_2[4] == self.player_2[6] == 1
            ):
                messagebox._show(title="WINNER", message=self.plr2_name+" WINS")
                self.reset_board()
            elif self.player_1.count(1) == 5 or self.player_2.count(1) == 5:
                messagebox._show(title="DRAW", message="IT IS A DRAW MATCH")
                self.reset_board()

        def player_name(self):
            self.plr1_name="Player 1"
            self.plr2_name="Player 2"

            self.options.entryconfig(0, state=DISABLED)
            self.block_board()
            self.frame_player_name = Frame(root, bg="WHITE")
            self.label_plr_1_icon = Label(self.frame_player_name, text="\u26CC",
                                          bg="WHITE", font=("times new roman", 15))
            self.label_plr_1_icon.grid(row=0, column=0)
            self.label_plr_1_name = Label(self.frame_player_name, text="Player 1:",
                                          bg="WHITE", font=("times new roman", 15))
            self.label_plr_1_name.grid(row=0, column=1)
            self.entry_plr_1_name = Entry(self.frame_player_name, relief=SOLID, font=("times new roman", 15))

            self.entry_plr_1_name.grid(row=0, column=2)

            self.label_plr_2_icon = Label(self.frame_player_name, text="\u25EF",
                                          bg="WHITE", font=("times new roman", 15))
            self.label_plr_2_icon.grid(row=1, column=0)
            self.label_plr_2_name = Label(self.frame_player_name, text="Player 2:",
                                          bg="WHITE", font=("times new roman", 15))
            self.label_plr_2_name.grid(row=1, column=1)
            self.entry_plr_2_name = Entry(self.frame_player_name, relief=SOLID, font=("times new roman", 15))
            self.entry_plr_2_name.grid(row=1, column=2)

            self.entry_plr_2_name.bind("<Return>", self.done_player_name)

            self.button_ok = Button(self.frame_player_name, text="OK", font=("times new roman", 15), relief=GROOVE,
                                    command=self.done_player_name)
            self.button_ok.grid(row=2, column=0, columnspan=3)
            self.frame_player_name.place(relx=0.5, rely=0.5, anchor=CENTER)

        def done_player_name(self, event=None):
            if self.entry_plr_1_name.get() != "":
                self.plr1_name = self.entry_plr_1_name.get()
            if self.entry_plr_2_name.get() != "":
                self.plr2_name = self.entry_plr_2_name.get()

            self.frame_player_name.destroy()
            self.reset_board()
            self.options.entryconfig(0, state=NORMAL)

        def block_board(self):
            self.pos_0.config(text="    ", state=DISABLED)
            self.pos_1.config(text="    ", state=DISABLED)
            self.pos_2.config(text="    ", state=DISABLED)
            self.pos_3.config(text="    ", state=DISABLED)
            self.pos_4.config(text="    ", state=DISABLED)
            self.pos_5.config(text="    ", state=DISABLED)
            self.pos_6.config(text="    ", state=DISABLED)
            self.pos_7.config(text="    ", state=DISABLED)
            self.pos_8.config(text="    ", state=DISABLED)

        def reset_board(self):
            self.player_1 = [0] * 9
            self.player_2 = [0] * 9
            self.player = 1
            self.pos_0.config(text="    ", state=NORMAL)
            self.pos_1.config(text="    ", state=NORMAL)
            self.pos_2.config(text="    ", state=NORMAL)
            self.pos_3.config(text="    ", state=NORMAL)
            self.pos_4.config(text="    ", state=NORMAL)
            self.pos_5.config(text="    ", state=NORMAL)
            self.pos_6.config(text="    ", state=NORMAL)
            self.pos_7.config(text="    ", state=NORMAL)
            self.pos_8.config(text="    ", state=NORMAL)



    obj = TicTacToe()
    obj.body(root)

    root.mainloop()
