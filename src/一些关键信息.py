# -*- coding: utf-8 -*-
#
# @Author: CPS
# @email: 373704015@qq.com
# @Date: 2025-04-10 20:24:27.728475
# @Last Modified by: CPS
# @Last Modified time: 2025-04-10 20:24:27.728475
# @file_path "D:\CPS\MyProject\Projects_Personal\GG_wx_fapiao_download\src"
# @Filename "一些关键信息.py"
# @Description: 功能描述
#
import os, sys

sys.path.append("..")

from os import path
from pathlib import Path
from pydantic import BaseModel


发票页的请求url为 = r"http://zszjoa.prpsdc.com:8099/sys/attachment/sys_att_main/sysAttMain.do?method=readDownload&fdId=19610d2caeabfe395ab847a4df1854e2&useBrowserOpen=true&isSupportDirect=null&dj_ifr=true&open=1"
