from tkinter import *
foto_list=["pilt1.png","pilt2.png","pilt3.png","pilt4.png"]
list_=["Arkadiy","Andrey","Vjatseslav","Valentin"]
def list_to_txt(event):
    global can,foto#----------------
    txt.delete(0.0,END)
    valik=lbox.curselection()
    txt.insert(END,lbox.get(valik[0]))
    can.delete(ALL)#---------------
    foto=PhotoImage(file=foto_list[valik[0]])#-------------
    can.create_image(0,0,image=foto,anchor=NW)#-----------------

def txt_to_list(event):
    text=txt.get(0.0,END)
    text=text[-2:-1]
    if text=="\n":
        pass
    else:
        list_.append(text)
        print(list_)
        lbox.config(height=len(list_))
        lbox.insert(END,text)   
        txt.delete(0.0,END)



def opisanie():
    text = txt.get(0.0, END)
    print(list(text))
    if text=="pilt1.png\n":
        ttt="Милый котик без породы. Зовут Аркадий. 4 года."
    elif text=="pilt2.png\n":
        ttt="Породистый английский кот Андрей. 2 года."
    elif text=="pilt3.png\n":
        ttt="Европейский кот Вячеслав. 10 лет."
    elif text=="pilt4.png\n":
        ttt="Кот Валентин Владимирович. Отзывается на ""Депутат"", 7 лет."
    opis.config(text=ttt)

win=Tk()
lbox=Listbox(win,width=20,height=len(foto_list),selectmode=SINGLE)

for element in foto_list:
    lbox.insert(END,element)

lbox.grid(row=0,column=0)
lbox.bind("<<ListboxSelect>>",list_to_txt)
txt=Text(win,height=1,width=20,wrap=WORD)
txt.grid(row=0,column=1)
txt.bind("<Return>",txt_to_list)
can=Canvas(win,width=130,height=130,bg="gold")#--------------
can.grid(row=1,column=2,columnspan=2)#--------------------
foto=PhotoImage(file="pilt1.png")#----------------
can.create_image(0,0,image=foto,anchor=NW)#-----------------

btn=Button(win,text="Cправка",fg="Black",bg="white",font="Arial 20",width=10, command=opisanie)
btn.grid(row=1,columns=2)
opis=Label(win, text="DESCRIPTION", width=150, height=20)
opis.grid(row=1, column=5)

win.mainloop()



