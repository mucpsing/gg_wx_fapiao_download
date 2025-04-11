# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date:
# @Last Modified by: CPS
# @Last Modified time: 2025-04-10 23:25:27.768326
# @file_path "D:\CPS\MyProject\Projects_Personal\GG_wx_fapiao_download"
# @Filename "test.py"
# @Description: 修改pdf文件的尺寸为A4 置顶对齐，方便打印
#
import os, sys

sys.path.append("..")

from os import path
import fitz


def get_page_display_size(page):
    """获取考虑旋转后的页面显示尺寸"""
    rotation = page.rotation
    if rotation in (90, 270):
        return page.rect.height, page.rect.width
    return page.rect.width, page.rect.height


def is_a4_portrait(page, tolerance=5):
    """检查页面是否为A4纵向"""
    a4_width, a4_height = 595, 842  # A4尺寸（单位：点）
    width, height = get_page_display_size(page)
    return abs(width - a4_width) <= tolerance and abs(height - a4_height) <= tolerance


def convert_pdf_to_a4_portrait(input_path, output_path, vertical_align="top"):
    """
    将PDF转换为A4纵向格式，支持置顶对齐
    :param input_path: 输入PDF路径
    :param output_path: 输出PDF路径
    :param vertical_align: 垂直对齐方式（"top" 或 "center"）
    """
    src_doc = fitz.open(input_path)
    new_doc = fitz.open()  # 创建新文档

    a4_width, a4_height = 595, 842

    for page_num in range(len(src_doc)):
        page = src_doc[page_num]
        display_width, display_height = get_page_display_size(page)

        if is_a4_portrait(page):
            new_page = new_doc.new_page(width=a4_width, height=a4_height)
            new_page.show_pdf_page(new_page.rect, src_doc, page_num)
        else:
            new_page = new_doc.new_page(width=a4_width, height=a4_height)
            scale = min(a4_width / display_width, a4_height / display_height)

            scaled_width = display_width * scale
            scaled_height = display_height * scale

            # 水平居中计算
            x = (a4_width - scaled_width) / 2

            # 垂直对齐方式判断
            if vertical_align.lower() == "top":
                y = 0  # 置顶对齐
            else:  # 默认居中
                y = (a4_height - scaled_height) / 2

            dest_rect = fitz.Rect(x, y, x + scaled_width, y + scaled_height)
            new_page.show_pdf_page(dest_rect, src_doc, page_num)

    new_doc.save(output_path)
    new_doc.close()
    src_doc.close()


if __name__ == "__main__":
    # 使用示例
    input_pdf = path.abspath(
        r"D:\CPS\MyProject\Projects_Personal\GG_wx_fapiao_download\data\粉盒，硒鼓.pdf"
    )
    convert_pdf_to_a4_portrait(input_pdf, "output.pdf")
