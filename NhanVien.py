from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import json
import requests

class emp:
    def __init__(self):
        self.root = Tk()
        self.obj()

    def obj(self):
        # frame1
        self.frame = LabelFrame(self.root, text= "",)
        self.frame.place(x= 50, y = 250)
        self.table()
        self.my_tree.grid(row=1, columnspan=3)
        self.P_allData()
        S_button = Button(self.frame, text="Tìm kiếm", command=self.Search_box, padx=10, pady=5, bg ='#9898F5')
        S_button.grid(row=0, column=0)
        self.S_entry = Entry(self.frame, font=("default", 15))
        self.S_entry.place(x=185, y=3)
        self.Search_box()
        Label(self.root, text="").grid(row=1, column=0)

        # frame2
        self.frame2 = LabelFrame(self.root, text="", )
        self.frame2.place(x=50, y=550)
        space = Label(self.frame2).grid(row=1, column=0)
        ln_label = Label(self.frame2, text='Last name').grid(row=2, column=0)
        fn_label = Label(self.frame2, text='First name').grid(row=2, column=1)
        email_label = Label(self.frame2, text='EMAIL').grid(row=2, column=2)
        space = Label(self.frame2).grid(row=4, column=0)
        date_label = Label(self.frame2, text='Date').grid(row=5, column=0)
        sdt_label = Label(self.frame2, text='SDT').grid(row=5, column=1)
        add_label = Label(self.frame2, text='Dia chi').grid(row=5, column=2)

        self.ln_entry = Entry(self.frame2, font=("default", 10), width=30)
        self.ln_entry.grid(row=3, column=0)
        self.fn_entry = Entry(self.frame2, font=("default", 10), width=30)
        self.fn_entry.grid(row=3, column=1)
        self.email_entry = Entry(self.frame2, font=("default", 10), width=30)
        self.email_entry.grid(row=3, column=2)
        self.date_entry = Entry(self.frame2, font=("default", 10), width=30)
        self.date_entry.grid(row=6, column=0)
        self.sdt_entry = Entry(self.frame2, font=("default", 10), width=30)
        self.sdt_entry.grid(row=6, column=1)
        self.add_entry = Entry(self.frame2, font=("default", 10), width=30)
        self.add_entry.grid(row=6, column=2)
        self.C_button = Button(self.frame2, text='Thêm nhân viên', padx=20, pady=5, command=self.create_data, bg = '#EEEE95')
        self.C_button.grid(row=0, columnspan=3)

        #frame3
        Label(self.root, text="    ").grid(row=0, column=1)
        self.frame3 = LabelFrame(self.root, text="", )
        self.frame3.place(x = 850, y = 260)

        Label(self.frame3, text="HỌ ", font=('default', 17)).grid(row=1, column=0)
        Label(self.frame3, text="TÊN ", font=('default', 17)).grid(row=2, column=0)
        Label(self.frame3, text="GIỚI TÍNH", font=('default', 17)).grid(row=3, column=0)
        Label(self.frame3, text="NGÀY THÁNG", font=('default', 17)).grid(row=4, column=0)
        Label(self.frame3, text="SDT ", font=('default', 17)).grid(row=5, column=0)
        Label(self.frame3, text="ĐỊA CHỈ", font=('default', 17)).grid(row=6, column=0)

        self.info1 = Entry(self.frame3, font=("default", 15))
        self.info1.grid(row=1, column=1)
        self. info2 = Entry(self.frame3, font=("default", 15))
        self. info2.grid(row=2, column=1)
        self. info3 = Entry(self.frame3, font=("default", 15))
        self.info3.grid(row=3, column=1)
        self.info4 = Entry(self.frame3, font=("default", 15))
        self.info4.grid(row=4, column=1)
        self.info5 = Entry(self.frame3, font=("default", 15))
        self. info5.grid(row=5, column=1)
        self.info6 = Entry(self.frame3, font=("default", 15))
        self.info6.grid(row=6, column=1)


        de_button = Button(self.frame3, text="Xóa", padx=20, pady=10, command=self.remove_data, bg = '#EEEE95')
        de_button.grid(row=0, column=0)

        up_button = Button(self.frame3, text="Cập Nhật", padx=20, pady=10, command=self.update_data, bg = '#EEEE95')
        up_button.grid(row=0, column=1)

        self.my_tree.bind("<Double-1>", self.Clicker)

    def table(self):
        self.my_tree = ttk.Treeview(self.frame)
        #Define Our Columns
        self.my_tree['column'] = ("id", "l_name", "f_name", 'gender', 'date', 'numberPhone')

        #Formate Our Columns
        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("id", anchor=CENTER, width=120)
        self.my_tree.column("l_name", anchor=W, width=120)
        self.my_tree.column("f_name", anchor=W, width =120)
        self.my_tree.column("gender", anchor=W, width =120)
        self.my_tree.column("date", anchor=W, width =120)
        self.my_tree.column("numberPhone", anchor=W, width =120)


        #Create Headings
        self.my_tree.heading("#0", text = "", anchor=W)
        self.my_tree.heading("id", text="MÃ NV", anchor=CENTER)
        self.my_tree.heading("l_name", text = "HỌ", anchor=W)
        self.my_tree.heading("f_name", text="TÊN", anchor=W)
        self.my_tree.heading("gender", text = "GIỚI TÍNH", anchor=CENTER)
        self.my_tree.heading("date", text = "NGÀY THÁNG", anchor=CENTER)
        self.my_tree.heading("numberPhone", text = "SDT", anchor=CENTER)



    def P_allData(self):
        url = "https://apichicken.herokuapp.com/api/emp/"
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

    def delete_my_tree(self):
        for record in self.my_tree.get_children():
            self.my_tree.delete(record)

    def Search_box(self):
        try:
            S_urls = "https://apichicken.herokuapp.com/api/emp/{}".format(int(self.S_entry.get()))
            S_response = requests.get(S_urls)
            S_data = S_response.json()
            self.S_entry.delete(0, END)
            self.delete_my_tree()
            self.S_datal = list(S_data.values())
            self.my_tree.insert(parent='', index='end', iid=0, text="", values=self.S_datal)
        except:
            if not self.S_entry.get():
                self.delete_my_tree()
                self.P_allData()
            else:
                self.S_entry.delete(0, END)
                messagebox.showerror("Lỗi", "Nhập vào là một số!")

    def create_data(self):
        data = dict.fromkeys(['l_name', 'f_name', 'email', 'date', 'numberPhone', 'address'], 0)
        try:
            dtime_var = datetime.strptime(self.date_entry.get(), '%Y-%m-%d')
        except:
            announce = messagebox.showerror("Lỗi", "date yyyy-mm-dd\n EX: 2022-11-09")
        else:
            entr_lst = [self.ln_entry.get(), self.fn_entry.get(), self.email_entry.get(), self.date_entry.get(), self.sdt_entry.get(),
                        self.add_entry.get()]
            print(entr_lst)
            i = 0
            for k in data.keys():
                data[k] = entr_lst[i]
                i += 1
            U_urls = "https://apichicken.herokuapp.com/api/emp/"
            S_response = requests.post(U_urls, json=data)
            data_test = S_response.json()
            announce = messagebox.showinfo("Thành công", "Dữ liệu đã được ghi")
            print(data_test)

            self.ln_entry.delete(0, END)
            self.fn_entry.delete(0, END)
            self.email_entry.delete(0, END)
            self.date_entry.delete(0, END)
            self.sdt_entry.delete(0, END)
            self.add_entry.delete(0, END)

    def remove_data(self):
        id_lst = []
        if messagebox.askyesno("Thoát", " bạn có xóa không?") == True:
            for selected_item in self.my_tree.selection():
                item = self.my_tree.item(selected_item)
                id = item['values'][0]
                de_url = "https://apichicken.herokuapp.com/api/emp/{}/".format(id)
                response = requests.delete(de_url)
                print(response.status_code)
                self.my_tree.delete(selected_item)

            x = self.my_tree.selection()
            for record in x:
                self.my_tree.delete(record)

            announce = messagebox.showinfo("Xóa thành công", "Xóa dữ liệu thành công")
        else:
            pass

    def Clicker(self, e):
        self.select_record()

    def select_record(self):
        self.info1.delete(0, END)
        self.info2.delete(0, END)
        self.info3.delete(0, END)
        self.info4.delete(0, END)
        self.info5.delete(0, END)
        self.info6.delete(0, END)

        selected = self.my_tree.focus()
        values = self.my_tree.item(selected, 'values')

        self.info1.insert(0, values[1])
        self.info2.insert(0, values[2])
        self.info3.insert(0, values[3])
        self.info4.insert(0, values[4])
        self.info5.insert(0, values[5])
        self.info6.insert(0, values[6])


    def update_data(self):
        selected = self.my_tree.focus()
        values = self.my_tree.item(selected, 'values')
        id = int(values[0])

        todo = {}
        todo["l_name"] = self.info1.get()
        todo["f_name"] = self.info2.get()
        todo["gender"] = self.info3.get()
        todo["date"] = self.info4.get()
        todo["sdt"] = self.info5.get()
        todo["address"] = self.info6.get()
        print(todo)
        up_url = "https://apichicken.herokuapp.com/api/emp/{}/".format(id)
        response = requests.patch(up_url, json=todo)
        print(response.status_code)
        announce = messagebox.showinfo("Thành công", "Cập nhật dự liệu thành công")



if __name__ == "__main__":
    a = emp()
    a.root.mainloop()