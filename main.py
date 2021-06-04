'''
打印tkinter的版本
'''
import tkinter
from tkinter import *


print(tkinter.TkVersion)
root = Tk()      # 建立根窗口 自定义的Tk对象名称，也可以取其它名称
root.title("wxy")
root.config(bg= '#FFEDDF')
screenWidth = root.winfo_screenwidth()     # 屏幕宽度
screenHeight = root.winfo_screenheight()   # 屏幕高度
w = 322 # 窗口宽
h = 160 # 窗口高
x = (screenWidth - 2*w)/2 # 窗口左上角x轴位置
y = (screenHeight - 3*h)/2  # 窗口左上角y轴位置
root.geometry("%dx%d+%d+%d" % (w,h,x,y))  # 表示距离屏幕左上角(400,200)
# +x表示窗口左侧距离屏幕左侧距离, -x表示窗口右侧距离屏幕右侧的距离
# +y与-y的含义类似，窗口上侧(下侧)距离屏幕上侧(下侧)的距离
aaa=2234213

root.mainloop()  # 让程序继续运行，同时进入等待与处理窗口事件，放在程序最后一行1
