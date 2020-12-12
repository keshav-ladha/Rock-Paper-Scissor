import tkinter as tk
import random

root = tk.Tk()
root.title("R.P.S.")
root.geometry("245x275")

u_c = ""
c_c = ""
u_s = 0
c_s = 0
def c_t_n(choice):
    a={
        "rock":0,
        "paper":1,
        "scissor":2
    }
    return a[choice]

def n_t_c(choice):
    a={
        0:"rock",
        1:"paper",
        2:"scissor"
    }
    return a[choice]

def result(user,comp):
    global u_c
    global u_s
    global c_c
    global c_s
    u_c = c_t_n(user)
    c_c = c_t_n(comp)
    if (u_c-c_c)%3==1:
        u_s+=1
        print("You Win!")
    elif u_c==c_c:
        print("Tie!")
    else:
        c_s+=1
    text_area = tk.Text(master=root,height=12,width=30,bg="#FFFF99")
    text_area.grid(column=0,row=4)
    answer = f" Your Choice:{n_t_c(u_c)}\n My Choice :{n_t_c(c_c)}\n Your Score :{u_s}\n Computer Score :{c_s}"    
    text_area.insert(tk.END,answer)

def random_comp():
    a = ["rock","paper","scissor"]
    b = random.randint(0,2)
    c = a[b]
    return c

def rock():
    global u_c
    global c_c
    u_c = "rock"
    c_c = random_comp()
    result(u_c,c_c)

def scissor():
    global u_c
    global c_c
    u_c = "scissor"
    c_c = random_comp()
    result(u_c,c_c)

def paper():
    global u_c
    global c_c
    u_c = "paper"
    c_c = random_comp()
    result(u_c,c_c)


button1 = tk.Button(text="Rock", bg="skyblue",fg="white",padx=100,command=rock)
button2 = tk.Button(text="Paper", bg="pink",fg="white",padx=100,command=paper)
button3 = tk.Button(text="Scissor", bg="yellow",fg="white",padx=100,command=scissor)

button1.grid(row=1, column=0)
button2.grid(row=2, column=0)
button3.grid(row=3, column=0)



root.mainloop()