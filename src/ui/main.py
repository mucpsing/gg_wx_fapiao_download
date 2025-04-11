#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import os, sys
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
#Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
from tkinter.messagebox import *
#from tkinter import filedialog  #.askopenfilename()
#from tkinter import simpledialog  #.askstring()

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('Form1')
        self.master.geometry('878x496+1+2')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.mainBtn_sel_fileVar = StringVar(value='绑定目录')
        self.style.configure('TmainBtn_sel_file.TButton', font=('宋体',12))
        self.mainBtn_sel_file = Button(self.top, text='绑定目录', textvariable=self.mainBtn_sel_fileVar, command=self.mainBtn_sel_file_Cmd, style='TmainBtn_sel_file.TButton')
        self.mainBtn_sel_file.setText = lambda x: self.mainBtn_sel_fileVar.set(x)
        self.mainBtn_sel_file.text = lambda : self.mainBtn_sel_fileVar.get()
        self.mainBtn_sel_file.place(relx=0.014, rely=0.847, relwidth=0.958, relheight=0.124)

        self.style.configure('TFrame1.TLabelframe', font=('宋体',9))
        self.style.configure('TFrame1.TLabelframe.Label', font=('宋体',9))
        self.Frame1 = LabelFrame(self.top, text='当前目录绑定目录', style='TFrame1.TLabelframe')
        self.Frame1.place(relx=0.014, rely=0.629, relwidth=0.958, relheight=0.197)

        self.mainBtn_copyVar = StringVar(value='一键【点击】复制下载脚本')
        self.style.configure('TmainBtn_copy.TButton', font=('宋体',14))
        self.mainBtn_copy = Button(self.top, text='一键【点击】复制下载脚本', textvariable=self.mainBtn_copyVar, command=self.mainBtn_copy_Cmd, style='TmainBtn_copy.TButton')
        self.mainBtn_copy.setText = lambda x: self.mainBtn_copyVar.set(x)
        self.mainBtn_copy.text = lambda : self.mainBtn_copyVar.get()
        self.mainBtn_copy.place(relx=0.014, rely=0.024, relwidth=0.972, relheight=0.584)

        self.Text1Var = StringVar(value='')
        self.Text1 = Entry(self.Frame1, textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.setText = lambda x: self.Text1Var.set(x)
        self.Text1.text = lambda : self.Text1Var.get()
        self.Text1.place(relx=0.014, rely=0.246, relwidth=0.971, relheight=0.631)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        super().__init__(master)

    def mainBtn_sel_file_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def mainBtn_copy_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()



