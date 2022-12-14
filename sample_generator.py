"""
一个用于随机生成样例的模块。
"""
import re
import string
import random

def sample_generator(path, num):
    """
    该函数读入一个文件路径（包含stdin_format.txt）和期待的生成样例数量
    最后返回一个包含了num个符合stdin_format.txt要求的随机样例的列表。
    """
    output_list = []
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
        file.close()
        lines = content.split("\n")
        for _ in range(num):
            output = ""
            for line in lines:
                types = line.split()
                for type_pattern in types:
                    if type_pattern.startswith("int"):
                        pattern = re.compile(r'[(](.*?)[)]', re.S)
                        info = re.findall(pattern, type_pattern)[0]
                        args = info.split(",")
                        output += str(random.randint(int(args[0]), int(args[1])))

                    elif type_pattern.startswith("string"):
                        pattern = re.compile(r'[(](.*?)[)]', re.S)
                        info = re.findall(pattern, type_pattern)[0]
                        args = info.split(",")
                        length = random.randint(int(args[0]), int(args[1]))
                        for _ in range(length):
                            output += random.choice(string.ascii_letters)
                    else:
                        output += random.choice(string.ascii_letters)
                    output += " "
                output += "\n"
            output_list.append(output)
    return output_list
