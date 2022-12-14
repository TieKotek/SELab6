"""
main模块是机器比对模块的主要模块，其负责遍历input文件夹下的每一个子目录
并且调用上述两个模块并且负责输出最后的equal.csv和inequal.csv
"""
import os
import csv
import time
from sample_generator import sample_generator
from execute import execute
from config import sample_num

def main():
    start = time.time()
    if not os.path.exists('./output'):
        os.mkdir('output')
    with open("./output/equal.csv", "w", encoding="utf-8") as equal:
        with open("./output/inequal.csv", "w", encoding="utf-8") as inequal:
            e_writer = csv.writer(equal)
            i_writer = csv.writer(inequal)
            e_writer.writerow(["file1", "file2"])
            i_writer.writerow(["file1", "file2"])
            pwd = os.getcwd()
            if os.path.exists('input'):
                for directory in os.listdir('input'):
                    if not os.path.isdir(os.path.join(pwd, 'input/' + directory)):
                        continue
                    sample_list = sample_generator(
                                    os.path.join(pwd, 'input/' + directory + '/stdin_format.txt'),
                                    sample_num
                                )
                    result_table  = []
                    print("Working on " + pwd +'/input/' + directory)
                    os.chdir(os.path.join(pwd, 'input/' + directory))
                    for f in os.listdir():
                        if f.endswith('.cpp'):
                            result_table.append(execute(f, sample_list))

                    for i in range(len(result_table)):
                        for j in range(i + 1, len(result_table)):
                            if result_table[i]["output"] == result_table[j]["output"]:
                                e_writer.writerow([
                                    os.path.join('input', directory, result_table[i]["name"]),
                                    os.path.join('input', directory, result_table[j]["name"])
                                ])
                            else:
                                i_writer.writerow([
                                    os.path.join('input', directory, result_table[i]["name"]),
                                    os.path.join('input', directory, result_table[j]["name"])
                                ])
            else:
                print("Please first create input directory!")
            equal.close()
            inequal.close()
    if os.name == 'nt':
        if os.path.exists("./a.exe"):
            os.remove("./a.exe")
    else:
        if os.path.exists("./a.out"):
            os.remove("./a.out")
    end = time.time()
    print("Done, it takes: ", round(end - start, 2), "s")


if __name__ == '__main__':
    main()
