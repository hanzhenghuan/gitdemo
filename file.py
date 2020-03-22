# name :fileinfo.py
# author :hanzhenghuan
# created: 2019.5
# version: 1.0

#description :system for teacher to manage student




from tkinter import *
top=Tk()
tea={'admin':{'Pwd':'123456','Name':'Admin'}}
stu={'BZB':'100'}#创建教师和学生的字典
top.title('学生管理系统登录界面')
top.geometry('300x150')
L1=Label(top,text="用户名").place(x=40,y=0)#创建文本框以及对应位置
E1=Entry(top,bd=4)
E1.place(x=90,y=0)
L2=Label(top,text="密码").place(x=50,y=50)
E2=Entry(top,bd=4)
E2.place(x=90,y=50)
def b1():
a,b=E1.get(),E2.get()
if a in tea and tea[a]['Pwd']==b:#若输入的名字和密码在教师的字典中
c=tea[a]['Name']
top2=Tk()
top2.geometry('300x150')
top2.title('登陆成功')