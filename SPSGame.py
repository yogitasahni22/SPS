import tkinter as tk
import random
from tkinter import messagebox


def stone():
    computer_choice = choices[random.randint(0, 2)]
    choice = "Stone"
    if (choice == 'Stone'):
        if (computer_choice == 'Stone'):
            print("**It's a tie**")
            result=-1
        elif (computer_choice == 'Scissors'):
            print("**You won**")
            result=1
        else:
            print(("**You lose**"))
            result=0
    #return your_score,computer_score
    callback(choice,computer_choice,result)
def paper():

    computer_choice = choices[random.randint(0, 2)]
    choice = "Paper"
    if (choice == 'Paper'):

        if (computer_choice == 'Paper'):
            print("**It's a tie**")
            result=-1
        elif (computer_choice == 'Stone'):
            print("**You won**")
            result=1
        else:
            print(("**You lose**"))
            result=0
    #return your_score, computer_score
    callback(choice,computer_choice,result)


def scissors():
    computer_choice = choices[random.randint(0, 2)]
    choice = "Scissors"
    if (choice == 'Scissors'):
        if (computer_choice == 'Scissors'):
            print("**It's a tie**")
            result=-1
        elif (computer_choice == 'Paper'):
            print("**You won**")
            result =1
           # your_score += 1
        else:
            print(("**You lose**"))
            result=0
           # computer_score += 1

    callback(choice,computer_choice,result)
    #return your_score, computer_score

def callback(choice,computer_choice,result):
    your_score = 0
    computer_score = 0
    if(result ==-1):
        pass
    elif(result==1):
        your_score+=1
    else:
        computer_score+=1
    answer = "Your's Choice ={}\nComputer's choice={}\nYour Score={}\nComputer's score={}".format(choice,
                                                                                                  computer_choice,
                                                                                                  your_score,
                                                                                                  computer_score)
    messagebox.showinfo("Score Board",answer)

   # logic()
"""    text_area = tk.Text(master=window, height=12, width=30)
    #text_area.grid(column=0, row=4)
    answer = "Your's Choice ={}\nComputer's choice={}\nYour Score={}\nComputer's score={}".format(choice,
                                                                                                  computer_choice,
                                                                                                  your_score,
                                                                                          computer_score)
    text_area.insert(tk.END, answer)
    text_area.pack()
    """



def logic():
    root.withdraw()
    window =tk.Toplevel()
    #photo = tk.PhotoImage(file =r"C:\Users\vritti\Pictures\Python pictures\StoneImage(1).png")
    btn1 = tk.Button(master = window,text ="STONE", command =stone,font = ("Times",15,"bold"),bg = "darkslategray3",relief ="ridge")
    btn1.place(x=130,y=0)
   # btn1.pack()
    btn2 = tk.Button(master = window,text="PAPER", command=paper, font=("Times", 15, "bold"),bg ="thistle",relief ="ridge")
    btn2.place(x=230, y=0)
    #btn2.pack()
    btn3 = tk.Button(master =window,text = "SCISSORS", command=scissors, font=("Times", 15, "bold"),bg ="wheat3",relief ="ridge")
    btn3.place(x=325, y=0)
    #btn3.pack()
    btn4 = tk.Button(master = window, text="Quit", command = window.destroy , font=("Arial", 15, "italic"))
    btn4.place(x=250,y=250)
    canvas1 = tk.Canvas(window, width = 1000, height = 190)
    canvas1.place(x=170,y=50)
    img1 = tk.PhotoImage(file=r"stonepaperscissor1.png")
    canvas1.create_image(0,0,anchor ="nw",image=img1)



    window.geometry("600x300+320+220")
    window.mainloop()


global choices
choices = ["Stone", "Paper", "Scissors"]
root = tk.Tk()
title = root.title("STONE-PAPER-SCISSORS")
w_label1 = tk.Label(root,text = "STONE PAPER SCISSORS\n GAME", font = ("Fixedsys", 30, "bold"), fg="SystemWindowFrame",bg ="floralwhite")
w_label1.pack(fill="both")
w_label2 = tk.Label(root,text = "Developed By\n #YoVri", font = ("Helvetica", 15, "italic"),fg = "SystemWindowText",bg = "rosybrown1")
w_label2.pack(fill ="both")
w_button = tk.Button(root, text="Start", command = logic , font = ("Arial",22,"bold"), fg = "SystemButtonShadow",bg ="palevioletred",relief ="sunken")
w_button.place(x=250,y=180)
root.geometry("600x300+320+220")
root.mainloop()
