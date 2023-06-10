from NhanVien import emp
from tkinter import *
from tkinter import messagebox
from HangHoa import product
from tkinter import ttk
from Loai import category
from TaiKhoan import account
from DangNhap import Login
from YeuCau import order

class Main(emp, product, category, account, Login, order):
    def __init__(self):
        # self.w = Login()
        # self.w.loginw.mainloop()
        # self.w.loginw.destroy()
        self.root = Tk()
        self.root.title("Hệ Thống Bán Gà Rán")
        width = 1240
        height = 750
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.root.resizable(0, 0)
        self.root.protocol('WM_DELETE_WINDOW', self.__Main_del__)
        self.buildmain()
        super(emp).__init__()
        self.obj()
        '''pd_button = Button(self.root, text = " PRODUCT", command = self.product_Table)
        pd_button.place(x = 50, y = 200)'''

    def __Main_del__(self):
        if messagebox.askyesno("Thoát", " bạn có muốn thoát?") == True:
            self.root.quit()
            exit(0)
        else:
            pass

    def buildmain(self):
        self.topframe = LabelFrame(self.root, width=1400, height=120, bg="skyblue")
        self.topframe.place(x=0, y=0)
        self.store_name = 'Hệ thống'
        self.storelable = Label(self.topframe, text=self.store_name + " bán và quản lý gà rán", bg="#FF3030",
                                anchor="center")
        self.storelable.config(font="Roboto 30 bold", fg="snow")
        self.storelable.place(x=360, y=30)
        mi = PhotoImage(file="images/myprofile.png")
        mi = mi.subsample(4, 4)
        # self.myprofile = ttk.Label(self.topframe, text=self.w.username.get(), image=mi, compound=TOP)
        # self.myprofile.image = mi
        # self.myprofile.place(x=1043, y=15)

        #Button
        a = 8
        b = 8
        self.mainframe = LabelFrame(self.root, width=1150, height=120, bg="#f7f7f7")
        self.mainframe.place(x=50, y=120)
        mi = PhotoImage(file="images/items.png")
        mi = mi.subsample(a, b)
        self.items = Button(self.mainframe, text="Hàng hóa", bd=5, image=mi, font="roboto 11 bold", compound=TOP,
                            command=self.product_Table)
        self.items.image = mi
        self.items.place(x=30, y=10)
        mi = PhotoImage(file="images/inventory.png")
        mi = mi.subsample(a, b)
        self.stocks = Button(self.mainframe, text="Loai", bd=5, image=mi, font="roboto 11 bold", compound=TOP,
                             command=self.category_Table)
        self.stocks.image = mi
        self.stocks.place(x=211, y=10)

        mi = PhotoImage(file="images/accounts.png")
        mi = mi.subsample(a, b)
        self.acc = Button(self.mainframe, text="Tai khoản", bd=5, image=mi, font="roboto 11 bold", compound=TOP,
                             command=self.account_Table)
        self.acc.image = mi
        self.acc.place(x=392, y=10)

        mi = PhotoImage(file="images/Contacts_512.png")
        mi = mi.subsample(a, b)
        self.changeuser = Button(self.mainframe, text="Nhân viên", bd=5, font="roboto 11 bold", image=mi, compound=TOP
                                 , command=self.employee_Table)
        self.changeuser.image = mi
        self.changeuser.place(x=573, y=10)

        mi = PhotoImage(file="images/Invoice2.png")
        mi = mi.subsample(a, b)
        self.orderImg = Button(self.mainframe, text="Đơn hàng", bd=5, font="roboto 11 bold", image=mi, compound=TOP
                                 , command=self.order_Table)
        self.orderImg.image = mi
        self.orderImg.place(x=754, y=10)

        mi = PhotoImage(file="images/Door_Out-512.png")
        mi = mi.subsample(a, b)
        self.logout = Button(self.mainframe, text="Quit", bd=5, font="roboto 11 bold", image=mi, compound=TOP
                             , command = self.__Main_del__)
        self.logout.image = mi
        self.logout.place(x=935, y=10)

    def clear_frames(self):
        self.delete_my_tree()
        self.my_tree.grid_remove()
        self.my_tree.destroy()

        self.frame.grid_forget()
        self.frame2.grid_forget()
        self.frame3.grid_forget()
        self.frame.destroy()
        self.frame2.destroy()
        self.frame3.destroy()

    def product_Table(self):
        self.clear_frames()
        self.obj1()

    def employee_Table(self):
        self.clear_frames()
        self.obj()

    def category_Table(self):
        self.clear_frames()
        self.obj2()

    def account_Table(self):
        self.clear_frames()
        self.obj3()

    def order_Table(self):
        self.clear_frames()
        self.obj4()

if __name__ == '__main__':
    w = Main()
    w.root.mainloop()