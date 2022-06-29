#!/usr/bin/env Python
# coding=utf-8
import unittest
from unittest.mock import patch

import data_operate
from data_operate import addDataNameAndPassword, addDataRecord, deleteDataRecord, \
    selectPassword, updateData, queryLimitRecords, queryStatistics


class MyTestCase(unittest.TestCase):
    def test_addDataNameAndPassword(self):
        print('\n')
        data_operate.createNameAndPassword()
        self.assertEqual(addDataNameAndPassword('张三', '123456'), True)
        self.assertEqual(addDataNameAndPassword('', ''), False)
        self.assertEqual(addDataNameAndPassword('', '111111'), False)
        self.assertEqual(addDataNameAndPassword('李四', ''), False)
        self.assertEqual(addDataNameAndPassword('李四', '111111'), True)
        self.assertEqual(addDataNameAndPassword('张三', '111111'), False)
        self.assertEqual(addDataNameAndPassword('张三', '123456'), False)
        self.assertEqual(addDataNameAndPassword('王五', '233233'), True)

    def test_addDateRecord(self):
        print('\n')
        data_operate.createRecord()
        self.assertEqual(addDataRecord("张三", "2022", "06", "18", "支出", "食品", "拉面店", 30), True)
        self.assertEqual(addDataRecord("张三", "2022", "06", "18", "支出", "食品", "拉面店", 30), True)
        self.assertEqual(addDataRecord("张三", "2022", "06", "18", "支出", "食品", "拉面店", "30"), False)
        self.assertEqual(addDataRecord("张三", "2022", "06", "18", "支出", "食品", "拉面店", -30), True)
        self.assertEqual(addDataRecord("张三", "2022", "06", "19", "借入", "家具", "李四", 1000), True)
        self.assertEqual(addDataRecord("李四", "2022", "06", "20", "借出", "家具", "张三", 1000), True)
        self.assertEqual(addDataRecord("张三", "2022", "05", "15", "支出", "管理费", "王五", 200), True)
        self.assertEqual(addDataRecord("张三", "2022", "04", "12", "支出", "办公用品", "商场", 200), True)
        self.assertEqual(addDataRecord("张三", "2021", "07", "02", "借出", "彩礼", "王五", 5000), True)
        self.assertEqual(addDataRecord("张三", "2022", "06", "20", "收入", "营业额", "用户", 20000), True)
        self.assertEqual(addDataRecord("张三", "2022", "06", "30", "支出", "维修费", "李四", 500), True)
        self.assertEqual(addDataRecord("李四", "2022", "06", "30", "收入", "维修费", "张三", 500), True)
        self.assertEqual(addDataRecord("王五", "2022", "05", "15", "收入", "管理费", "张三", 200), True)
        self.assertEqual(addDataRecord("王五", "2021", "07", "02", "借入", "彩礼", "张三", 5000), True)

    def test_deleteDataRecord(self):
        print('\n')
        self.assertEqual(deleteDataRecord("张三", "2022", "06", "18", "支出", "食品", "拉面店", -30), True)
        self.assertEqual(deleteDataRecord("张三", "2022", "06", "18", "支出", "食品", "拉面店", -30), False)
        self.assertEqual(deleteDataRecord("", "", "", "", "", "", "", 30), False)

    def test_selectPassword(self):
        print('\n')
        self.assertEqual(selectPassword("张三")[0], '123456')
        self.assertEqual(selectPassword("李四")[0], '111111')
        self.assertEqual(selectPassword("王五")[0], '233233')
        self.assertEqual(selectPassword("赵六")[0], '')

    def test_updateData(self):
        print('\n')
        self.assertEqual(updateData('张三', '123456'), True)

    def test_queryLimitRecords(self):
        print('\n')
        self.assertEqual(queryLimitRecords('2022', '全年', '张三')[1], 20040)
        self.assertEqual(queryLimitRecords('2022', '06', '张三')[1], 20440)
        self.assertEqual(queryLimitRecords('2022', '05', '张三')[1], -200)
        self.assertEqual(queryLimitRecords('2021', '全年', '张三')[1], -5000)
        self.assertEqual(queryLimitRecords('2021', '07', '张三')[1], -5000)
        self.assertEqual(queryLimitRecords('2021', '07', '王五')[1], 5000)
        self.assertEqual(queryLimitRecords('2022', '全年', '李四')[1], -500)
        self.assertEqual(queryLimitRecords('2022', '06', '李四')[1], -500)
        self.assertEqual(queryLimitRecords('2021', '全年', '李四')[1], 0)

    def test_queryStatistics(self):
        print('\n')
        result = queryStatistics('张三')
        self.assertEqual(result[0], 20000)
        self.assertEqual(result[1], 960)
        self.assertEqual(result[2], 1000)
        self.assertEqual(result[3], 5000)
        self.assertEqual(result[4], 15040)
        result = queryStatistics('张三', '2022')
        self.assertEqual(result[0], 20000)
        self.assertEqual(result[1], 960)
        self.assertEqual(result[2], 1000)
        self.assertEqual(result[3], 0)
        self.assertEqual(result[4], 20040)
        result = queryStatistics('张三', '-1')
        self.assertEqual(result[0], 20000)
        self.assertEqual(result[1], 960)
        self.assertEqual(result[2], 1000)
        self.assertEqual(result[3], 5000)
        self.assertEqual(result[4], 15040)
        result = queryStatistics('张三', '2021')
        self.assertEqual(result[0], 0)
        self.assertEqual(result[1], 0)
        self.assertEqual(result[2], 0)
        self.assertEqual(result[3], 5000)
        self.assertEqual(result[4], -5000)
        result = queryStatistics('李四')
        self.assertEqual(result[0], 500)
        self.assertEqual(result[1], 0)
        self.assertEqual(result[2], 0)
        self.assertEqual(result[3], 1000)
        self.assertEqual(result[4], -500)
        result = queryStatistics('李四', '2021')
        self.assertEqual(result[0], 0)
        self.assertEqual(result[1], 0)
        self.assertEqual(result[2], 0)
        self.assertEqual(result[3], 0)
        self.assertEqual(result[4], 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
    suite = unittest.TestSuite()
    test = unittest.defaultTestLoader.loadTestsFromModule(MyTestCase)
    suite.addTests(test)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
