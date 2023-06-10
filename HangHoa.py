from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import json
import requests

class product:
    def __init__(self):
        self.root = Tk()
        self.root.title('Hàng hóa')
        self.root.geometry("1150x500")
        self.obj1()

    def obj1(self):
        # frame1
        self.frame = LabelFrame(self.root, text= "",)
        self.frame.place(x = 50, y = 250)
        self.table1()
        self.my_tree.grid(row=1, columnspan=3)
        self.P_allData1()
        S_button = Button(self.frame, text="Tìm kiếm", command=self.Search_box1, padx=10, pady=5, bg = '#9898F5')
        S_button.grid(row=0, column=0)
        self.S_entry1 = Entry(self.frame, font=("default", 15))
        self.S_entry1.place(x=185, y=3)
        self.Search_box1()
        Label(self.root, text="").grid(row=1, column=0)

        # frame2
        self.frame2 = LabelFrame(self.root, text="", )
        self.frame2.place(x = 50, y = 550)
        space = Label(self.frame2).grid(row=0, column=0)
        namehh_label = Label(self.frame2, text='Tên HH').grid(row=1, column=0)
        makho_label = Label(self.frame2, text='Mã kho').grid(row=1, column=1)
        gia_label = Label(self.frame2, text='Gía').grid(row=1, column=2)

        self.name_entry1 = Entry(self.frame2, font=("default", 10), width=30)
        self.name_entry1.grid(row=2, column=0)
        self.clicked1 = IntVar()
        options = self.lst_OpMenu1()
        self.clicked1.set('--Mã kho--')
        print(options)
        self.acc_entry1 = OptionMenu(self.frame2, self.clicked1, *options)
        print(self.clicked1)
        self.acc_entry1.grid(row=2, column=1)
        self.gia_entry1 = Entry(self.frame2, font=("default", 10), width=30)
        self.gia_entry1.grid(row=2, column=2)
        self.C_button1 = Button(self.frame2, text='Thêm hàng hóa', padx=20, pady=5, command=self.create_data1, bg = '#EEEE95')
        self.C_button1.grid(row=0, columnspan=3)

        #frame3
        Label(self.root, text="    ").grid(row=0, column=1)
        self.frame3 = LabelFrame(self.root, text="", )
        self.frame3.place(x = 850, y = 260)

        Label(self.frame3, text="Mã hàng hóa ", font=('default', 17)).grid(row=1, column=0)
        Label(self.frame3, text="Tên hàng hóa ", font=('default', 17)).grid(row=2, column=0)
        Label(self.frame3, text="Mã kho ", font=('default', 17)).grid(row=3, column=0)
        Label(self.frame3, text="Gía ", font=('default', 17)).grid(row=4, column=0)

        self.info1_1 = Entry(self.frame3, font=("default", 15))
        self.info1_1.grid(row=1, column=1)
        self. info2_1 = Entry(self.frame3, font=("default", 15))
        self. info2_1.grid(row=2, column=1)
        self. info3_1 = Entry(self.frame3, font=("default", 15))
        self.info3_1.grid(row=3, column=1)


        de_button = Button(self.frame3, text="Xóa", padx=20, pady=10, command=self.remove_data1, bg = '#EEEE95')
        de_button.grid(row=0, column=0)

        up_button = Button(self.frame3, text="Cập Nhật", padx=20, pady=10, command=self.update_data1, bg = '#EEEE95')
        up_button.grid(row=0, column=1)

        self.my_tree.bind("<Double-1>", self.Clicker1)

    def table1(self):
        self.my_tree = ttk.Treeview(self.frame)
        #Define Our Columns
        self.my_tree['column'] = ("id_product", "name", "id_category", "price")

        #Formate Our Columns
        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("id_product", anchor=CENTER, width=120)
        self.my_tree.column("name", anchor=W, width=120)
        self.my_tree.column("id_category", anchor=W, width =120)
        self.my_tree.column("price", anchor=W, width =120)

        #Create Headings
        self.my_tree.heading("#0", text = "", anchor=W)
        self.my_tree.heading("id_product", text="Mã HH", anchor=CENTER)
        self.my_tree.heading("name", text = "Tên HH", anchor=W)
        self.my_tree.heading("id_category", text="Mã kho", anchor=W)
        self.my_tree.heading("price", text = "Gía", anchor=CENTER)


    def P_allData1(self):
        url = "https://apichicken.herokuapp.com/api/product/"
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

    def delete_my_tree1(self):
        for record in self.my_tree.get_children():
            self.my_tree.delete(record)

    def Search_box1(self):
        try:
            S_urls = "https://apichicken.herokuapp.com/api/product/{}".format(int(self.S_entry1.get()))
            S_response = requests.get(S_urls)
            S_data = S_response.json()
            self.S_entry1.delete(0, END)
            self.delete_my_tree1()
            self.S_datal = list(S_data.values())
            self.my_tree.insert(parent='', index='end', iid=0, text="", values=self.S_datal)
        except:
            if not self.S_entry1.get():
                self.delete_my_tree1()
                self.P_allData1()
            else:
                self.S_entry1.delete(0, END)
                messagebox.showerror("Lỗi", "Nhập vào là một số!")

    def lst_OpMenu1(self):
        url= "https://apichicken.herokuapp.com/api/category/"
        response = requests.get(url)
        data = response.json()
        lst_id = []
        for i in data:
            lst_id.append(i['id_category'])

        print(lst_id)
        return lst_id

    def create_data1(self):
        data = dict.fromkeys(['name', 'id_category', 'price'], 0)
        try:
            get_gia = int(self.gia_entry1.get())
        except:
            announce = messagebox.showerror("Lỗi", "Gía phải là số nguyên")
        else:
            entr_lst = [ self.name_entry1.get(), self.clicked1.get(), self.gia_entry1.get()]
            print(entr_lst)
            i = 0
            for k in data.keys():
                data[k] = entr_lst[i]
                i += 1
            U_urls = "https://apichicken.herokuapp.com/api/product/"
            S_response = requests.post(U_urls, json=data)
            data_test = S_response.json()
            announce = messagebox.showinfo("Thành công", "Dữ liệu đã được ghi")
            print(data_test)

            self.name_entry.delete(0, END)
            self.gia_entry.delete(0, END)

    def remove_data1(self):
        id_lst = []
        if messagebox.askyesno("Thoát", " bạn có xóa không?") == True:

            for selected_item in self.my_tree.selection():
                item = self.my_tree.item(selected_item)
                id = item['values'][0]
                de_url = "https://apichicken.herokuapp.com/api/product/{}/".format(id)
                response = requests.delete(de_url)
                print(response.status_code)
                self.my_tree.delete(selected_item)

            x = self.my_tree.selection()
            for record in x:
                self.my_tree.delete(record)

            announce = messagebox.showinfo("Xóa thành công", "Xóa dữ liệu thành công")
        else:
            pass

    def select_record1(self):
        self.info1_1.delete(0, END)
        self.info2_1.delete(0, END)
        self.info3_1.delete(0, END)

        selected = self.my_tree.focus()
        values = self.my_tree.item(selected, 'values')

        self.info1_1.insert(0, values[1])
        self.info2_1.insert(0, values[2])
        self.info3_1.insert(0, values[3])


    def Clicker1(self, e):
        self.select_record1()

    def update_data1(self):
        selected = self.my_tree.focus()
        values = self.my_tree.item(selected, 'values')
        id = int(values[0])

        todo = {}
        todo["name"] = self.info1_1.get()
        todo["id_category"] = self.info2_1.get()
        todo["price"] = self.info3_1.get()

        print(todo)
        up_url = "https://apichicken.herokuapp.com/api/product/{}/".format(id)
        response = requests.patch(up_url, json=todo)
        print(response.status_code)
        announce = messagebox.showinfo("Thành công", "Cập nhật dự liệu thành công")



if __name__ == "__main__":
    a = product()
    a.root.mainloop()