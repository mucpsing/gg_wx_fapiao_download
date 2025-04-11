# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date: 2025-04-11 14:51:13.726317
# @Last Modified by: CPS
# @Last Modified time: 2025-04-11 14:51:13.726317
# @file_path "W:\CPS\MyProject\projsect_persional\gg_wx_fapiao_download\src"
# @Filename "watchfolder.py"
# @Description: 监听指定的文件夹，当文件发生添加或者删除后，执行指定的动作，当前脚本是监听所有pdf文件，有新增或者删除时，对没处理过的pdf脚本进行a4尺寸转换转换
#
import os, sys

sys.path.append("..")

from os import path
from pathlib import Path


import time
import threading
from src import utils
from src.utils import tools, pdf


class DirectoryWatchToA4Pdf:
    def __init__(self, watch_path: str, interval=1):
        self.path = watch_path
        self.interval = interval
        self._running = False
        self.thread = None
        self.handleFileList = []

    def _conver_pdf_a4(self):
        p = Path(self.path)
        for each in p.glob("*.pdf"):
            if each.name.endswith("_A4.pdf"):
                continue

            md5 = tools.str2md5(f"{each.name}_{each.stat().st_mtime}")

            if md5 in self.handleFileList:
                continue

            if not md5 in self.handleFileList:
                basename, ext = path.splitext(each.name)
                output_a4_pdf = path.join(self.path, f"{basename}_A4{ext}")
                pdf.convert_pdf_to_a4_portrait(each, output_a4_pdf)
                self.handleFileList.append(md5)

    def _get_files(self):
        """获取当前目录下所有文件的集合"""
        return set(
            os.path.join(root, f)
            for root, _, files in os.walk(self.path)
            for f in files
        )

    def _poll(self):
        """轮询逻辑的核心循环"""
        previous_files = self._get_files()
        while self._running:
            time.sleep(self.interval)
            current_files = self._get_files()
            created = current_files - previous_files
            deleted = previous_files - current_files
            if created:
                print(f"[轮询] 新增文件: {created}")
                for each in created:
                    if not each.endswith(".pdf"):
                        continue

                    full_path = path.join(self.path, each)
                    basename, ext = path.splitext(path.basename(full_path))
                    md5 = tools.str2md5(f"{basename}_{os.stat(full_path).st_ctime}")
                    output_a4_pdf = path.join(self.path, f"{basename}_A4{ext}")
                    if md5 in self.handleFileList and path.exists(output_a4_pdf):
                        print("文件md5已存在跳过: ", basename)
                        continue

                    if each.endswith("_A4.pdf"):
                        continue

                    pdf.convert_pdf_to_a4_portrait(each, output_a4_pdf)
                    self.handleFileList.append(md5)

                tools.refresh_explorer()

            if deleted:
                print(f"[轮询] 删除文件: {deleted}")
            previous_files = current_files

    def start(self):
        # self._conver_pdf_a4()
        """启动轮询线程"""
        if not self._running:
            self._running = True
            self.thread = threading.Thread(target=self._poll)
            self.thread.daemon = True  # 设置为守护线程，主程序退出时自动终止
            self.thread.start()
            print("轮询线程已启动")

    def stop(self):
        """停止轮询线程"""
        if self._running:
            self._running = False
            # self.thread.join()  # 等待线程结束
            print("轮询线程已停止")


# 使用示例
# if __name__ == "__main__":
#     tar = r"W:\CPS\MyProject\projsect_persional\gg_wx_fapiao_download\data"

#     poller = DirectoryWatchToA4Pdf(tar, interval=1)
#     poller.start()

#     try:
#         # 主程序继续执行其他逻辑
#         while True:
#             print("[主程序] 正在运行...")
#             time.sleep(5)
#     except KeyboardInterrupt:
#         poller.stop()
