import string
import unittest
from sample_generator import sample_generator

class TestSample(unittest.TestCase):
    def test_int(self):
        sample_num = 100
        result_list = sample_generator("test_sample_generator/test_int.txt", sample_num)
        self.assertEqual(len(result_list), sample_num)
        for result in result_list:
            data = result.split(" ")
            self.assertEqual(len(data), 3)
            self.assertEqual(data[-1], "\n")
            try:
                int_data1 = int(data[0])
                int_data2 = int(data[1])
            except:
                self.assertTrue(False)
            self.assertTrue(1 <= int_data1 and int_data1 <= 300 and 400 <= int_data2 and int_data2 <= 500)
            
    def test_string(self):
        sample_num = 100
        result_list = sample_generator("test_sample_generator/test_string.txt", sample_num)
        self.assertEqual(len(result_list), sample_num)
        for result in result_list:
            data = result.strip("\n")
            data = result.split(" ")
            self.assertEqual(len(data), 3)
            self.assertEqual(data[-1], "\n")
            str1, str2, _ = data
            for ch in str1:
                self.assertIn(ch, string.ascii_letters)
            for ch in str2:
                self.assertIn(ch, string.ascii_letters)
            self.assertTrue(3 <= len(str1) and len(str1) <= 20 and 21 <= len(str2) and len(str2) <= 40)

  
if __name__ == '__main__':
    unittest.main()