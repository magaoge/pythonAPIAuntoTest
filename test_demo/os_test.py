import os, inspect

def load_file1():
    # 获取当前文件路径,必须是文件路径，不能是文件夹路径，如果不填，默认为当前模块所在的绝对路径
    current_path = os.path.abspath("token_setter.py")
    # 获取当前文件的父目录
    # os.path.sep是指安装当前的系统，自适应文件夹分隔符
    father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")

    print(current_path)
    print(father_path)


def load_file2():
    # 获取当前文件路径
    current_path = inspect.getfile(inspect.currentframe())
    # 获取当前文件所在目录，相当于当前文件的父目录
    dir_name = os.path.dirname(current_path)
    # 转换为绝对路径
    file_abs_path = os.path.abspath(dir_name)
    # 划分目录
    # os.path.split('PATH')
    # 1.PATH指一个文件的全路径作为参数：
    # 2.如果给出的是一个目录和文件名，则输出路径和文件名
    # 3.如果给出的是一个目录名，则输出路径和为空文件名
    # 4.返回的数据类型是一个元祖
    list_path = os.path.split(file_abs_path)

    print(dir_name)
    print('list_path:' + str(list_path))


if __name__ == '__main__':
    load_file2()

