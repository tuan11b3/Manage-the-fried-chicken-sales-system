from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import json
import requests

class category:
    def __init__(self):

        self.root = Tk()
        self.obj2()

    def obj2(self):
        # frame1
        self.frame = LabelFrame(self.root, text= "",)
        self.frame.place(x= 50, y = 250)
        self.table2()
        self.my_tree.grid(row=1, columnspan=3)
        self.P_allData2()
        S_button = Button(self.frame, text="Tìm kiếm", command=self.Search_box2, padx=10, pady=5, bg = '#9898F5')
        S_button.grid(row=0, column=0)
        self.S_entry2 = Entry(self.frame, font=("default", 15))
        self.S_entry2.place(x=185, y=3)
        self.Search_box2()
        Label(self.root, text="").grid(row=1, column=0)

        # frame2
        self.frame2 = LabelFrame(self.root, text="", )
        self.frame2.place(x=50, y=550)
        space = Label(self.frame2, text = " ").grid(row=1, column=0)
        ln_label = Label(self.frame2, text='TÊN LOẠI').grid(row=2, column=0)

        self.cateName_entry = Entry(self.frame2, font=("default", 10), width=30)
        self.cateName_entry.grid(row=3, column=0)
        self.C_button2 = Button(self.frame2, text='Thêm loại', padx=20, pady=5, command=self.create_data2, bg = '#EEEE95')
        self.C_button2.grid(row=0, columnspan=3)

        #frame3
        Label(self.root, text="    ").grid(row=0, column=1)
        self.frame3 = LabelFrame(self.root, text="", )
        self.frame3.place(x = 850, y = 260)

        Label(self.frame3, text="TÊN LOẠI", font=('default', 17)).grid(row=1, column=0)

        self.info1_2 = Entry(self.frame3, font=("default", 15))
        self.info1_2.grid(row=1, column=1)

        de_button = Button(self.frame3, text="Xóa", padx=20, pady=10, command=self.remove_data2, bg = '#EEEE95')
        de_button.grid(row=0, column=0)
        de_button["state"] = "disabled"

        up_button = Button(self.frame3, text="Cập Nhật", padx=20, pady=10, command=self.update_data2, bg = '#EEEE95')
        up_button.grid(row=0, column=1)

        self.my_tree.bind("<Double-1>", self.Clicker2)

    def table2(self):
        self.my_tree = ttk.Treeview(self.frame)
        #Define Our Columns
        self.my_tree['column'] = ("id_category", "name_category")

        #Formate Our Columns
        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("id_category", anchor=CENTER, width=120)
        self.my_tree.column("name_category", anchor=CENTER, width=350)

        #Create Headings
        self.my_tree.heading("#0", text = "", anchor=W)
        self.my_tree.heading("id_category", text="MÃ KHO", anchor=CENTER)
        self.my_tree.heading("name_category", text = "TÊN LOẠI", anchor=W)


    def P_allData2(self):
        url = "https://apichicken.herokuapp.com/api/category/"
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

    def delete_my_tree2(self):
        for record in self.my_tree.get_children():
            self.my_tree.delete(record)

    def Search_box2(self):
        try:
            S_urls = "https://apichicken.herokuapp.com/api/category/{}".format(int(self.S_entry2.get()))
            S_response = requests.get(S_urls)
            S_data = S_response.json()
            print(S_data)
            self.S_entry2.delete(0, END)
            self.delete_my_tree2()
            self.S_datal = list(S_data.values())
            self.my_tree.insert(parent='', index='end', iid=0, text="", values=self.S_datal)
        except:
            if not self.S_entry2.get():
                self.delete_my_tree2()
                self.P_allData2()
            else:
                self.S_entry2.delete(0, END)
                messagebox.showerror("Lỗi", "Nhập vào là một số!")

    def create_data2(self):
        data = dict.fromkeys(['name_category'], 0)

        entr_lst = [self.cateName_entry.get()]
        print(entr_lst)
        i = 0
        for k in data.keys():
            data[k] = entr_lst[i]
            i += 1
        U_urls = "https://apichicken.herokuapp.com/api/category/"
        S_response = requests.post(U_urls, json=data)
        data_test = S_response.json()
        announce = messagebox.showinfo("Thành công", "Dữ liệu đã được ghi")
        print(data_test)

        self.cateName_entry.delete(0, END)


    def remove_data2(self):
        id_lst = []
        if messagebox.askyesno("Thoát", " bạn có xóa không?") == True:
            for selected_item in self.my_tree.selection():
                item = self.my_tree.item(selected_item)
                id = item['values'][0]
                de_url = "https://apichicken.herokuapp.com/api/category/".format(id)
                response = requests.delete(de_url)
                print(response.status_code)
                print(response.json())
                self.my_tree.delete(selected_item)

            x = self.my_tree.selection()
            for record in x:
                self.my_tree.delete(record)

            announce = messagebox.showinfo("Xóa thành công", "Xóa dữ liệu thành công")
        else:
            pass

    def select_record2(self):
        self.info1_2.delete(0, END)
        selected = self.my_tree.focus()
        values = self.my_tree.item(selected, 'values')
        self.info1_2.insert(0, values[1])

    def Clicker2(self, e):
        self.select_record2()

    def update_data2(self):
        selected = self.my_tree.focus()
        values = self.my_tree.item(selected, 'values')
        id = int(values[0])

        todo = {}
        todo["name_category"] = self.info1_2.get()
        print(todo)
        up_url = "https://apichicken.herokuapp.com/api/category/{}/".format(id)
        response = requests.patch(up_url, json=todo)
        print(response.status_code)
        announce = messagebox.showinfo("Thành công", "Cập nhật dự liệu thành công")



if __name__ == "__main__":
    a = category()
    a.root.mainloop()