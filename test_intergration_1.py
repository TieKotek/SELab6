import os
import unittest
import json
from sample_generator import sample_generator
from execute import execute
from config import use_hash

pwd = os.getcwd()

class TestSample(unittest.TestCase):
    def test_int_add(self):
        sample_num = 10
        self.assertFalse(use_hash, "Please make sure you have disabled use_hash")
        path = os.path.join(pwd, "intergration_test1/case1")
        os.chdir(path)
        sample_list = sample_generator("stdin_format.txt", sample_num)
        expect_output = []
        for sample in sample_list:
            data = sample.split(" ")
            output = int(data[0]) + int(data[1])
            output = str(output)
            expect_output.append({
                "status": "AC",
                "output": output + "\n",
                "error": ""
            })
        expect = {
            "name": "add.cpp",
            "output": json.dumps(expect_output)
        }
        result = execute("add.cpp", sample_list)
        self.assertEqual(result, expect)
            
    def test_string_con(self):
        sample_num = 10
        self.assertFalse(use_hash, "Please make sure you have disabled use_hash")
        path = os.path.join(pwd, "intergration_test1/case2")
        os.chdir(path)
        sample_list = sample_generator("stdin_format.txt", sample_num)
        expect_output = []
        for sample in sample_list:
            data = sample.split(" ")
            output = data[0] + data[1]
            expect_output.append({
                "status": "AC",
                "output": output + "\n",
                "error": ""
            })
        expect = {
            "name": "string_con.cpp",
            "output": json.dumps(expect_output)
        }
        result = execute("string_con.cpp", sample_list)
        self.assertEqual(result, expect)
  
if __name__ == '__main__':
    unittest.main()