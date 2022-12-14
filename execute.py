"""
该模块负责读入由sample_generator模块生成的样例列表，和一个目录路径，
对指定目录下的每一个cpp文件，调用编译器进行编译，并且执行传入样例列表每一个样例。
最后将目录下每一个文件对于每一个样例的运行结果进行打包并且以json字符串的格式返回。
"""
import subprocess
import json
import os
from hashlib import sha256
from config import timeout, use_hash


def execute(file_path, sample_list):
    """
    负责读入由sample_generator模块生成的样例列表，和一个目录路径，
    对指定目录下的每一个cpp文件，调用编译器进行编译，并且执行传入样例列表每一个样例。
    最后将目录下每一个文件对于每一个样例的运行结果进行打包并且以json字符串的格式返回。
    """
    output_list = []
    compile_result = subprocess.run(
        ['g++', file_path],
        text=True,
        stderr=subprocess.DEVNULL,
        check=False
    )
    for sample in sample_list:
        output = {}
        if compile_result.returncode == 0:
            try:
                if os.name == 'nt':
                    run_result = subprocess.run(
                        ['./a.exe'],
                        text=True,
                        input=sample,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        timeout=timeout,
                        check=False
                    )
                else:
                    run_result = subprocess.run(
                        ['./a.out'],
                        text=True,
                        input=sample,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        timeout=timeout,
                        check=False
                    )
                if run_result.returncode == 0:
                    output["status"] = "AC"
                    output["output"] = run_result.stdout
                    output["error"] = run_result.stderr
                else:
                    output["status"] = "RE"
                    output["output"] = run_result.stdout
                    output["error"] = run_result.stderr
            except subprocess.TimeoutExpired:
                output["status"] = "TLE"
                output["output"] = ""
                output["error"] = ""
        else:
            output["status"] = "CE"
            output["output"] = ""
            output["error"] = ""
        output_list.append(output)
    f_json = {}
    f_json["name"] = file_path
    output_str = json.dumps(output_list)
    if use_hash:
        f_json["output"] = sha256(output_str.encode('utf-8')).hexdigest()
    else: f_json["output"] = output_str
    return f_json
