import hashlib, time
import ctypes
import ctypes.wintypes


def str2md5(inputStr: str = None) -> str:
    if not inputStr:
        inputStr = str(time.time())

    obj = hashlib.md5()

    obj.update(inputStr.encode("utf-8"))

    return obj.hexdigest()


def refresh_explorer(path=None):
    """
    通知资源管理器刷新指定目录（传None则刷新整个桌面）
    """
    # 定义Windows API常量
    SHCNE_ASSOCCHANGED = 0x08000000  # 文件关联变更事件
    SHCNE_UPDATEDIR = 0x00001000  # 目录内容更新事件
    SHCNF_IDLIST = 0x0000  # 标识按路径刷新
    SHCNF_PATHW = 0x0005  # 使用宽字符路径
    SHCNF_FLUSH = 0x1000  # 立即刷新

    shell32 = ctypes.windll.shell32

    if path:
        # 转换为绝对路径
        abs_path = ctypes.wintypes.LPCWSTR(path)
        # 发送目录更新事件
        shell32.SHChangeNotify(
            SHCNE_UPDATEDIR, SHCNF_PATHW | SHCNF_FLUSH, abs_path, None
        )
    else:
        # 发送全局关联变更事件（刷新整个桌面）
        shell32.SHChangeNotify(
            SHCNE_ASSOCCHANGED, SHCNF_IDLIST | SHCNF_FLUSH, None, None
        )
