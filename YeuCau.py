from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import json
import requests

class order:
    def __init__(self):
        self.root = Tk()
        self.obj4()

    def obj4(self):
        # frame1
        self.frame = LabelFrame(self.root, text= "",)
        self.frame.place(x= 50, y = 250)
        self.table4()
        self.my_tree.grid(row=1, columnspan=3)
        self.P_allData4()
        S_button = Button(self.frame, text="Tìm kiếm", command=self.Search_box4, padx=10, pady=5, bg ='#9898F5')
        S_button.grid(row=0, column=0)
        self.S_entry4 = Entry(self.frame, font=("default", 15))
        self.S_entry4.place(x=185, y=3)
        self.Search_box4()
        Label(self.root, text="").grid(row=1, column=0)

        # frame2
        self.frame2 = LabelFrame(self.root, text="", )
        self.frame2.place(x=50, y=550)

        #frame3
        Label(self.root, text="    ").grid(row=0, column=1)
        self.frame3 = LabelFrame(self.root, text="", )
        self.frame3.place(x = 850, y = 260)

        Label(self.frame3, text="MÃ DH", font=('default', 17)).grid(row=1, column=0)
        Label(self.frame3, text="NGÀY THÁNG", font=('default', 17)).grid(row=2, column=0)

        self.info1_4 = Entry(self.frame3, font=("default", 15))
        self.info1_4.grid(row=1, column=1)
        self. info2_4 = Entry(self.frame3, font=("default", 15))
        self. info2_4.grid(row=2, column=1)

        de_button = Button(self.frame3, text="Xóa", padx=20, pady=10, command=self.remove_data4, bg = '#EEEE95')
        de_button.grid(row=0, column=0)
        de_button["state"] = "disabled"

        up_button = Button(self.frame3, text="Cập Nhật", padx=20, pady=10, command=self.update_data4, bg = '#EEEE95')
        up_button.grid(row=0, column=1)
        up_button["state"] = "disabled"
        self.my_tree.bind("<Double-1>", self.Clicker4)

    def table4(self):
        self.my_tree = ttk.Treeview(self.frame)
        #Define Our Columns
        self.my_tree['column'] = ("id_Order", "id_emp", "date")

        #Formate Our Columns
        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("id_Order", anchor=CENTER, width=120)
        self.my_tree.column("id_emp", anchor=W, width=120)
        self.my_tree.column("date", anchor=W, width =200)

        #Create Headings
        self.my_tree.heading("#0", text = "", anchor=W)
        self.my_tree.heading("id_Order", text="MÃ ĐƠN HÀNG", anchor=CENTER)
        self.my_tree.heading("id_emp", text = "MÃ NV", anchor=W)
        self.my_tree.heading("date", text="NGÀY", anchor=W)

    def P_allData4(self):
        url = "https://apichicken.herokuapp.com/api/order/"
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

    def delete_my_tree4(self):
        for record in self.my_tree.get_children():
            self.my_tree.delete(record)

    def Search_box4(self):
        try:
            S_urls = "https://apichicken.herokuapp.com/api/order/{}".format(int(self.S_entry4.get()))
            S_response = requests.get(S_urls)
            S_data = S_response.json()
            self.S_entry4.delete(0, END)
            self.delete_my_tree4()
            self.S_datal = list(S_data.values())
            self.my_tree.insert(parent='', index='end', iid=0, text="", values=self.S_datal)
        except:
            if not self.S_entry4.get():
                self.delete_my_tree4()
                self.P_allData4()
            else:
                self.S_entry4.delete(0, END)
                messagebox.showerror("Lỗi", "Nhập vào là một số!")

    def remove_data4(self):
        id_lst = []
        if messagebox.askyesno("Thoát", " bạn có xóa không?") == True:
            for selected_item in self.my_tree.selection():
                item = self.my_tree.item(selected_item)
                id = item['values'][0]
                de_url = "https://apichicken.herokuapp.com/api/order/{}/".format(id)
                response = requests.delete(de_url)
                print(response.status_code)
                self.my_tree.delete(selected_item)

            x = self.my_tree.selection()
            for record in x:
                self.my_tree.delete(record)

            announce = messagebox.showinfo("Xóa thành công", "Xóa dữ liệu thành công")
        else:
            pass

    def Clicker4(self, e):
        self.select_record4()

    def select_record4(self):
        self.info1_4.delete(0, END)
        self.info2_4.delete(0, END)

        selected = self.my_tree.focus()
        values = self.my_tree.item(selected, 'values')

        self.info1_4.insert(0, values[1])
        self.info2_4.insert(0, values[2])

    def update_data4(self):
        selected = self.my_tree.focus()
        values = self.my_tree.item(selected, 'values')
        id = int(values[0])

        todo = {}
        todo["id_emp"] = self.info1_4.get()
        todo["date"] = self.info2_4.get()
        print(todo)
        up_url = "https://apichicken.herokuapp.com/api/order/{}/".format(id)
        response = requests.patch(up_url, json=todo)
        print(response.status_code)
        announce = messagebox.showinfo("Thành công", "Cập nhật dự liệu thành công")



if __name__ == "__main__":
    a = order()
    a.root.mainloop()