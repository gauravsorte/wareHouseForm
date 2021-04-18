#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#    Jan 02, 2021 04:46:30 PM IST  platform: Windows NT

import sys
import mysql.connector
from tkinter import messagebox



try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import WareHouseForm_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    WareHouseForm_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    WareHouseForm_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Times New Roman} -size 15 -weight bold"
        font11 = "-family {Times New Roman} -size 13 -weight bold"
        font12 = "-family {Times New Roman} -size 12 -weight bold"
        font9 = "-family {Times New Roman} -size 24 -weight bold"

        top.geometry("699x525+323+142")

        windowWidth = 699 #root.winfo_reqwidth()
        windowHeight = 525 #root.winfo_reqheight()
        print("Width", windowWidth, "Height", windowHeight)

        # Gets both half the screen width/height and window width/height
        positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
        positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

        # Positions the window in the center of the page.
        root.geometry("+{}+{}".format(positionRight, positionDown))

        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1, 1)
        top.title("VowTech")
        top.configure(background="#d9d9d9")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.029, rely=0.019, relheight=0.162
                , relwidth=0.937)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.015, rely=0.129, height=59, width=634)
        self.Label1.configure(background="#000000")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''Warehouse Inventory System''')

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.029, rely=0.21, relheight=0.524, relwidth=0.465)

        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#80ffff")

        self.Label2 = tk.Label(self.Frame2)
        self.Label2.place(relx=0.003, rely=0.036, height=31, width=168)
        self.Label2.configure(background="#80ffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#ff0000")
        self.Label2.configure(text='''Product Widget''')

        self.Label3 = tk.Label(self.Frame2)
        self.Label3.place(relx=0.049, rely=0.182, height=21, width=98)
        self.Label3.configure(background="#80ffff")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font11)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Product ID :''')

        self.Entry1 = tk.Entry(self.Frame2)
        self.Entry1.place(relx=0.517, rely=0.171,height=30, relwidth=0.474)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Label3_1 = tk.Label(self.Frame2)
        self.Label3_1.place(relx=0.034, rely=0.327, height=21, width=126)
        self.Label3_1.configure(activebackground="#f9f9f9")
        self.Label3_1.configure(activeforeground="black")
        self.Label3_1.configure(background="#80ffff")
        self.Label3_1.configure(disabledforeground="#a3a3a3")
        self.Label3_1.configure(font="-family {Times New Roman} -size 13 -weight bold -slant roman -underline 0 -overstrike 0")
        self.Label3_1.configure(foreground="#000000")
        self.Label3_1.configure(highlightbackground="#d9d9d9")
        self.Label3_1.configure(highlightcolor="black")
        self.Label3_1.configure(text='''Product Name:''')

        self.Entry2 = tk.Entry(self.Frame2)
        self.Entry2.place(relx=0.517, rely=0.32,height=30, relwidth=0.474)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="blue")
        self.Entry2.configure(selectforeground="white")

        self.Label3_2 = tk.Label(self.Frame2)
        self.Label3_2.place(relx=0.031, rely=0.487, height=21, width=126)
        self.Label3_2.configure(activebackground="#f9f9f9")
        self.Label3_2.configure(activeforeground="black")
        self.Label3_2.configure(background="#80ffff")
        self.Label3_2.configure(disabledforeground="#a3a3a3")
        self.Label3_2.configure(font="-family {Times New Roman} -size 13 -weight bold -slant roman -underline 0 -overstrike 0")
        self.Label3_2.configure(foreground="#000000")
        self.Label3_2.configure(highlightbackground="#d9d9d9")
        self.Label3_2.configure(highlightcolor="black")
        self.Label3_2.configure(text='''Product Price:''')

        self.Entry3 = tk.Entry(self.Frame2)
        self.Entry3.place(relx=0.514, rely=0.476,height=30, relwidth=0.474)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(selectbackground="blue")
        self.Entry3.configure(selectforeground="white")

        self.Label3_2 = tk.Label(self.Frame2)
        self.Label3_2.place(relx=0.034, rely=0.655, height=21, width=147)
        self.Label3_2.configure(activebackground="#f9f9f9")
        self.Label3_2.configure(activeforeground="black")
        self.Label3_2.configure(background="#80ffff")
        self.Label3_2.configure(disabledforeground="#a3a3a3")
        self.Label3_2.configure(font="-family {Times New Roman} -size 13 -weight bold -slant roman -underline 0 -overstrike 0")
        self.Label3_2.configure(foreground="#000000")
        self.Label3_2.configure(highlightbackground="#d9d9d9")
        self.Label3_2.configure(highlightcolor="black")
        self.Label3_2.configure(text='''Product Company:''')

        self.Entry4 = tk.Entry(self.Frame2)
        self.Entry4.place(relx=0.511, rely=0.64,height=30, relwidth=0.474)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(highlightbackground="#d9d9d9")
        self.Entry4.configure(highlightcolor="black")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(selectbackground="blue")
        self.Entry4.configure(selectforeground="white")

        self.Label3_3 = tk.Label(self.Frame2)
        self.Label3_3.place(relx=0.031, rely=0.836, height=21, width=127)
        self.Label3_3.configure(activebackground="#f9f9f9")
        self.Label3_3.configure(activeforeground="black")
        self.Label3_3.configure(background="#80ffff")
        self.Label3_3.configure(disabledforeground="#a3a3a3")
        self.Label3_3.configure(font="-family {Times New Roman} -size 13 -weight bold -slant roman -underline 0 -overstrike 0")
        self.Label3_3.configure(foreground="#000000")
        self.Label3_3.configure(highlightbackground="#d9d9d9")
        self.Label3_3.configure(highlightcolor="black")
        self.Label3_3.configure(text='''Phone Number:''')

        self.Entry5 = tk.Entry(self.Frame2)
        self.Entry5.place(relx=0.508, rely=0.811,height=30, relwidth=0.474)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(highlightbackground="#d9d9d9")
        self.Entry5.configure(highlightcolor="black")
        self.Entry5.configure(insertbackground="black")
        self.Entry5.configure(selectbackground="blue")
        self.Entry5.configure(selectforeground="white")

        self.Frame3 = tk.Frame(top)
        self.Frame3.place(relx=0.501, rely=0.21, relheight=0.524, relwidth=0.465)

        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#80ffff")

        self.Label2_6 = tk.Label(self.Frame3)
        self.Label2_6.place(relx=0.009, rely=0.036, height=31, width=168)
        self.Label2_6.configure(activebackground="#f9f9f9")
        self.Label2_6.configure(activeforeground="black")
        self.Label2_6.configure(background="#80ffff")
        self.Label2_6.configure(disabledforeground="#a3a3a3")
        self.Label2_6.configure(font="-family {Times New Roman} -size 15 -weight bold -slant roman -underline 0 -overstrike 0")
        self.Label2_6.configure(foreground="#ff0000")
        self.Label2_6.configure(highlightbackground="#d9d9d9")
        self.Label2_6.configure(highlightcolor="black")
        self.Label2_6.configure(text='''Product Widget''')

        self.Listbox1 = tk.Listbox(self.Frame3)
        self.Listbox1.place(relx=0.062, rely=0.145, relheight=0.771
                , relwidth=0.905)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")

        self.Frame4 = tk.Frame(top)
        self.Frame4.place(relx=0.029, rely=0.781, relheight=0.162
                , relwidth=0.937)
        self.Frame4.configure(relief='groove')
        self.Frame4.configure(borderwidth="2")
        self.Frame4.configure(relief="groove")
        self.Frame4.configure(background="#80ffff")

        self.Button1 = tk.Button(self.Frame4)
        self.Button1.place(relx=0.031, rely=0.353, height=31, width=55)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font12)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''SAVE''')
        self.Button1.configure(command=self.savedata)

        self.Button2 = tk.Button(self.Frame4)
        self.Button2.place(relx=0.127, rely=0.353, height=31, width=135)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {Times New Roman} -size 12 -weight bold -slant roman -underline 0 -overstrike 0")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''SHOW PRODUCT''')

        self.Button3 = tk.Button(self.Frame4)
        self.Button3.place(relx=0.347, rely=0.353, height=31, width=65)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font="-family {Times New Roman} -size 12 -weight bold -slant roman -underline 0 -overstrike 0")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''CLEAR''')
        self.Button3.configure(command=self.cleardata)

        self.Button4 = tk.Button(self.Frame4)
        self.Button4.place(relx=0.458, rely=0.353, height=31, width=75)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(font="-family {Times New Roman} -size 12 -weight bold -slant roman -underline 0 -overstrike 0")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''DELETE''')
        self.Button4.configure(command=self.deletedata)


        self.Button5 = tk.Button(self.Frame4)
        self.Button5.place(relx=0.585, rely=0.365, height=31, width=75)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(cursor="fleur")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(font="-family {Times New Roman} -size 12 -weight bold -slant roman -underline 0 -overstrike 0")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''SEARCH''')
        self.Button5.configure(command=self.searchdata)

        self.Button6 = tk.Button(self.Frame4)
        self.Button6.place(relx=0.711, rely=0.353, height=31, width=75)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(font="-family {Times New Roman} -size 12 -weight bold -slant roman -underline 0 -overstrike 0")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''UPDATE''')
        self.Button6.configure(command=self.updatedata)

        self.Button7 = tk.Button(self.Frame4)
        self.Button7.place(relx=0.849, rely=0.353, height=31, width=75)
        self.Button7.configure(activebackground="#ececec")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(font="-family {Times New Roman} -size 12 -weight bold -slant roman -underline 0 -overstrike 0")
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(text='''CLOSE''')
        self.Button7.configure(command=self.closeapp)

        self.myconn = mysql.connector.connect(host="localhost", user="root", passwd="root   ", database="Python4")
        # creating the cursor object
        self.cur = self.myconn.cursor()

        self.loadAllData()

        self.Listbox1.bind('<<ListboxSelect>>', self.my_upd)

    def my_upd(self,my_widget):
        my_w = my_widget.widget
        index = int(my_w.curselection()[0])
        value = my_w.get(index)
        print("You selected item ", index, value)
        it  = iter(value)

        self.Entry1.delete(0, tk.END)
        self.Entry1.insert(0, str(next(it)))

        self.Entry2.delete(0, tk.END)
        self.Entry2.insert(0, str(next(it)))

        self.Entry3.delete(0, tk.END)
        self.Entry3.insert(0, str(next(it)))

        self.Entry4.delete(0, tk.END)
        self.Entry4.insert(0, str(next(it)))

        self.Entry5.delete(0, tk.END)
        self.Entry5.insert(0, str(next(it)))


    def savedata(self):
        product_id = self.Entry1.get()
        product_name = self.Entry2.get()
        product_price = self.Entry3.get()
        product_company = self.Entry4.get()
        phone_no = self.Entry5.get()

        if product_id==None or product_id=="":
            messagebox.showerror("Error","Product ID Should Not Be Empty!!!")
            self.Entry1.focus_set()
            return
        if product_name==None or product_name=="":
            messagebox.showerror("Error","Product Name Should Not Be Empty!!!")
            self.Entry2.focus_set()
            return
        if product_price==None or product_price=="":
            messagebox.showerror("Error","Product Price Should Not Be Empty!!!")
            self.Entry3.focus_set()
            return
        if product_company==None or product_company=="":
            messagebox.showerror("Error","Product Company Should Not Be Empty!!!")
            self.Entry4.focus_set()
            return
        if phone_no==None or phone_no=="":
            messagebox.showerror("Error","Phone Number Should Not Be Empty!!!")
            self.Entry5.focus_set()
            return

        sql = "insert into product(product_id, product_name, product_price, product_comapany,phone_no) values (%s, %s, %s, %s, %s)"
        val=[]
        val.append(int(product_id))
        val.append(product_name)
        val.append(float(product_price))
        val.append(product_company)
        val.append(phone_no)
        val = tuple(val)

        try:
            self.cur.execute(sql, val)
            self.myconn.commit()
            messagebox.showinfo("Success",'Record Save Success!!!')
            self.loadAllData()
        except:
            self.myconn.rollback()
            messagebox.showerror("Failed",'Record Save Failed!!!')

    def cleardata(self):

        self.Entry1.delete(0, tk.END)
        self.Entry1.insert(0, "")

        self.Entry2.delete(0, tk.END)
        self.Entry2.insert(0, "")

        self.Entry3.delete(0, tk.END)
        self.Entry3.insert(0, "")

        self.Entry4.delete(0, tk.END)
        self.Entry4.insert(0, "")

        self.Entry5.delete(0, tk.END)
        self.Entry5.insert(0, "")

        self.Entry1.focus_set()



    def closeapp(self):
        MsgBox = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                           icon='warning')
        if MsgBox == 'yes':
            root.destroy()
        else:
            tk.messagebox.showinfo('Return', 'You will now return to the application screen')

    def loadAllData(self):
        try:
            self.Listbox1.delete(0, tk.END);
            # Reading the Employee data
            self.cur.execute("select product_id,product_name,product_price,product_comapany,phone_no from Product")

            # fetching the rows from the cursor object
            result = self.cur.fetchall()
            # printing the result
            for index , x in enumerate(result):
                print(index+1,x)
                self.Listbox1.insert(index+1,x)
        except:
            self.myconn.rollback()

    def searchdata(self):
        product_id = self.Entry1.get()
        try:
            # Reading the Employee data
            self.cur.execute(f"select product_id,product_name,product_price,product_comapany,phone_no from Product where product_id={product_id}")

            # fetching the rows from the cursor object
            result = self.cur.fetchone()
            print(result)

            if result==None:
                messagebox.showerror("Error", "Product Not Found!!!")
                return

            it = iter(result)

            self.Entry1.delete(0, tk.END)
            self.Entry1.insert(0, str(next(it)))

            self.Entry2.delete(0, tk.END)
            self.Entry2.insert(0, str(next(it)))

            self.Entry3.delete(0, tk.END)
            self.Entry3.insert(0, str(next(it)))

            self.Entry4.delete(0, tk.END)
            self.Entry4.insert(0, str(next(it)))

            self.Entry5.delete(0, tk.END)
            self.Entry5.insert(0, str(next(it)))
        except:
            self.myconn.rollback()
    def updatedata(self):

        product_id = self.Entry1.get()
        product_name = self.Entry2.get()
        product_price = self.Entry3.get()
        product_company = self.Entry4.get()
        phone_no = self.Entry5.get()

        if product_id==None or product_id=="":
            messagebox.showerror("Error","Product ID Should Not Be Empty!!!")
            self.Entry1.focus_set()
            return
        if product_name==None or product_name=="":
            messagebox.showerror("Error","Product Name Should Not Be Empty!!!")
            self.Entry2.focus_set()
            return
        if product_price==None or product_price=="":
            messagebox.showerror("Error","Product Price Should Not Be Empty!!!")
            self.Entry3.focus_set()
            return
        if product_company==None or product_company=="":
            messagebox.showerror("Error","Product Company Should Not Be Empty!!!")
            self.Entry4.focus_set()
            return
        if phone_no==None or phone_no=="":
            messagebox.showerror("Error","Phone Number Should Not Be Empty!!!")
            self.Entry5.focus_set()
            return

        sql = f"update product set product_name='{product_name}', product_price={product_price}, product_comapany='{product_company}',phone_no='{phone_no}' where product_id={product_id}"
        try:
            self.cur.execute(sql)
            self.myconn.commit()
            messagebox.showinfo("Success",'Record Update Success!!!')
            self.loadAllData()

        except:
            self.myconn.rollback()
            messagebox.showerror("Failed",'Record Update Failed!!!')

    def deletedata(self):

        product_id = self.Entry1.get()

        if product_id==None or product_id=="":
            messagebox.showerror("Error","Product ID Should Not Be Empty!!!")
            self.Entry1.focus_set()
            return

        sql = f"delete from product where product_id={product_id}"
        try:
            self.cur.execute(sql)
            self.myconn.commit()
            messagebox.showinfo("Success",'Record Deleted Success!!!')
            self.loadAllData()

        except:
            self.myconn.rollback()
            messagebox.showerror("Failed",'Record Deleted Failed!!!')
if __name__ == '__main__':
    vp_start_gui()





