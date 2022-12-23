import win32gui,win32con
import sys

import pyautogui
import cv2
import numpy as np
def get_hwnd_dic(hwnd, hwnd_title):
    if (win32gui.IsWindow(hwnd)
            and win32gui.IsWindowEnabled(hwnd)
            and win32gui.IsWindowVisible(hwnd)
            and win32gui.GetWindowText(hwnd)):
        hwnd_title[f"{hwnd}"] = win32gui.GetWindowText(hwnd)
def get_hwnd():
    """
    :return: {hwnd:title}
    """
    hwnd_title = {}
    win32gui.EnumWindows(get_hwnd_dic, hwnd_title)
    return hwnd_title


#获取所有窗口句柄
target_window = ""
hwndJson = get_hwnd()
for key in hwndJson:
  if "Google Chrome" in hwndJson[key]:
    target_window = hwndJson[key]

if target_window == "":
  print("无有效句柄")
  sys.exit(1)
  
hwnd= win32gui.FindWindow(None, target_window)
#以下代码由于实际执行截图会比激活窗口快 考虑在第一次执行时忽略结果
#全屏
win32gui.ShowWindow(hwnd, win32con.SW_SHOWMAXIMIZED)
#激活窗口
win32gui.SetForegroundWindow(hwnd)

(left, top, right, bottom) = win32gui.GetClientRect(hwnd)
img = pyautogui.screenshot(region=[left,top, right, bottom])  # 分别代表：左上角坐标，宽高
#对获取的图片转换成二维矩阵形式，后再将RGB转成BGR
#因为imshow,默认通道顺序是BGR，而pyautogui默认是RGB所以要转换一下，不然会有点问题
img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
cv2.imwrite('cookie.jpg', img)
cv2.destroyAllWindows()

