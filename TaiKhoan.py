from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import json
import requests

class account:
    def __init__(self, root):
        self.root = root
        self.obj3()

    def obj3(self):
        # frame1
        self.frame = LabelFrame(self.root, text= "",)
        self.frame.place(x= 50, y = 250)
        self.table3()
        self.my_tree.grid(row=1, columnspan=3)
        self.P_allData3()
        S_button = Button(self.frame, text="Tìm kiếm", command=self.Search_box3, padx=10, pady=5, bg = '#9898F5')
        S_button.grid(row=0, column=0)
        self.S_entry3 = Entry(self.frame, font=("default", 15))
        self.S_entry3.place(x=185, y=3)
        self.Search_box3()
        Label(self.root, text="").grid(row=1, column=0)

        self.frame2 = LabelFrame(self.root, text="", )
        self.frame2.place(x=50, y=550)

        self.frame3 = LabelFrame(self.root, text="", )
        self.frame3.place(x=850, y=260)

    def table3(self):
        self.my_tree = ttk.Treeview(self.frame)
        #Define Our Columns
        self.my_tree['column'] = ("id_account", "name_account", "password", "id_per")

        #Formate Our Columns
        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("id_account", anchor=CENTER, width=120)
        self.my_tree.column("name_account", anchor=W, width=120)
        self.my_tree.column("password", anchor=W, width =120)
        self.my_tree.column("id_per", anchor=W, width =120)

        #Create Headings
        self.my_tree.heading("#0", text = "", anchor=W)
        self.my_tree.heading("id_account", text="MÃ TÀI KHOẢN", anchor=CENTER)
        self.my_tree.heading("name_account", text = "TÊN TÀI KHOẢN", anchor=W)
        self.my_tree.heading("password", text="MẬT KHẨU", anchor=W)
        self.my_tree.heading("id_per", text = "MÃ QUYỀN", anchor=CENTER)




    def P_allData3(self):
        url = "https://apichicken.herokuapp.com/api/account/"
        response = requests.get(url)
        data = response.json()
        my_list = []
        my_dict = {}
        for j in range(len(data)):
            my_dict = data[j]
            temp_list = []
            for i in my_dict.values():
                temp_list.append(i)

            my_list.append(temp_list)

        for i in range(len(data)):
            self.my_tree.insert(parent='', index='end', iid=i, text="", values=my_list[i])

    def delete_my_tree3(self):
        for record in self.my_tree.get_children():
            self.my_tree.delete(record)

    def Search_box3(self):
        try:
            S_urls = "https://apichicken.herokuapp.com/api/account/{}".format(int(self.S_entry3.get()))
            S_response = requests.get(S_urls)
            S_data = S_response.json()
            self.S_entry3.delete(0, END)
            self.delete_my_tree3()
            self.S_datal = list(S_data.values())
            self.my_tree.insert(parent='', index='end', iid=0, text="", values=self.S_datal)
        except:
            if not self.S_entry3.get():
                self.delete_my_tree3()
                self.P_allData3()
            else:
                self.S_entry3.delete(0, END)
                messagebox.showerror("Lỗi", "Nhập vào là một số!")

if __name__ == "__main__":
    a = account()
    a.root.mainloop()