from tkinter import *
from tkinter import messagebox
import tkinter as tk
root=tk.Tk()
root.title("Contact Manager")
root.iconbitmap("cm_icon.ico")
root.geometry('500x300')
root.config(bg='black')
root.resizable(width=False,height=False)

contact_list={}
blocked_list=[]
restore=[]
deleted=[]
global l

    
def view_contacts():
    global win
    win=Toplevel(root,bg='black')
    win.title("SAVED")
    win.geometry('350x350')
    win.resizable(width=False,height=False)

    show=Label(win,text='NAME    --   PHONE',bg='blue',fg='white',width='80',font=('Times','15'))
    show.pack()
    
    if(contact_list=={}):
        curr=Label(win,text='No Contacts',fg='white',bg='black',font=('Times','18'))
        curr.pack()
    else:
        global con
        k=0
        frame=Frame(win,width=40,height=40)
        frame.pack()
        def block_contact():
            x=l.curselection()
            for i in x:
                if(l.get(i) not in blocked_list):
                    blocked_list.append(l.get(i))
                l.delete(i)
                return blocked_list
        def delete_contact():
            x=l.curselection()
            for i in x:
                if (l.get(i) not in deleted):
                    deleted.append(l.get(i))
                l.delete(i)
               
                
    
        l=Listbox(frame,width='30',height='10',bg='black',fg='white',selectmode=MULTIPLE,font=('calibri','16'))
        s=Scrollbar(frame,bg='black',command=l.yview)
        #r=Scrollbar(frame,command=l.xview)
        #l.configure(xscrollcommand=r.set)
        l.configure(yscrollcommand=s.set)
        s.pack(side=RIGHT,fill=Y)
        for i,j in contact_list.items():
            con=''
            
            con+=i+' : '+j
            if(con not in deleted and con not in blocked_list):
                l.insert(k,con)
   
            l.pack(side=LEFT)
            k=k+1
        #r.pack(side=BOTTOM,fill=X)
        

        fr=Frame(win,width='40',height='30',bg='black')
        fr.pack(fill=BOTH)
        bloc=Button(fr,text='BLOCK',padx=20,pady=10,bg='black',font=('Calibri','16'),fg='white',command=lambda:block_contact())
        bloc.pack(side=LEFT)
        delete=Button(fr,text='DELETE',padx=20,pady=10,bg='black',font=('Calibri','16'),fg='white',command=lambda:delete_contact())
        delete.pack(side=RIGHT)



            
def create_contact():
    win=Toplevel(root,bg='black')
    win.title("ADD")
    win.geometry('370x315')
    win.resizable(width=False,height=False)
    name=Label(win,text='Enter Name',width='40',bg='black',fg='white',font=('Arial Black','20'))
    name.pack()
    space=Label(win,bg='black')
    space.pack()
    text_input=StringVar()
    namev=Entry(win,textvariable=text_input,width='25',font=('Times','18'))
    namev.pack()
    space=Label(win,text=' ',bg='black')
    space.pack()
    phone=Label(win,text='Enter Phone Number',bg='black',fg='white',width='40',font=('Arial Black','20'))
    phone.pack()
    space=Label(win,text=' ',bg='black')
    space.pack()
    num_input=StringVar()
    phonev=Entry(win,textvariable=num_input,width='25',font=('Times','18'))
    phonev.pack()
    space=Label(win,text=' ',bg='black')
    space.pack()

    def save_contact():
        if(namev.get()=='' or phonev.get()==''):
            messagebox.showwarning('warning','Enter the fields')
        elif((namev.get()>='0' and namev.get()<='9') or  (phonev.get().upper()>='A' and phonev.get().upper()<='Z')):
            messagebox.showerror('ERROR','Enter a Valid Contact')
        else:
            if((namev.get() in contact_list.keys()) or (phonev.get() in contact_list.values())):
                messagebox.showinfo('info','Already exists')
            else:
                contact_list.update({namev.get():phonev.get()})
                text_input.set('')
                num_input.set('')
        
    save=Button(win,text='SAVE',bg='blue',fg='white',width='10',padx=20,pady=10,font=('Times','16'),command=lambda : save_contact()).pack()


    
    
def block_contactss():
    win=Toplevel(root,bg='black')
    win.geometry('300x325')
    win.title("BLOCKED")
    win.resizable(width=False,height=False)
 
    if(blocked_list==[]):
        show=Label(win,text='Blocked list is empty',bg='black',font=('Calibri','16'),fg='white',width='40')
        show.pack()
    else:
        frame=Frame(win)
        frame.pack()
        li=Listbox(frame,width='30',height='10',bg='black',fg='white',font=('Calibri','16'),selectmode=SINGLE)
        sc=Scrollbar(frame,bg='black',command=li.yview)
        li.configure(yscrollcommand=sc.set)
        for y in blocked_list:
            li.insert(END,y)

        
        sc.pack(side=RIGHT,fill=Y)
        li.pack()
        def restore_contact():
            global l
            x=li.curselection()
            for i in x:
                if(li.get(i) not in restore):
                    restore.append(li.get(i))
                blocked_list.remove(li.get(i))
                li.delete(i)
                               

        res=Button(win,text='RESTORE',padx=20,pady=10,font=('Times','16'),bg='black',fg='white',command=lambda:restore_contact())
        res.pack()


        
            
    
welcome=tk.Label(root,text='         WELCOME TO CONTACT MANAGER      ',padx=10,bg='blue',font=('calibri',20),fg='white',height='2')
welcome.pack()
space=Label(root,text=' ',bg='black')
space.pack()
view=Button(root,text='        VIEW CONTACTS       ',bg='black',fg='white',padx=20,font=('calibri',15),command=lambda:view_contacts())
view.pack()
space=Label(root,text=' ',bg='black')
space.pack()
create=Button(root,text='       CREATE CONTACT      ',bg='black',padx=20,fg='white',font=('calibri',15),command=lambda:create_contact())
create.pack()
space=Label(root,text=' ',bg='black')
space.pack()
block=Button(root,text='          BLOCK LIST               ',bg='black',padx=20,fg='white',font=('calibri',15),command=lambda:block_contactss())
block.pack()


root.mainloop()


