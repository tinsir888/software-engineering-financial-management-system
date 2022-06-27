# pylint: disable=C0116&&C0301&&C0103
import csv
from tkinter import *
from tkinter import ttk, filedialog, dialog
import tkinter.messagebox
import profile

# from main import *
from data_operate import *
from Calendar import Calendar


########################################## for all window ##########################################

def setStyle(signInWindow):
    signInWindow.configure(background=color)
    signInWindow.resizable(1, 1)

    # Notebook color
    sky_color = "sky blue"
    gold_color = "gold"
    color_tab = "#ccdee0"

    # style
    style = ttk.Style()
    style.theme_create("beautiful", parent="alt", settings={
        "TNotebook": {
            "configure": {
                "tabmargins": [10, 10, 20, 0],
                # "tabmargins": [10, 10, 20, 10],
                "background": sky_color
            }
        },
        "TNotebook.Tab": {
            "configure": {
                "padding": [30, 10],
                "background": sky_color,
                "font": ('Microsoft JhengHei', 14),
                "borderwidth": [0]
            },
            "map": {
                "background": [
                    ("selected", gold_color),
                    ('!active', sky_color),
                    ('active', color_tab)
                ],
                "expand": [
                    ("selected", [1, 1, 1, 0])
                ]
            }
        }
    }
                       )
    style.theme_use("beautiful")
    style.layout("Tab",
                 [('Notebook.tab', {
                     'sticky': 'nswe',
                     'children': [(
                         'Notebook.padding', {
                             'side': 'top',
                             'sticky': 'nswe',
                             'children': [('Notebook.label', {'side': 'top', 'sticky': ''})],
                         }
                     )],
                 }
                   )]
                 )
    style.configure('TLabel', background=color, foreground='white')
    style.configure('TFrame', background=color)
    style.configure('TEntry', background='white', foreground=color)


def setWindowBasic(signInWindow, titleName, width, height):
    signInWindow.title(titleName)
    signInWindow.geometry('700x420')
    signInWindow.minsize(width, height)  # 最小尺寸
    signInWindow.maxsize(width, height)  # 最大尺寸


########################################## for all window ##########################################


########################################## for main window #########################################

def setFrame1(main_notebook, userID):
    frame1 = ttk.Frame(main_notebook, width=1000, height=600)
    frame1.pack(side=TOP)
    main_notebook.add(frame1, text='我的记录')

    columns = ['姓名', '年', '月', '日', '收支类型', '用途', '其他', '金额']
    tb = ttk.Treeview(
        master=frame1,
        height=22,
        columns=columns,
        show='headings'
    )
    # defining table headings
    tb.heading(column='姓名', text='姓名', anchor='w', command=lambda: print('姓名'))
    tb.heading(column='年', text='年', anchor='w', command=lambda: print('年'))
    tb.heading(column='月', text='月', anchor='w', command=lambda: print('月'))
    tb.heading(column='日', text='日', anchor='w', command=lambda: print('日'))
    tb.heading(column='收支类型', text='收支类型', anchor='w', command=lambda: print('收支类型'))
    tb.heading(column='用途', text='用途', anchor='w', command=lambda: print('用途'))
    tb.heading(column='其他', text='其他', anchor='w', command=lambda: print('其他'))
    tb.heading(column='金额', text='金额', anchor='w', command=lambda: print('金额'))
    # defining table columns
    tb.column('姓名', width=100, minwidth=100, anchor=S)
    tb.column('年', width=100, minwidth=100, anchor=S)
    tb.column('月', width=50, minwidth=50, anchor=S)
    tb.column('日', width=50, minwidth=50, anchor=S)
    tb.column('收支类型', width=100, minwidth=100, anchor=S)
    tb.column('用途', width=200, minwidth=100, anchor=S)
    tb.column('其他', width=200, minwidth=100, anchor=S)
    tb.column('金额', width=200, minwidth=200, anchor=S)

    def refreshPage(frame, userID):
        global record_data
        record_data = queryAllRecords('system.db', userID)
        tb.delete(*tb.get_children())
        # print(record_data)
        for idx, data in enumerate(record_data):
            tb.insert("", END, values=data)
        tb.pack(pady=20)

    refreshButton = Button(frame1, text="刷新页面", width=10, font=("Microsoft JhengHei", 15),
                           command=lambda: refreshPage(frame1, userID), bg='#4A5360', foreground='white')
    refreshButton.place(x=800, y=490, width=132, height=40)


def setFrame2(main_notebook, userID):
    frame2 = ttk.Frame(main_notebook, width=1000, height=600)
    frame2.pack(side=TOP)
    main_notebook.add(frame2, text='新增记录')

    # ---------------- name -------------------- #
    nameLabel = Label(frame2, text="姓名:", font=("Microsoft JhengHei", 15), bg=color, foreground='white')
    nameLabel.place(x=200 - 10, y=100)
    nameInputEntry = Entry(frame2, width=20, font=("Microsoft JhengHei", 14))
    nameInputEntry.place(x=300 - 10, y=102, height=28)

    # ---------------- date -------------------- #
    date_str = StringVar()
    date_str_gain = lambda: [
        date_str.set(date)
        for date in [Calendar().selection()]
        if date]
    dateInputButton = Button(frame2, text='日期:', font=("Microsoft JhengHei", 15),
                             command=date_str_gain, bg='#4A5360', foreground='white')
    dateInputButton.place(x=200 - 10, y=150, height=28)

    dateInputEntry = Entry(frame2, width=20, font=("Microsoft JhengHei", 14), textvariable=date_str)
    dateInputEntry.place(x=300 - 10, y=152, height=28)

    # ---------------- type -------------------- #
    typeLabel = Label(frame2, text="收支类型:", font=("Microsoft JhengHei", 15), bg=color, foreground='white')
    typeLabel.place(x=200 - 10, y=200)
    # typeInputEntry = Entry(frame2, width=20, font=("Microsoft JhengHei", 14))
    # typeInputEntry.place(x=300 - 10, y=202, height=28)
    type = StringVar()
    typeInputEntry = ttk.Combobox(frame2, width=17, font=("Microsoft JhengHei", 15), background=color,
                                  foreground="black", textvariable=type)
    typeInputEntry['value'] = ("收入", "支出", "借入", "借出")
    typeInputEntry.place(x=300 - 10, y=202, height=28)

    # ---------------- usage -------------------- #
    usageLabel = Label(frame2, text="用途:", font=("Microsoft JhengHei", 15), bg=color, foreground='white')
    usageLabel.place(x=200 - 10, y=250)
    usageInputEntry = Entry(frame2, width=20, font=("Microsoft JhengHei", 14))
    usageInputEntry.place(x=300 - 10, y=252, height=28)

    # ---------------- more -------------------- #
    moreLabel = Label(frame2, text="其他:", font=("Microsoft JhengHei", 15), bg=color, foreground='white')
    moreLabel.place(x=200 - 10, y=300)
    moreInputEntry = Entry(frame2, width=20, font=("Microsoft JhengHei", 14))
    moreInputEntry.place(x=300 - 10, y=302, height=28)

    # ---------------- number -------------------- #
    numberLabel = Label(frame2, text="金额:", font=("Microsoft JhengHei", 15), bg=color, foreground='white')
    numberLabel.place(x=200 - 10, y=350)
    numberInputEntry = Entry(frame2, width=20, font=("Microsoft JhengHei", 14))
    numberInputEntry.place(x=300 - 10, y=352, height=28)

    # ----------------- 插入按钮 --------------------- #
    def clickInsert(frame, userID):
        name = nameInputEntry.get()
        date = dateInputEntry.get().split("-")
        types = typeInputEntry.get()
        usage = usageInputEntry.get()
        more = moreInputEntry.get()
        number = numberInputEntry.get()
        if name == "" or types == "" or date == "" or number == "":
            tkinter.messagebox.showinfo("注意", '有必填项为空')
        elif name != userID:
            tkinter.messagebox.showinfo('注意', '不能操作其他人的账户')
        else:
            number = int(number)
            if number <= 0:
                tkinter.messagebox.showinfo("注意", '金额必须大于零')
            else:
                addDataRecord(name, date[0], date[1], date[2], types, usage, more, number)

    def clickDelete(frame, userID):
        name = nameInputEntry.get()
        date = dateInputEntry.get().split("-")
        types = typeInputEntry.get()
        usage = usageInputEntry.get()
        more = moreInputEntry.get()
        number = numberInputEntry.get()
        if name == "" or types == "" or date == "" or number == "":
            tkinter.messagebox.showinfo("注意", '有必填项为空')
        elif name != userID:
            tkinter.messagebox.showinfo('注意', '不能操作其他人的账户')
        else:
            number = int(number)
            if number <= 0:
                tkinter.messagebox.showinfo("注意", '金额必须大于零')
            else:
                deleteDataRecord(name, date[0], date[1], date[2], types, usage, more, number)

    insertButton = Button(frame2, text="添加", width=10, font=("Microsoft JhengHei", 15),
                          command=lambda: clickInsert(frame2), bg='#4A5360', foreground='white')
    insertButton.place(x=250 - 15, y=400 + 7, width=132, height=40)

    deleteButton = Button(frame2, text="删除", width=10, font=("Microsoft JhengHei", 15),
                          command=lambda: clickDelete(frame2), bg='#4A5360', foreground='white')
    deleteButton.place(x=400 - 15, y=400 + 7, width=132, height=40)


def setFrame3(main_notebook, userID):
    frame3 = ttk.Frame(main_notebook, width=1000, height=600)
    frame3.pack(side=TOP)
    main_notebook.add(frame3, text='统计数据')
    text = Text(frame3, width=40, height=10, undo=True, autoseparators=False)
    fontConfig = tkinter.font.Font(size=25)
    text.configure(font=fontConfig)
    text.config(state=DISABLED)
    # 适用 pack(fill=X) 可以设置文本域的填充模式。比如 X表示沿水平方向填充，Y表示沿垂直方向填充，BOTH表示沿水平、垂直方向填充
    text.pack(pady=10)

    type = StringVar()
    yearLabel = Label(frame3, text="请输入要查询的年份:", font=("Microsoft JhengHei", 15), bg=color, foreground='white')
    yearLabel.place(x=150, y=360)
    yearInputEntry = Entry(frame3, width=7, font=("Microsoft JhengHei", 14), textvariable=type)
    yearInputEntry.place(x=350, y=362, height=28)

    def OneYear(frame, userID):
        year = yearInputEntry.get()
        if year == "":
            tkinter.messagebox.showinfo("注意", '请输入年份')
        text.config(state=NORMAL)
        text.delete(1.0, END)
        income, spend, borrow, lend, remain = queryStatistics(userID, year, 'system.db')
        # 创建一个文本控件
        # width 一行可见的字符数；height 显示的行数
        # INSERT 光标处插入；END 末尾处插入
        text.insert(INSERT, "%s年总收入：%.2f元\n\n总支出：%.2f元\n\n总借入：%.2f元\n\n总借出：%.2f元\n\n账户剩余：%.2f元"
                    % (year, income, spend, borrow, lend, remain))
        text.config(state=DISABLED)

    def AllYears(frame, userID):
        text.config(state=NORMAL)
        text.delete(1.0, END)
        income, spend, borrow, lend, remain = queryStatistics(userID)
        # 创建一个文本控件
        # width 一行可见的字符数；height 显示的行数
        # INSERT 光标处插入；END 末尾处插入
        text.insert(INSERT, "已记录总收入：%.2f元\n\n总支出：%.2f元\n\n总借入：%.2f元\n\n总借出：%.2f元\n\n账户剩余：%.2f元"
                    % (income, spend, borrow, lend, remain))
        text.config(state=DISABLED)

    findyearButton = Button(frame3, text="查询该年数据", width=10, font=("Microsoft JhengHei", 15),
                            command=lambda: OneYear(frame3, userID), bg='#4A5360', foreground='white')
    findyearButton.place(x=500, y=360, width=165, height=40)

    findallButton = Button(frame3, text="查询总数据", width=10, font=("Microsoft JhengHei", 15),
                           command=lambda: AllYears(frame3, userID), bg='#4A5360', foreground='white')
    findallButton.place(x=700, y=360, width=132, height=40)


def setFrame4(main_notebook, userID):
    frame1 = ttk.Frame(main_notebook, width=1000, height=600)
    frame1.pack(side=TOP)
    main_notebook.add(frame1, text='记账凭证')

    type = StringVar()
    yearLabel = Label(frame1, text="请输入要查询的年份:", font=("Microsoft JhengHei", 15), bg=color, foreground='white')
    yearLabel.place(x=200 - 10, y=150)
    yearInputEntry = Entry(frame1, width=7, font=("Microsoft JhengHei", 14), textvariable=type)
    yearInputEntry.place(x=400, y=152, height=28)

    timeLabel = Label(frame1, text="请输入要查询的月份:", font=("Microsoft JhengHei", 15), bg=color, foreground='white')
    timeLabel.place(x=200 - 10, y=200)
    type = StringVar()
    timeInputEntry = ttk.Combobox(frame1, width=5, font=("Microsoft JhengHei", 15), background=color,
                                  foreground="black", textvariable=type)
    timeInputEntry['value'] = ("01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "全年")
    timeInputEntry.place(x=400, y=202, height=28)

    # ----------------- print accounting voucher --------------------- #
    def clickPrintAccVoucher(frame, userID):
        # record_data=queryAllRecords('system.db')
        year = yearInputEntry.get()
        month = timeInputEntry.get()
        if year == "" or month == "":
            tkinter.messagebox.showinfo("注意", '请输入时间')
        else:
            newWindow = Toplevel(frame)
            setWindowBasic(newWindow, "记账凭证", 1000, 600)
            columns = ['姓名', '年', '月', '日', '收支类型', '用途', '其他', '金额']
            tb = ttk.Treeview(
                master=newWindow,
                height=22,
                columns=columns,
                show='headings'
            )
            # defining table headings
            tb.heading(column='姓名', text='姓名', anchor='w', command=lambda: print('姓名'))
            tb.heading(column='年', text='年', anchor='w', command=lambda: print('年'))
            tb.heading(column='月', text='月', anchor='w', command=lambda: print('月'))
            tb.heading(column='日', text='日', anchor='w', command=lambda: print('日'))
            tb.heading(column='收支类型', text='收支类型', anchor='w', command=lambda: print('收支类型'))
            tb.heading(column='用途', text='用途', anchor='w', command=lambda: print('用途'))
            tb.heading(column='其他', text='其他', anchor='w', command=lambda: print('其他'))
            tb.heading(column='金额', text='金额', anchor='w', command=lambda: print('金额'))
            # defining table columns
            tb.column('姓名', width=100, minwidth=100, anchor=S)
            tb.column('年', width=100, minwidth=100, anchor=S)
            tb.column('月', width=50, minwidth=50, anchor=S)
            tb.column('日', width=50, minwidth=50, anchor=S)
            tb.column('收支类型', width=100, minwidth=100, anchor=S)
            tb.column('用途', width=200, minwidth=100, anchor=S)
            tb.column('其他', width=200, minwidth=100, anchor=S)
            tb.column('金额', width=200, minwidth=200, anchor=S)

            global record_data
            record_data, sum = queryLimitRecords(year, month, userID, 'system.db')
            tb.delete(*tb.get_children())
            # print(record_data)
            for idx, data in enumerate(record_data):
                # print(data)
                tb.insert("", END, values=data)
            if sum >= 0:
                data0 = ['张三', year, month, 'all', '净收入', '', '', sum]
            else:
                data0 = ['张三', year, month, 'all', '净支出', '', '', -sum]
            tb.insert("", END, values=data0)
            tb.pack(pady=20)
            file_path = filedialog.askopenfilename(title=u'导出记账凭证为csv文件')
            print("导出记账凭证的路径：", file_path)
            if file_path is not None:
                with open(file=file_path, mode='w+', encoding='utf-8-sig') as file:
                    csvwriter = csv.writer(file, delimiter=',')
                    for row_id in tb.get_children():
                        row = tb.item(row_id)['values']
                        print('save row:', row)
                        csvwriter.writerow(row)
                dialog.Dialog(None, {'title': 'File Modified', 'text': '导出完成', 'bitmap': 'warning', 'default': 0,
                                     'strings': ('OK', 'Cancle')})
                print('导出记账凭证完成')

    printButton = Button(frame1, text="导出对应记账凭证", width=10, font=("Microsoft JhengHei", 15),
                         command=lambda: clickPrintAccVoucher(frame1, userID), bg='#4A5360', foreground='white')
    printButton.place(x=800, y=490, width=176, height=40)


def setFrames(main_notebook, userID):
    setFrame1(main_notebook, userID)
    setFrame2(main_notebook, userID)
    setFrame3(main_notebook, userID)
    setFrame4(main_notebook, userID)


########################################## for main window ##########################################


########################################## for sign window ##########################################

def setSignUpWindowFrame(frame, signUpWindow):
    frame.pack(side=TOP)

    IDLabel = Label(frame, text="姓名:", font=("Microsoft JhengHei", 15), bg=color, foreground='white')
    IDLabel.place(x=200 - 35, y=100 + 7)

    ID = StringVar()
    IDInputEntry = Entry(frame, width=20, font=("Microsoft JhengHei", 14), textvariable=ID)
    IDInputEntry.place(x=300 - 35 - 40, y=102 + 7, height=28)

    passwordLabel = Label(frame, text="密码:", font=("Microsoft JhengHei", 15), bg=color, foreground='white')
    passwordLabel.place(x=200 - 35, y=150 + 7)

    password = StringVar()
    passwordInputEntry = Entry(frame, width=20, font=("Microsoft JhengHei", 14), textvariable=password)
    passwordInputEntry.place(x=300 - 35 - 40, y=152 + 7, height=28)

    infoLabel = Label(frame, font=("Microsoft JhengHei", 15), bg=color, foreground='white')
    infoLabel.place(x=200 - 35, y=260 + 7)

    def signUpConfirmed(signUpWindow):
        userId = ID.get()
        userpassword = password.get()
        realPassword = selectPassword(userId)
        if len(userpassword) < 6:
            tkinter.messagebox.showinfo('提示', '密码长度过短')
        else:
            if realPassword is not None:
                tkinter.messagebox.showinfo('提示', '已注册用户名,已为您更新密码')
            userPassword = password.get()
            addDataNameAndPassword(userId, userPassword)

            signUpWindow.destroy()
            signInWindow.attributes('-disabled', 0)

    def signUpReturn():
        signUpWindow.destroy()
        signInWindow.attributes('-disabled', 0)
        # signInWindow.mainloop()

    yesButton = Button(frame, text="确定", width=10, font=("Microsoft JhengHei", 15),
                       command=lambda: signUpConfirmed(signUpWindow), bg='#4A5360', foreground='white')
    yesButton.place(x=205 - 35, y=200 + 7, width=132, height=40)

    returnButton = Button(frame, text="返回", width=10, font=("Microsoft JhengHei", 15), command=lambda: signUpReturn(),
                          bg='#4A5360', foreground='white')
    returnButton.place(x=205 - 35 + 148, y=200 + 7, width=132, height=40)


def setSignInWindowFrame(frame):
    frame.pack(side=TOP)

    IDLabel = Label(frame, text="姓名:", font=("Microsoft JhengHei", 15), bg=color, foreground='white')
    IDLabel.place(x=200 - 35, y=100 + 7)

    ID = StringVar()
    IDInputEntry = Entry(frame, width=20, font=("Microsoft JhengHei", 14), textvariable=ID)
    IDInputEntry.place(x=300 - 35 - 40, y=102 + 7, height=28)

    passwordLabel = Label(frame, text="密码:", font=("Microsoft JhengHei", 15), bg=color, foreground='white')
    passwordLabel.place(x=200 - 35, y=150 + 7)

    password = StringVar()
    passwordInputEntry = Entry(frame, width=20, font=("Microsoft JhengHei", 14), textvariable=password)
    passwordInputEntry.place(x=300 - 35 - 40, y=152 + 7, height=28)

    infoLabel = Label(frame, font=("Microsoft JhengHei", 15), bg=color, foreground='white')
    infoLabel.place(x=200 - 35, y=260 + 7)

    def signUp(signInWindow):
        signUpWindow = Toplevel(signInWindow)
        signInWindow.attributes('-disabled', 1)

        setWindowBasic(signUpWindow, "注册", 600, 360)

        frame = ttk.Frame(signUpWindow, width=1000, height=600)
        frame.pack()

        # setStyle(signUpWindow)
        setSignUpWindowFrame(frame, signUpWindow)

        signUpWindow.focus_force()  # 新窗口获得焦点
        signUpWindow.mainloop()

    def enterMainWindow():
        userId = ID.get()
        userPassword = password.get()
        realPassword = selectPassword(userId)

        if realPassword is None:
            tkinter.messagebox.showinfo('提示', '未注册，请先注册')
        else:
            if realPassword[0] != userPassword:
                tkinter.messagebox.showinfo('提示', '密码错误！')
            else:
                # 新窗口
                signInWindow.destroy()

                mainWindow = Tk()

                setWindowBasic(mainWindow, "财务管理系统", 1000, 600)
                color = '#21252b'
                setStyle(mainWindow)

                # frame
                frame_main_notebook = ttk.Frame(mainWindow, width=1000, height=600)
                frame_main_notebook.pack()

                # note book
                main_notebook = ttk.Notebook(frame_main_notebook, width=1000, height=600)
                main_notebook.pack(side=TOP, expand=1, fill='both')
                setFrames(main_notebook, userId)

                mainWindow.mainloop()

    signUpButton = Button(frame, text="注册", width=10, font=("Microsoft JhengHei", 15),
                          command=lambda: signUp(signInWindow), bg='#4A5360', foreground='white')
    signUpButton.place(x=205 - 35, y=200 + 7, width=132, height=40)

    loginButton = Button(frame, text="登录", width=10, font=("Microsoft JhengHei", 15), command=enterMainWindow,
                         bg='#4A5360', foreground='white')
    loginButton.place(x=205 - 35 + 148, y=200 + 7, width=132, height=40)


######################################### for sign window ##########################################

def main():
    signInWindow.mainloop()


if __name__ == '__main__':
    signInWindow = Tk()
    setWindowBasic(signInWindow, "登录", 600, 360)

    frame = ttk.Frame(signInWindow, width=1000, height=600)
    frame.pack()

    color = '#21252b'
    setStyle(signInWindow)
    setSignInWindowFrame(frame)

    profile.run("main()")
    # main()
