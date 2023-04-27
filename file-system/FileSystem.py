
class File:
    def __init__(self, name, isDir=False):
        self.name = name
        self.isDir = isDir # это папка или файл

    def get_name(self):
        return self.name


class FileSystem:

    def __init__(self):
        self.root = []

    # создаем папку
    def mkdir(self, path):
        f = File(path, True)
        self.root.append(f)

    def ls(self, dir):
        return [f.get_name() for f in self.root]

    def write_file(self, path, source):
        pass

    def read_file(self, path):
        pass


fs = FileSystem()
fs.mkdir("aaa")
fs.mkdir("xxx")
fs.mkdir("aaa/bbb")
print(fs.ls(""))

fs.mkdir("aaa/bbb")
fs.mkdir("aaa/ccc")
fs.mkdir("aaa/bbb/ccc2")
fs.mkdir("xxx")

# aaa
# ...bbb
# ......ccc2
# ...ccc
# xxx

print(fs.ls("aaa"))
# bbb
# ccc
print(fs.ls("aaa/bbb"))
# ccc2


fs.write_file("1.txt", "привет")
fs.write_file("aaa/1.txt", "Ярослав")
fs.write_file("aaa/bbb/1.txt", "Абрамов")

print(fs.read_file("aaa/1.txt"))
# Ярослав