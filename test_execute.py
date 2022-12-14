import unittest
import os 
from execute import execute
import json
from config import use_hash

pwd = os.getcwd()

class TestExecute(unittest.TestCase):
    def test_add(self):
        self.assertFalse(use_hash, "Please make sure you have disabled use_hash")
        path = os.path.join(pwd, "test_execute")
        os.chdir(path)
        sample_list = [
            "13 25",
            "26 70",
            "100 129",
            "0 20",
        ]
        result = execute("add.cpp", sample_list)
        expect_output = [
            {
                "status": "AC",
                "output": "38\n",
                "error": ""
            },
            {
                "status": "AC",
                "output": "96\n",
                "error": ""
            },
            {
                "status": "AC",
                "output": "229\n",
                "error": ""
            },
            {
                "status": "AC",
                "output": "20\n",
                "error": ""
            }
        ]
        expect = {
            "name": "add.cpp",
            "output": json.dumps(expect_output)
        }
        self.assertEqual(result, expect)

    def test_string_con(self):
        self.assertFalse(use_hash, "Please make sure you have disabled use_hash")
        path = os.path.join(pwd, "test_execute")
        os.chdir(path)
        sample_list = [
            "aljkdfal adfafd",
            "12 70",
            "kkk kk",
            "0 20",
        ]
        result = execute("string_con.cpp", sample_list)
        expect_output = [
            {
                "status": "AC",
                "output": "aljkdfaladfafd\n",
                "error": ""
            },
            {
                "status": "AC",
                "output": "1270\n",
                "error": ""
            },
            {
                "status": "AC",
                "output": "kkkkk\n",
                "error": ""
            },
            {
                "status": "AC",
                "output": "020\n",
                "error": ""
            }
        ]
        expect = {
            "name": "string_con.cpp",
            "output": json.dumps(expect_output)
        }
        self.assertEqual(result, expect)

    def test_compile_error(self):
        self.assertFalse(use_hash, "Please make sure you have disabled use_hash")
        path = os.path.join(pwd, "test_execute")
        os.chdir(path)
        sample_list = [
            "13 25",
            "26 70",
            "100 129",
            "0 20",
        ]
        result = execute("compile_error.cpp", sample_list)
        expect_output = [
            {
                "status": "CE",
                "output": "",
                "error": ""
            },
            {
                "status": "CE",
                "output": "",
                "error": ""
            },
            {
                "status": "CE",
                "output": "",
                "error": ""
            },
            {
                "status": "CE",
                "output": "",
                "error": ""
            },
        ]
        expect = {
            "name": "compile_error.cpp",
            "output": json.dumps(expect_output)
        }
        self.assertEqual(result, expect)

    def test_TLE(self):
        self.assertFalse(use_hash, "Please make sure you have disabled use_hash")
        path = os.path.join(pwd, "test_execute")
        os.chdir(path)
        sample_list = [
            "13 25",
            "26 70",
            "100 129",
            "0 20",
        ]
        result = execute("TLE.cpp", sample_list)
        expect_output = [
            {
                "status": "TLE",
                "output": "",
                "error": ""
            },
            {
                "status": "TLE",
                "output": "",
                "error": ""
            },
            {
                "status": "TLE",
                "output": "",
                "error": ""
            },
            {
                "status": "TLE",
                "output": "",
                "error": ""
            },
        ]
        expect = {
            "name": "TLE.cpp",
            "output": json.dumps(expect_output)
        }
        self.assertEqual(result, expect)

    def test_quick_sort(self):
        self.assertFalse(use_hash, "Please make sure you have disabled use_hash")
        path = os.path.join(pwd, "test_execute")
        os.chdir(path)
        sample_list = [
            "4\n7 4 5 3",
            "10\n10 9 8 7 6 5 4 3 2 1",
            "3\n2 4 5",
            "1\n1",
        ]
        result = execute("quick_sort.cpp", sample_list)
        expect_output = [
            {
                "status": "AC",
                "output": "3 4 5 7 ",
                "error": ""
            },
            {
                "status": "AC",
                "output": "1 2 3 4 5 6 7 8 9 10 ",
                "error": ""
            },
            {
                "status": "AC",
                "output": "2 4 5 ",
                "error": ""
            },
            {
                "status": "AC",
                "output": "1 ",
                "error": ""
            }
        ]
        expect = {
            "name": "quick_sort.cpp",
            "output": json.dumps(expect_output)
        }
        self.assertEqual(result, expect)

    def test_RE(self):
        self.assertFalse(use_hash, "Please make sure you have disabled use_hash")
        path = os.path.join(pwd, "test_execute")
        os.chdir(path)
        sample_list = [
            "13 25",
            "26 70",
            "100 129",
            "0 20",
        ]
        result = execute("RE.cpp", sample_list)
        expect_output = [
            {
                "status": "RE",
                "output": "",
                "error": ""
            },
            {
                "status": "RE",
                "output": "",
                "error": ""
            },
            {
                "status": "RE",
                "output": "",
                "error": ""
            },
            {
                "status": "RE",
                "output": "",
                "error": ""
            }
        ]
        expect = {
            "name": "RE.cpp",
            "output": json.dumps(expect_output)
        }
        self.assertEqual(result, expect)

if __name__ == '__main__':
    unittest.main()