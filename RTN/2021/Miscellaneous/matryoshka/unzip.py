from zipfile import ZipFile

filename = 'file.zip'
password = 'code.txt'

for i in range(0, 101):
    with ZipFile(filename) as zf:
        with open(password) as f:
            zf.extractall(str(i), pwd = bytes(eval(f.readline())))
            filename = str(i) + '/file.zip'
            password = str(i) + '/code.txt'