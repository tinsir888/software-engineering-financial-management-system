# coding=utf-8
# pylint: disable=C0116
import sqlite3
from tkinter import *
from tkinter import ttk, filedialog, dialog
import tkinter.messagebox

def createNameAndPassword(db='system.db'):
    """
    创建表
    """
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    str = "DROP TABLE IF EXISTS \"nameAndPassword\";" \
          "CREATE TABLE \"nameAndPassword\" " \
          "(" \
          "    \"name\" text NOT NULL," \
          "    \"password\" text NOT NULL," \
          "    PRIMARY KEY (\"name\")" \
          ");"
    for i in str.split(';'):
        cur.execute(i)
    conn.commit()
    cur.close()
    conn.close()
    print('创建数据库%s成功' % db)


def createRecord(db='system.db'):
    """
    创建表
    """
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    str = "DROP TABLE IF EXISTS \"record\";" \
          "CREATE TABLE \"record\" " \
          "(" \
          "    \"name\" text NOT NULL," \
          "    \"year\" text NOT NULL," \
          "    \"month\" text NOT NULL," \
          "    \"day\" text NOT NULL," \
          "    \"types\" text," \
          "    \"usage\" text," \
          "    \"more\" text," \
          "    \"number\" real NOT NULL" \
          ");"
    for i in str.split(';'):
        cur.execute(i)
    conn.commit()
    cur.close()
    conn.close()
    print('创建数据库%s成功' % db)


def addDataNameAndPassword(name, password, db='system.db'):

    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("insert into nameAndPassword values('%s','%s')" % (name, password))
    conn.commit()
    cur.close()
    conn.close()
    tkinter.messagebox.showinfo('提示', '注册成功')
    print('添加数据成功')


def addDataRecord(name, year, month, day, types, usage, more, number, db='system.db'):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    try:
        cur.execute("insert into record values('%s','%s','%s','%s','%s','%s','%s',%d)" % (
            name, year, month, day, types, usage, more, number))
        conn.commit()
        tkinter.messagebox.showinfo("提示", '数据添加成功')
        print('添加数据成功')
    except:
        tkinter.messagebox.showinfo("注意", '数据添加失败')
        print('添加数据失败')
        return False
    cur.close()
    conn.close()
    return True


def deleteDataRecord(name, year, month, day, types, usage, more, number, db='system.db'):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(
        "delete from record where name=='%s' and year=='%s' and month=='%s' "
        "and day=='%s' and types=='%s' and usage=='%s' and more=='%s' and number==%d"
        % (name, year, month, day, types, usage, more, number))
    conn.commit()
    if cur.rowcount == 0:
        tkinter.messagebox.showinfo("注意", '没有该记录，删除失败')
        print('没有这条记录')
        return False
    tkinter.messagebox.showinfo("提示", '成功删除')
    print('删除数据成功')
    cur.close()
    conn.close()
    return True


def selectPassword(name, db='system.db'):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("select password from nameAndPassword where name = '%s'" % name)
    res = cur.fetchone()
    if res:
        print('查询数据成功')
    else:
        res = ('',)
        print('未找到查询数据')
    cur.close()
    conn.close()
    return res


def queryAll(db='system.db'):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    sql = "select * from nameAndPassword"
    cur.execute(sql)
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()
    print('打印用户信息成功')


def queryAllRecords(db='system.db', userID=''):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    print(userID)
    sql = "select * from record where name = '%s'" % (userID)
    cur.execute(sql)
    ret = cur.fetchall()
    cur.close()
    conn.close()
    print('打印收支记录成功')
    return ret


def updateData(name, password, db='system.db'):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("update nameAndPassword set password= '%s' where name = '%s'" % (password, name))
    conn.commit()
    cur.close()
    conn.close()
    print('更新数据成功')


def queryLimitRecords(yea, mon, userID='', db='system.db'):
    """
    创建指定月份范围内记账凭证
    """
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    if mon == "全年":
        cur.execute("select * from record where year= '%s'  and name = '%s'" % (yea, userID))
    else:
        cur.execute("select * from record where year= '%s' and month= '%s' and name = '%s'" % (yea, mon, userID))
    ret = cur.fetchall()
    cur.close()
    cur3 = conn.cursor()
    cur4 = conn.cursor()
    cur5 = conn.cursor()
    cur2 = conn.cursor()
    if mon == "全年":
        cur2.execute("select sum(number) from record where year= '%s' and types= '收入' and name = '%s'" % (yea, userID))
        cur3.execute("select sum(number) from record where year= '%s' and types= '支出' and name = '%s'" % (yea, userID))
        cur4.execute("select sum(number) from record where year= '%s' and types= '借入' and name = '%s'" % (yea, userID))
        cur5.execute("select sum(number) from record where year= '%s' and types= '借出' and name = '%s'" % (yea, userID))
    else:
        cur2.execute(
            "select sum(number) from record where year= '%s' and month= '%s' and types= '收入' and name = '%s'" % (
                yea, mon, userID))
        cur3.execute(
            "select sum(number) from record where year= '%s' and month= '%s' and types= '支出' and name = '%s'" % (
                yea, mon, userID))
        cur4.execute(
            "select sum(number) from record where year= '%s' and month= '%s' and types= '借入' and name = '%s'" % (
                yea, mon, userID))
        cur5.execute(
            "select sum(number) from record where year= '%s' and month= '%s' and types= '借出' and name = '%s'" % (
                yea, mon, userID))
    sum2 = cur2.fetchone()[0]
    sum3 = cur3.fetchone()[0]
    sum4 = cur4.fetchone()[0]
    sum5 = cur5.fetchone()[0]
    sum = (sum2 if sum2 is not None else 0) - (sum3 if sum3 is not None else 0) + \
          (sum4 if sum4 is not None else 0) - (sum5 if sum5 is not None else 0)
    cur2.close()
    cur3.close()
    cur4.close()
    cur5.close()
    conn.close()
    print('已创建记账凭证')
    return ret, sum


def queryStatistics(userID='', year='-1', db='system.db'):
    """
    查询总收入、总支出、总借入、总借出、账户剩余
    返回：总收入、总支出、总借入、总借出、账户剩余
    """
    conn = sqlite3.connect(db)
    cur2 = conn.cursor()
    cur3 = conn.cursor()
    cur4 = conn.cursor()
    cur5 = conn.cursor()
    if year == '-1':
        cur2.execute("select sum(number) from record where types= '收入' and name = '%s'" % userID)
        cur3.execute("select sum(number) from record where types= '支出' and name = '%s'" % userID)
        cur4.execute("select sum(number) from record where types= '借入' and name = '%s'" % userID)
        cur5.execute("select sum(number) from record where types= '借出' and name = '%s'" % userID)
    else:
        cur2.execute(
            "select sum(number) from record where types= '收入' and name = '%s' and year = '%s'" % (userID, year))
        cur3.execute(
            "select sum(number) from record where types= '支出' and name = '%s' and year = '%s'" % (userID, year))
        cur4.execute(
            "select sum(number) from record where types= '借入' and name = '%s' and year = '%s'" % (userID, year))
        cur5.execute(
            "select sum(number) from record where types= '借出' and name = '%s' and year = '%s'" % (userID, year))
    tot_income = cur2.fetchone()[0]
    tot_expenditure = cur3.fetchone()[0]
    tot_borrow = cur4.fetchone()[0]
    tot_lend = cur5.fetchone()[0]
    cur2.close()
    cur3.close()
    cur4.close()
    cur5.close()
    conn.close()
    '''
    tot_income = (0 if tot_income==None else tot_income)
    tot_expenditure = (0 if tot_expenditure==None else tot_expenditure)
    tot_borrow = (0 if tot_borrow==None else tot_borrow)
    tot_lend = (0 if tot_lend==None else tot_lend)
    '''
    tot_remain = (0 if tot_income is None else tot_income) + (0 if tot_borrow is None else tot_borrow) - \
                 (0 if tot_expenditure is None else tot_expenditure) - (0 if tot_lend is None else tot_lend)
    print('收入:', tot_income, '支出:', tot_expenditure, '借入:', tot_borrow, '借出:', tot_lend, '盈亏:', tot_remain)
    return (0 if tot_income is None else tot_income), \
           (0 if tot_expenditure is None else tot_expenditure), \
           (0 if tot_borrow is None else tot_borrow), \
           (0 if tot_lend is None else tot_lend), \
           tot_remain
