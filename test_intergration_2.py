import os
import unittest
import csv
from main import main

pwd = os.getcwd()

class TestSample(unittest.TestCase):
    def test_main(self):
        path = os.path.join(pwd, "intergration_test2")
        os.chdir(path)
        main()
        try:
            equal = open(os.path.join(path, "output/equal.csv"), "r", encoding="utf-8")
            inequal = open(os.path.join(path, "output/inequal.csv"), "r", encoding="utf-8")
            equal_list = list(csv.DictReader(equal))
            inequal_list = list(csv.DictReader(inequal))
            equal.close()
            inequal.close()
            for i in range(len(equal_list)):
                file1 = equal_list[i]["file1"]
                file2 = equal_list[i]["file2"]
                if file1 > file2:
                    equal_list[i] = file2 + " " + file1
                else:
                    equal_list[i] = file1 + " " + file2
            for i in range(len(inequal_list)):
                file1 = inequal_list[i]["file1"]
                file2 = inequal_list[i]["file2"]
                if file1 > file2:
                    inequal_list[i] = file2 + " " + file1
                else:
                    inequal_list[i] = file1 + " " + file2
            equal_list.sort()
            inequal_list.sort()
            expect_equal_list = [
                'input\\case1\\add2.cpp input\\case1\\add1.cpp',
                'input\\case1\\add2.cpp input\\case1\\add3.cpp',
                'input\\case1\\add1.cpp input\\case1\\add3.cpp',
                'input\\case2\\string_con1.cpp input\\case2\\string_con3.cpp'
            ]
            expect_inequal_list = [
                'input\\case1\\add1.cpp input\\case1\\add4.cpp',
                'input\\case1\\add2.cpp input\\case1\\add4.cpp',
                'input\\case1\\add3.cpp input\\case1\\add4.cpp',
                'input\\case2\\string_con1.cpp input\\case2\\string_con2.cpp',
                'input\\case2\\string_con2.cpp input\\case2\\string_con3.cpp'
            ]
            for i in range(len(expect_equal_list)):
                temp = expect_equal_list[i].split(" ")
                file1 = temp[0]
                file2 = temp[1]
                if file1 > file2:
                    expect_equal_list[i] = file2 + " " + file1
                else:
                    expect_equal_list[i] = file1 + " " + file2
            for i in range(len(expect_inequal_list)):
                temp = expect_inequal_list[i].split(" ")
                file1 = temp[0]
                file2 = temp[1]
                if file1 > file2:
                    expect_inequal_list[i] = file2 + " " + file1
                else:
                    expect_inequal_list[i] = file1 + " " + file2
            expect_equal_list.sort()
            expect_inequal_list.sort()
            self.assertEqual(equal_list, expect_equal_list)
            self.assertEqual(inequal_list, expect_inequal_list)

        except:
            self.assertTrue(False)
                
if __name__ == '__main__':
    unittest.main()