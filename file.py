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
def b8():
m=E3.get()
if m in stu:
top6=Tk()
top6.title('错误')
top6.geometry('300x170')
L6=Label(top6,text='该学生已存在').place(x=110,y=50)
B10=Button(top6,text='OK',command=top6.destroy).place(x=140,y=110)
else:
top7=Tk()
top7.title('提示')
top7.geometry('300x170')
L7=Label(top7,text='请输入学生成绩').place(x=10,y=10)
E4=Entry(top7,bd=4)
E4.place(x=10,y=30)
def b11():
n=E4.get()
stu[m]=n
top7.destroy()
B11=Button(top7,text='OK',command=b11).place(x=110,y=120)
B12=Button(top7,text='Cancel',command=top7.destroy).place(x=170,y=120)
L5=Label(top5,text='请输入学生姓名').place(x=30,y=10)
B8=Button(top5,text='OK',command=b8).place(x=110,y=120)
B9=Button(top5,text='Cancel',command=top5.destroy).place(x=170,y=120)
top4=Tk()
top4.geometry('300x200')
top4.title('学生管理系统')
B5=Button(top4,text='添加成绩',command=b5).place(x=130,y=25)
B6=Button(top4,text='查看成绩',command=b6).place(x=130,y=75)
B7=Button(top4,text='退出系统',command=top4.destroy).place(x=130,y=125)
top4.mainloop()
L3=Label(top2,text='欢迎登陆').place(x=120,y=50)
B3=Button(top2,text='0K',command=b3).place(x=250,y=100)
top2.mainloop()
else:
top3=Tk()
top3.geometry('300x150')
top3.title('登陆失败')
L4=Label(top3,text='用户名或密码错误').place(x=100,y=50)
B4=Button(top3,text='OK',command=top3.destroy).place(x=250,y=100)
top3.mainloop()
B1=Button(top,text="登入",command=b1).place(x=110,y=100)
B2=Button(top,text="退出",command=top.destroy).place(x=170,y=100)
top.mainloop()