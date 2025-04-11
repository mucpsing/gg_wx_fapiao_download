# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date: 2024-05-30 16:35:13.961047
# @Last Modified by: CPS
# @Last Modified time: 2024-05-30 16:35:13.961047
# @file_path "W:\CPS\MyProject\projsect_persional\python-tk-ui-learn\src"
# @Filename "events.py"
# @Description: 这是一个类似事件中心的组件，对应ui.py的Application类中所有回调方法
#
import os, sys

sys.path.append("..")

from src.utils.tk_utils import selectPath
from src.configEditor_launcher import UI as configEditor_show
from src.ui.main import Application


class UI_Var:
    Text1Var = "文件路径选择输入框，使用self.Text1Var.get()"


class UI_Events(Application):
    def mainBtn_sel_file_Cmd(self, event=None):
        """选择文件的按钮"""

        # 点击按钮打开文件的调用
        sel_path = selectPath("dir")
        if sel_path:
            if os.path.exists(sel_path):
                self.Text1Var.set(sel_path)

    def mainBtn_copy_Cmd(self, event=None):
        scripts = """var old_open=window.open;window.__cps||(window.__cps={readEl:document.getElementsByClassName("upload_opt_icon")[0]}),window.__cps.getHtmlContent=e=>{const n=document.getElementsByClassName(e);return 1!=n.length?(console.log("发生错误了，元素获取数量不对: ",n),""):n[0].innerHTML},window.open=function(e){const n=new URL(e);n.searchParams.set("dj_ifr","false"),n.searchParams.set("open","0"),n.searchParams.set("method","download"),console.log("fdId: ",n.searchParams.get("fdId")),fetch(n,{method:"GET",credentials:"include"}).then((e=>{if(!e.ok)throw new Error(`HTTP 错误，状态码：${e.status}`);const n=e.headers.get("content-type");return n.includes("application/json")?e.json():n.includes("text/")?e.text():e.blob()})).then((e=>{const n=__cps.getHtmlContent("upload_list_filename_title")+__cps.getHtmlContent("upload_list_filename_ext"),t=new FileReader;t.onload=function(e){const t=e.target.result,o=document.createElement("a");o.href=t,o.download=n,o.style.display="none",document.body.appendChild(o),o.click(),document.body.removeChild(o)},t.readAsDataURL(e)})).catch((e=>{console.error("请求失败：",e)}))};const readEl=document.getElementsByClassName("upload_opt_icon")[0],innerEl=readEl.querySelector(".upload_opt_tip_inner");innerEl.innerHTML="下载",readEl.click();"""

        import tkinter

        if self.root:
            self.root.clipboard_clear()  # 清空剪贴板
            self.root.clipboard_append(scripts)  # 添加文本到剪贴板
            self.root.attributes("-topmost", True)
        else:
            # 创建隐藏窗口
            root = tkinter.Tk()
            root.withdraw()  # 隐藏主窗口
            root.clipboard_clear()  # 清空剪贴板
            root.clipboard_append(scripts)  # 添加文本到剪贴板
            root.update()  # 确保剪贴板更新（必须调用）
            root.destroy()  # 销毁窗口（可选）

    # def mainBtn_open_config_editor_Cmd(self, subFormConfig):
    #     """打开一个子窗口"""
    #     configEditor_show()
