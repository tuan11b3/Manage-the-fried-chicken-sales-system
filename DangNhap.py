from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import requests

# from main import Main
import json


# LOGIN CLASS
class Login:

    def __init__(self):
        self.loginw=Tk()
        self.loginw.title("ĐĂNG NHẬP")
        width = 500
        height = 600
        screen_width = self.loginw.winfo_screenwidth()
        screen_height = self.loginw.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.loginw.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.loginw.resizable(0, 0)
        self.loginw.protocol('WM_DELETE_WINDOW', self.__login_del__)
        self.loginw.config(bg="#FF3030")
        self.username = StringVar(value="Tên đăng nhập")
        self.password = StringVar(value="Mật khẩu")
        self.obj()

    def __login_del__(self):
        if messagebox.askyesno("Thoát", " Thoát hệ thống?") == True:
            self.loginw.destroy()
            exit(0)                   # FORCE SYSTEM TO EXIT

    # WIDGET FUNCTION
    def obj(self):
        self.loginframe=LabelFrame(self.loginw,bg="#FF3030",height=400,width=300)
        self.loginw.bind('<Return>',self.checkuser)
        self.loginframe.place(x=103,y=95)
        self.toplabel = Label(self.loginframe, fg="white", bg="#FF3030", anchor="center", text="Login", font="Roboto 40 bold")
        self.toplabel.place(x=75,y=25)
        self.us = ttk.Entry(self.loginframe, width=20, textvariable=self.username,font="Roboto 14 ")
        self.us.place(x=35,y=145,height=40)
        self.pa = ttk.Entry(self.loginframe, width=20, textvariable=self.password,font="Roboto 14 ")
        self.pa.place(x=35,y=185,height=40)
        self.us.bind('<Button-1>', self.onclick)
        self.pa.bind('<Button-1>', self.onclick1)
        self.signin = Button(self.loginframe,width=20, text="Đăng nhập",bg="lightblue2",fg="dimgray",command=self.checkuser,font="Roboto 14")
        self.signin.place(x=35,y=290)
     #  self.register = Button(self.loginframe,width=20, text = "Register",bg="lightblue2",fg="dimgray",command = self.reguser,font="Roboto")
     #   self.register.place(x=35,y=320)

    # CHECK USER IN DATABASE
    def checkuser(self,event=0):
        todo = dict.fromkeys(['username', 'password'], 0)
        todo['username'] = self.username.get()
        todo['password'] = self.password.get()

        chUser_Url = "https://apichicken.herokuapp.com/api/login/"
        response = requests.post(chUser_Url, todo)
        data = response.json()
        condition = list(data.keys())
        print(condition)
        if 'non_field_errors' not in condition :
            self.success()
        else:
            self.fail()

    # LOGIN SUCCESS
    def success(self):
       # messagebox.showinfo("Success","Login successful")
        self.loginw.quit()

        # w = Main()
        # w.root.mainloop()

    # LOGIN FAILURE
    def fail(self):
        messagebox.showerror("Lỗi","Tên dăng nhập hoặc mật khẩu không đúng")

    # ONCLICK EVENTS
    def onclick(self,event):
        if (self.username.get() == "Tên đăng nhập"):
            self.us.delete(0, "end")

    def onclick1(self,event):
        if (self.password.get() == "Mật khẩu"):
            self.pa.delete(0, "end")
            self.pa.config(show = "*")
if __name__ == "__main__":
    w=Login()
    w.loginw.mainloop()

