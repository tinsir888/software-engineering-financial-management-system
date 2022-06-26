# coding=utf-8
import sqlite3

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
          "    PRIMARY KEY (\"name\", \"password\")" \
          ");"
    for i in str.split(';'):
        cur.execute(i)
    conn.commit()
    cur.close()
    conn.close()
    print('\n创建数据库%s成功' % db)


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
    print('\n创建数据库%s成功' % db)


def addDataNameAndPassword(name, password, db='system.db'):
    if name.strip() == '':
        print('姓名不能为空')
        return False
    if password.strip() == '':
        print('密码不能为空')
        return False

    conn = sqlite3.connect(db)
    cur = conn.cursor()
    try:
        cur.execute("insert into nameAndPassword values('%s','%s')" % (name, password))
        conn.commit()
        print('添加数据成功')
        return True
    except:
        print('您已注册')
        return False
    cur.close()
    conn.close()


def addDataRecord(name, year, month, day, types, usage, more, number, db='system.db'):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    try:
        cur.execute("insert into record values('%s','%s','%s','%s','%s','%s','%s',%d)" % (
            name, year, month, day, types, usage, more, number))
        conn.commit()
        print('添加数据成功')
    except:
        print('添加数据失败')
        return False
    cur.close()
    conn.close()


def deleteDataRecord(name, year, month, day, types, usage, more, number, db='system.db'):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    try:
        cur.execute(
            "delete from record where name=='%s' and year=='%s' and month=='%s' and day=='%s' and types=='%s' and usage=='%s' and more=='%s' and number==%d"
            % (name, year, month, day, types, usage, more, number))
        conn.commit()
        print('删除数据成功')
    except:
        print('删除数据失败')
        return False
    cur.close()
    conn.close()


def selectPassword(name, db='system.db'):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("select password from nameAndPassword where name = '%s'" % name)
    res = cur.fetchone()
    # print(res)
    cur.close()
    conn.close()
    print('查询数据成功')
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
    print('打印数据成功')


def queryAllRecords(db='system.db'):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    sql = "select * from record"
    cur.execute(sql)
    ret = cur.fetchall()
    cur.close()
    conn.close()
    print('successfully fetch all records!')
    return ret


def updateData(number, result, db='system.db'):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("update nameAndPassword set result= '%s' where number = %s" % (result, number))
    conn.commit()
    cur.close()
    conn.close()
    print('更新数据成功')

def queryLimitRecords(yea, mon, db='system.db'):
    """
    创建指定月份范围内记账凭证
    """
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    if mon == "全年":
        cur.execute("select * from record where year= '%s' " % (yea))
    else:
        cur.execute("select * from record where year= '%s' and month= '%s'" % (yea, mon))
    ret = cur.fetchall()
    cur.close()
    cur2 = conn.cursor()
    cur3 = conn.cursor()
    cur4 = conn.cursor()
    cur5 = conn.cursor()
    cur2.execute("select sum(number) from record where year= '%s' and month= '%s' and types= '收入'" % (yea, mon))
    cur3.execute("select sum(number) from record where year= '%s' and month= '%s' and types= '支出'" % (yea, mon))
    cur4.execute("select sum(number) from record where year= '%s' and month= '%s' and types= '借入'" % (yea, mon))
    cur5.execute("select sum(number) from record where year= '%s' and month= '%s' and types= '借出'" % (yea, mon))
    sum2 = cur2.fetchone()[0]
    sum3 = cur3.fetchone()[0]
    sum4 = cur4.fetchone()[0]
    sum5 = cur5.fetchone()[0]
    sum = (sum2 if sum2 != None else 0) - (sum3 if sum3 != None else 0) + (sum4 if sum4 != None else 0) - (
        sum5 if sum5 != None else 0)
    cur2.close()
    cur3.close()
    cur4.close()
    cur5.close()
    conn.close()
    # print('successfully fetch records!')
    return ret, sum

def queryStatistics(db='system.db'):
    """
    查询总收入、总支出、总借入、总借出、账户剩余
    返回：总收入、总支出、总借入、总借出、账户剩余
    """
    conn = sqlite3.connect(db)
    cur2 = conn.cursor()
    cur3 = conn.cursor()
    cur4 = conn.cursor()
    cur5 = conn.cursor()
    cur2.execute("select sum(number) from record where types= '收入'")
    cur3.execute("select sum(number) from record where types= '支出'")
    cur4.execute("select sum(number) from record where types= '借入'")
    cur5.execute("select sum(number) from record where types= '借出'")
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
    tot_remain = (0 if tot_income==None else tot_income)+(0 if tot_borrow==None else tot_borrow)-\
        (0 if tot_expenditure==None else tot_expenditure)-(0 if tot_lend==None else tot_lend)
    print(tot_income,tot_expenditure,tot_borrow,tot_lend,tot_remain)
    return (0 if tot_income==None else tot_income), \
        (0 if tot_expenditure==None else tot_expenditure), \
        (0 if tot_borrow==None else tot_borrow), \
        (0 if tot_lend==None else tot_lend), \
        tot_remain
    