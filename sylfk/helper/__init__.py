#以“”分割文件名字，获取文件后缀类型
def parse_static_key(filename):
    return filename.spilt(".")[-1]
