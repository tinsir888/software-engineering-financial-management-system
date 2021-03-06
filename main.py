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
    signInWindow.minsize(width, height)  # ????????????
    signInWindow.maxsize(width, height)  # ????????????


########################################## for all window ##########################################


########################################## for main window #########################################

def setFrame1(main_notebook, userID):
    frame1 = ttk.Frame(main_notebook, width=1000, height=600)
    frame1.pack(side=TOP)
    main_notebook.add(frame1, text='????????????')

    columns = ['??????', '???', '???', '???', '????????????', '??????', '??????', '??????']
    tb = ttk.Treeview(
        master=frame1,
        height=22,
        columns=columns,
        show='headings'
    )
    # defining table headings
    tb.heading(column='??????', text='??????', anchor='w', command=lambda: print('??????'))
    tb.heading(column='???', text='???', anchor='w', command=lambda: print('???'))
    tb.heading(column='???', text='???', anchor='w', command=lambda: print('???'))
    tb.heading(column='???', text='???', anchor='w', command=lambda: print('???'))
    tb.heading(column='????????????', text='????????????', anchor='w', command=lambda: print('????????????'))
    tb.heading(column='??????', text='??????', anchor='w', command=lambda: print('??????'))
    tb.heading(column='??????', text='??????', anchor='w', command=lambda: print('??????'))
    tb.heading(column='??????', text='??????', anchor='w', command=lambda: print('??????'))
    # defining table columns
    tb.column('??????', width=100, minwidth=100, anchor=S)
    tb.column('???', width=100, minwidth=100, anchor=S)
    tb.column('???', width=50, minwidth=50, anchor=S)
    tb.column('???', width=50, minwidth=50, anchor=S)
    tb.column('????????????', width=100, minwidth=100, anchor=S)
    tb.column('??????', width=200, minwidth=100, anchor=S)
    tb.column('??????', width=200, minwidth=100, anchor=S)
    tb.column('??????', width=200, minwidth=200, anchor=S)

    def refreshPage(frame, userID):
        global record_data
        record_data = queryAllRecords('system.db', userID)
        tb.delete(*tb.get_children())
        # print(record_data)
        for idx, data in enumerate(record_data):
            tb.insert("", END, values=data)
        tb.pack(pady=20)

    refreshButton = Button(frame1, text="????????????", width=10, font=("Microsoft JhengHei", 15),
                           command=lambda: refreshPage(frame1, userID), bg='#4A5360', foreground='white')
    refreshButton.place(x=800, y=490, width=132, height=40)


def setFrame2(main_notebook, userID):
    frame2 = ttk.Frame(main_notebook, width=1000, height=600)
    frame2.pack(side=TOP)
    main_notebook.add(frame2, text='????????????')

    # ---------------- name -------------------- #
    nameLabel = Label(frame2, text="??????:", font=("Microsoft JhengHei", 15), bg=color, foreground='white')
    nameLabel.place(x=200 - 10, y=100)
    nameInputEntry = Entry(frame2, width=20, font=("Microsoft JhengHei", 14))
    nameInputEntry.place(x=300 - 10, y=102, height=28)

    # ---------------- date -------------------- #
    date_str = StringVar()
    date_str_gain = lambda: [
        date_str.set(date)
        for date in [Calendar().selection()]
        if date]
    dateInputButton = Button(frame2, text='??????:', font=("Microsoft JhengHei", 15),
                             command=date_str_gain, bg='#4A5360', foreground='white')
    dateInputButton.place(x=200 - 10, y=150, height=28)

    dateInputEntry = Entry(frame2, width=20, font=("Microsoft JhengHei", 14), textvariable=date_str)
    dateInputEntry.place(x=300 - 10, y=152, height=28)

    # ---------------- type -------------------- #
    typeLabel = Label(frame2, text="????????????:", font=("Microsoft JhengHei", 15), bg=color, foreground='white')
    typeLabel.place(x=200 - 10, y=200)
    # typeInputEntry = Entry(frame2, width=20, font=("Microsoft JhengHei", 14))
    # typeInputEntry.place(x=300 - 10, y=202, height=28)
    type = StringVar()
    typeInputEntry = ttk.Combobox(frame2, width=17, font=("Microsoft JhengHei", 15), background=color,
                                  foreground="black", textvariable=type)
    typeInputEntry['value'] = ("??????", "??????", "??????", "??????")
    typeInputEntry.place(x=300 - 10, y=202, height=28)

    # ---------------- usage -------------------- #
    usageLabel = Label(frame2, text="??????:", font=("Microsoft JhengHei", 15), bg=color, foreground='white')
    usageLabel.place(x=200 - 10, y=250)
    usageInputEntry = Entry(frame2, width=20, font=("Microsoft JhengHei", 14))
    usageInputEntry.place(x=300 - 10, y=252, height=28)

    # ---------------- more -------------------- #
    moreLabel = Label(frame2, text="??????:", font=("Microsoft JhengHei", 15), bg=color, foreground='white')
    moreLabel.place(x=200 - 10, y=300)
    moreInputEntry = Entry(frame2, width=20, font=("Microsoft JhengHei", 14))
    moreInputEntry.place(x=300 - 10, y=302, height=28)

    # ---------------- number -------------------- #
    numberLabel = Label(frame2, text="??????:", font=("Microsoft JhengHei", 15), bg=color, foreground='white')
    numberLabel.place(x=200 - 10, y=350)
    numberInputEntry = Entry(frame2, width=20, font=("Microsoft JhengHei", 14))
    numberInputEntry.place(x=300 - 10, y=352, height=28)

    # ----------------- ???????????? --------------------- #
    def clickInsert(frame, userID):
        name = nameInputEntry.get()
        date = dateInputEntry.get().split("-")
        types = typeInputEntry.get()
        usage = usageInputEntry.get()
        more = moreInputEntry.get()
        number = numberInputEntry.get()
        if name == "" or types == "" or date == "" or number == "":
            tkinter.messagebox.showinfo("??????", '??????????????????')
        elif name != userID:
            tkinter.messagebox.showinfo('??????', '??????????????????????????????')
        else:
            number = int(number)
            if number <= 0:
                tkinter.messagebox.showinfo("??????", '?????????????????????')
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
            tkinter.messagebox.showinfo("??????", '??????????????????')
        elif name != userID:
            tkinter.messagebox.showinfo('??????', '??????????????????????????????')
        else:
            number = int(number)
            if number <= 0:
                tkinter.messagebox.showinfo("??????", '?????????????????????')
            else:
                deleteDataRecord(name, date[0], date[1], date[2], types, usage, more, number)

    insertButton = Button(frame2, text="??????", width=10, font=("Microsoft JhengHei", 15),
                          command=lambda: clickInsert(frame2, userID), bg='#4A5360', foreground='white')
    insertButton.place(x=250 - 15, y=400 + 7, width=132, height=40)

    deleteButton = Button(frame2, text="??????", width=10, font=("Microsoft JhengHei", 15),
                          command=lambda: clickDelete(frame2, userID), bg='#4A5360', foreground='white')
    deleteButton.place(x=400 - 15, y=400 + 7, width=132, height=40)


def setFrame3(main_notebook, userID):
    frame3 = ttk.Frame(main_notebook, width=1000, height=600)
    frame3.pack(side=TOP)
    main_notebook.add(frame3, text='????????????')
    text = Text(frame3, width=40, height=10, undo=True, autoseparators=False)
    fontConfig = tkinter.font.Font(size=25)
    text.configure(font=fontConfig)
    text.config(state=DISABLED)
    # ?????? pack(fill=X) ????????????????????????????????????????????? X??????????????????????????????Y??????????????????????????????BOTH????????????????????????????????????
    text.pack(pady=10)

    type = StringVar()
    yearLabel = Label(frame3, text="???????????????????????????:", font=("Microsoft JhengHei", 15), bg=color, foreground='white')
    yearLabel.place(x=150, y=360)
    yearInputEntry = Entry(frame3, width=7, font=("Microsoft JhengHei", 14), textvariable=type)
    yearInputEntry.place(x=350, y=362, height=28)

    def OneYear(frame, userID):
        year = yearInputEntry.get()
        if year == "":
            tkinter.messagebox.showinfo("??????", '???????????????')
        text.config(state=NORMAL)
        text.delete(1.0, END)
        income, spend, borrow, lend, remain = queryStatistics(userID, year, 'system.db')
        # ????????????????????????
        # width ???????????????????????????height ???????????????
        # INSERT ??????????????????END ???????????????
        text.insert(INSERT, "%s???????????????%.2f???\n\n????????????%.2f???\n\n????????????%.2f???\n\n????????????%.2f???\n\n???????????????%.2f???"
                    % (year, income, spend, borrow, lend, remain))
        text.config(state=DISABLED)

    def AllYears(frame, userID):
        text.config(state=NORMAL)
        text.delete(1.0, END)
        income, spend, borrow, lend, remain = queryStatistics(userID)
        # ????????????????????????
        # width ???????????????????????????height ???????????????
        # INSERT ??????????????????END ???????????????
        text.insert(INSERT, "?????????????????????%.2f???\n\n????????????%.2f???\n\n????????????%.2f???\n\n????????????%.2f???\n\n???????????????%.2f???"
                    % (income, spend, borrow, lend, remain))
        text.config(state=DISABLED)

    findyearButton = Button(frame3, text="??????????????????", width=10, font=("Microsoft JhengHei", 15),
                            command=lambda: OneYear(frame3, userID), bg='#4A5360', foreground='white')
    findyearButton.place(x=500, y=360, width=165, height=40)

    findallButton = Button(frame3, text="???????????????", width=10, font=("Microsoft JhengHei", 15),
                           command=lambda: AllYears(frame3, userID), bg='#4A5360', foreground='white')
    findallButton.place(x=700, y=360, width=132, height=40)


def setFrame4(main_notebook, userID):
    frame1 = ttk.Frame(main_notebook, width=1000, height=600)
    frame1.pack(side=TOP)
    main_notebook.add(frame1, text='????????????')

    type = StringVar()
    yearLabel = Label(frame1, text="???????????????????????????:", font=("Microsoft JhengHei", 15), bg=color, foreground='white')
    yearLabel.place(x=200 - 10, y=150)
    yearInputEntry = Entry(frame1, width=7, font=("Microsoft JhengHei", 14), textvariable=type)
    yearInputEntry.place(x=400, y=152, height=28)

    timeLabel = Label(frame1, text="???????????????????????????:", font=("Microsoft JhengHei", 15), bg=color, foreground='white')
    timeLabel.place(x=200 - 10, y=200)
    type = StringVar()
    timeInputEntry = ttk.Combobox(frame1, width=5, font=("Microsoft JhengHei", 15), background=color,
                                  foreground="black", textvariable=type)
    timeInputEntry['value'] = ("01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "??????")
    timeInputEntry.place(x=400, y=202, height=28)

    # ----------------- print accounting voucher --------------------- #
    def clickPrintAccVoucher(frame, userID):
        # record_data=queryAllRecords('system.db')
        year = yearInputEntry.get()
        month = timeInputEntry.get()
        if year == "" or month == "":
            tkinter.messagebox.showinfo("??????", '???????????????')
        else:
            newWindow = Toplevel(frame)
            setWindowBasic(newWindow, "????????????", 1000, 600)
            columns = ['??????', '???', '???', '???', '????????????', '??????', '??????', '??????']
            tb = ttk.Treeview(
                master=newWindow,
                height=22,
                columns=columns,
                show='headings'
            )
            # defining table headings
            tb.heading(column='??????', text='??????', anchor='w', command=lambda: print('??????'))
            tb.heading(column='???', text='???', anchor='w', command=lambda: print('???'))
            tb.heading(column='???', text='???', anchor='w', command=lambda: print('???'))
            tb.heading(column='???', text='???', anchor='w', command=lambda: print('???'))
            tb.heading(column='????????????', text='????????????', anchor='w', command=lambda: print('????????????'))
            tb.heading(column='??????', text='??????', anchor='w', command=lambda: print('??????'))
            tb.heading(column='??????', text='??????', anchor='w', command=lambda: print('??????'))
            tb.heading(column='??????', text='??????', anchor='w', command=lambda: print('??????'))
            # defining table columns
            tb.column('??????', width=100, minwidth=100, anchor=S)
            tb.column('???', width=100, minwidth=100, anchor=S)
            tb.column('???', width=50, minwidth=50, anchor=S)
            tb.column('???', width=50, minwidth=50, anchor=S)
            tb.column('????????????', width=100, minwidth=100, anchor=S)
            tb.column('??????', width=200, minwidth=100, anchor=S)
            tb.column('??????', width=200, minwidth=100, anchor=S)
            tb.column('??????', width=200, minwidth=200, anchor=S)

            global record_data
            record_data, sum = queryLimitRecords(year, month, userID, 'system.db')
            tb.delete(*tb.get_children())
            # print(record_data)
            for idx, data in enumerate(record_data):
                # print(data)
                tb.insert("", END, values=data)
            if sum >= 0:
                data0 = ['??????', year, month, 'all', '?????????', '', '', sum]
            else:
                data0 = ['??????', year, month, 'all', '?????????', '', '', -sum]
            tb.insert("", END, values=data0)
            tb.pack(pady=20)
            file_path = filedialog.askopenfilename(title=u'?????????????????????csv??????')
            print("??????????????????????????????", file_path)
            if file_path is not None:
                with open(file=file_path, mode='w+', encoding='utf-8-sig') as file:
                    csvwriter = csv.writer(file, delimiter=',')
                    for row_id in tb.get_children():
                        row = tb.item(row_id)['values']
                        print('save row:', row)
                        csvwriter.writerow(row)
                dialog.Dialog(None, {'title': 'File Modified', 'text': '????????????', 'bitmap': 'warning', 'default': 0,
                                     'strings': ('OK', 'Cancle')})
                print('????????????????????????')

    printButton = Button(frame1, text="????????????????????????", width=10, font=("Microsoft JhengHei", 15),
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

    IDLabel = Label(frame, text="??????:", font=("Microsoft JhengHei", 15), bg=color, foreground='white')
    IDLabel.place(x=200 - 35, y=100 + 7)

    ID = StringVar()
    IDInputEntry = Entry(frame, width=20, font=("Microsoft JhengHei", 14), textvariable=ID)
    IDInputEntry.place(x=300 - 35 - 40, y=102 + 7, height=28)

    passwordLabel = Label(frame, text="??????:", font=("Microsoft JhengHei", 15), bg=color, foreground='white')
    passwordLabel.place(x=200 - 35, y=150 + 7)

    password = StringVar()
    passwordInputEntry = Entry(frame, width=20, font=("Microsoft JhengHei", 14), textvariable=password)
    passwordInputEntry.place(x=300 - 35 - 40, y=152 + 7, height=28)

    infoLabel = Label(frame, font=("Microsoft JhengHei", 15), bg=color, foreground='white')
    infoLabel.place(x=200 - 35, y=260 + 7)

    def signUpConfirmed(signUpWindow):
        userId = ID.get()
        realPassword = selectPassword(userId)
        userPassword = password.get()
        if userId == '' or userPassword == '':
            tkinter.messagebox.showinfo("??????", '???????????????????????????')
            print('???????????????????????????')
        elif len(userPassword) < 6:
            tkinter.messagebox.showinfo("??????", '??????????????????')
            print('??????????????????')
        else:
            if realPassword is not None:
                tkinter.messagebox.showinfo('??????', '??????????????????,?????????????????????')
                updateData(userId, userPassword)
            else:
                addDataNameAndPassword(userId, userPassword)

            signUpWindow.destroy()
            signInWindow.attributes('-disabled', 0)

    def signUpReturn():
        signUpWindow.destroy()
        signInWindow.attributes('-disabled', 0)
        # signInWindow.mainloop()

    yesButton = Button(frame, text="??????", width=10, font=("Microsoft JhengHei", 15),
                       command=lambda: signUpConfirmed(signUpWindow), bg='#4A5360', foreground='white')
    yesButton.place(x=205 - 35, y=200 + 7, width=132, height=40)

    returnButton = Button(frame, text="??????", width=10, font=("Microsoft JhengHei", 15), command=lambda: signUpReturn(),
                          bg='#4A5360', foreground='white')
    returnButton.place(x=205 - 35 + 148, y=200 + 7, width=132, height=40)


def setSignInWindowFrame(frame):
    frame.pack(side=TOP)

    IDLabel = Label(frame, text="??????:", font=("Microsoft JhengHei", 15), bg=color, foreground='white')
    IDLabel.place(x=200 - 35, y=100 + 7)

    ID = StringVar()
    IDInputEntry = Entry(frame, width=20, font=("Microsoft JhengHei", 14), textvariable=ID)
    IDInputEntry.place(x=300 - 35 - 40, y=102 + 7, height=28)

    passwordLabel = Label(frame, text="??????:", font=("Microsoft JhengHei", 15), bg=color, foreground='white')
    passwordLabel.place(x=200 - 35, y=150 + 7)

    password = StringVar()
    passwordInputEntry = Entry(frame, width=20, font=("Microsoft JhengHei", 14), textvariable=password)
    passwordInputEntry.place(x=300 - 35 - 40, y=152 + 7, height=28)

    infoLabel = Label(frame, font=("Microsoft JhengHei", 15), bg=color, foreground='white')
    infoLabel.place(x=200 - 35, y=260 + 7)

    def signUp(signInWindow):
        signUpWindow = Toplevel(signInWindow)
        signInWindow.attributes('-disabled', 1)

        setWindowBasic(signUpWindow, "??????", 600, 360)

        frame = ttk.Frame(signUpWindow, width=1000, height=600)
        frame.pack()

        # setStyle(signUpWindow)
        setSignUpWindowFrame(frame, signUpWindow)

        signUpWindow.focus_force()  # ?????????????????????
        signUpWindow.mainloop()

    def enterMainWindow():
        userId = ID.get()
        userPassword = password.get()
        realPassword = selectPassword(userId)
        print(realPassword[0])
        if realPassword[0] == '':
            tkinter.messagebox.showinfo('??????', '?????????????????????????????????')
        else:
            if realPassword[0] != userPassword:
                tkinter.messagebox.showinfo('??????', '???????????????')
            else:
                # ?????????
                signInWindow.destroy()

                mainWindow = Tk()

                setWindowBasic(mainWindow, "??????????????????", 1000, 600)
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

    signUpButton = Button(frame, text="??????", width=10, font=("Microsoft JhengHei", 15),
                          command=lambda: signUp(signInWindow), bg='#4A5360', foreground='white')
    signUpButton.place(x=205 - 35, y=200 + 7, width=132, height=40)

    loginButton = Button(frame, text="??????", width=10, font=("Microsoft JhengHei", 15), command=enterMainWindow,
                         bg='#4A5360', foreground='white')
    loginButton.place(x=205 - 35 + 148, y=200 + 7, width=132, height=40)


######################################### for sign window ##########################################

def main():
    signInWindow.mainloop()


if __name__ == '__main__':
    signInWindow = Tk()
    setWindowBasic(signInWindow, "??????", 600, 360)

    frame = ttk.Frame(signInWindow, width=1000, height=600)
    frame.pack()

    color = '#21252b'
    setStyle(signInWindow)
    setSignInWindowFrame(frame)

    profile.run("main()")
    # main()
