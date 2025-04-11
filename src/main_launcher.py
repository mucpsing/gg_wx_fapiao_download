# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date: 2024-05-30 09:36:14.265723
# @Last Modified by: CPS
# @Last Modified time: 2024-05-30 09:36:14.265723
# @file_path "W:\CPS\MyProject\projsect_persional\python-tk-ui-learn\src"
# @Filename "test2.py"
# @Description: 功能描述
#

import tkinter, os, sys

sys.path.append("..")

from tkinter.messagebox import showwarning
from src.utils.tk_utils import selectPath

from src.ui.main import Application
from src.config import Config

# from src.events import UI_Events

# from src.configEditor_launcher import UI as configEditor_show
# from src.configEditor_launcher import SubWindowConfig

from enum import Enum


def check(config: Config):
    if float(tkinter.TkVersion) < 8.6:
        showwarning("版本过低提示", "注意，当前tk版本过低，可能存在未知问题")

    # 校验config对象
    pass


class UI(Application):
    # 这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, config: Config):
        check(config)
        root = tkinter.Tk()
        super().__init__(root)

        self.root = root

        self.master.title(config.title)
        self.config = config

        self.configEditor = None  # close 或者 open

        screenWidth = root.winfo_screenwidth()  # 获取显示区域的宽度
        screenHeight = root.winfo_screenheight()  # 获取显示区域的高度
        left = int((screenWidth - config.width) / 2)  # 定位x
        top = int((screenHeight - config.height) / 2 * 0.8)  # 定位y

        self.master.geometry(f"{config.width}x{config.height}+{left}+{top}")
        if config.dragged_file_enable:
            self.init_dragged_file()

        self.master.protocol("WM_DELETE_WINDOW", self.on_close)
        self.createWidgets()
        self.process_start()

    def process_start(self):
        self.mainloop()

    def init_dragged_file(self):
        import windnd

        def dragged_files(files, encodeing="gbk"):
            if len(files) > 1:
                showwarning("文件太多", "仅支持单个文件识别")
            self.Text1Var.set(files[0].decode(encodeing))

        windnd.hook_dropfiles(self.master, func=dragged_files)

    def on_close(self):
        self.master.quit()
        self.master.destroy()

    # def mainBtn_open_config_editor_Cmd(self):
    #     """打开一个子窗口"""
    #     if self.configEditor is None:
    #         sub_height = 500
    #         subConfig = SubWindowConfig(
    #             title="配置编辑器",
    #             width=300,
    #             height=sub_height,
    #             left=int(self.master.winfo_x() + self.config.width + 5),
    #             top=int(self.master.winfo_y()),
    #         )
    #         self.configEditor = configEditor_show(subConfig, self)

    #     else:
    #         self.configEditor.on_close()
    #         self.configEditor = None

    def mainBtn_sel_file_Cmd(self, event=None):
        """选择文件的按钮"""

        # 点击按钮打开文件的调用
        sel_path = selectPath("dir")
        if sel_path:
            if os.path.exists(sel_path):
                self.Text1Var.set(sel_path)

    def mainBtn_copy_Cmd(self, event=None):
        scripts = """var old_open=window.open;window.__cps||(window.__cps={readEl:document.getElementsByClassName("upload_opt_icon")[0]}),window.__cps.getHtmlContent=e=>{const n=document.getElementsByClassName(e);return 1!=n.length?(console.log("发生错误了，元素获取数量不对: ",n),""):n[0].innerHTML},window.open=function(e){const n=new URL(e);n.searchParams.set("dj_ifr","false"),n.searchParams.set("open","0"),n.searchParams.set("method","download"),console.log("fdId: ",n.searchParams.get("fdId")),fetch(n,{method:"GET",credentials:"include"}).then((e=>{if(!e.ok)throw new Error(`HTTP 错误，状态码：${e.status}`);const n=e.headers.get("content-type");return n.includes("application/json")?e.json():n.includes("text/")?e.text():e.blob()})).then((e=>{const n=__cps.getHtmlContent("upload_list_filename_title")+__cps.getHtmlContent("upload_list_filename_ext"),t=new FileReader;t.onload=function(e){const t=e.target.result,o=document.createElement("a");o.href=t,o.download=n,o.style.display="none",document.body.appendChild(o),o.click(),document.body.removeChild(o)},t.readAsDataURL(e)})).catch((e=>{console.error("请求失败：",e)}))};const readEl=document.getElementsByClassName("upload_opt_icon")[0],innerEl=readEl.querySelector(".upload_opt_tip_inner");innerEl.innerHTML="下载",readEl.click();"""
        self.root.clipboard_clear()  # 清空剪贴板
        self.root.clipboard_append(scripts)  # 添加文本到剪贴板
        self.root.attributes("-topmost", True)


def start_with_ui():
    config = Config

    UI(config)


if __name__ == "__main__":
    start_with_ui()
