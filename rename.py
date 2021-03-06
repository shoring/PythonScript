# -*- coding: UTF  -*-

import sys, getopt, os, re

#路径分隔符
fix = '\\' if sys.platform == 'win32' else '/' 

opts, args = getopt.getopt(sys.argv[1:], "hd:p:r:m:t") 

path, pattern, replacePattern, mode, isTest = "", "", "", 0, False

for opt, arg in opts:
    if opt == "-d":
        path = arg
        if not re.match('.+\\' + fix + '$', path):
            path += fix
    if opt == "-p":
        pattern = arg
    if opt == "-r":
        replacePattern = arg
    if opt == "-m":
        mode = int(arg)
    if opt == "-t":
        isTest = True
    if opt == "-h": 
        print(u"-d:  目录")
        print(u"-p:  正则表达式，()代表group")
        print(u"-r:  替换表达式，group(n)")
        print(u"-m:  重命名模式，默认为0。(0：采用group全部替换模式，1：直接采用sub替换掉匹配到字符）")
        print(u"-t:  是否测试")
        print(u"-h:  帮助")
        print(r"例:  python rename.pyw -d directory|filepath -p .+(\d{4}).*?(.txt) -r Test{1}{2}")
        exit()

print(path)
exit()
dirs = os.listdir(path)

for dir in dirs:
    replaceText = replacePattern
    success = False
    if mode == 0:
        match = re.match(pattern, dir)
        if match:
            success = True
            groupIndexs = re.findall(r'\{(\d)\}', replacePattern)
            if groupIndexs:
                for index in groupIndexs:
                    replaceText = replaceText.replace("{" + index + "}", match.group(int(index)))
    elif mode == 1:
        success = True
        replaceText = re.sub(pattern, replaceText, dir)

    if isTest:
        print(replaceText)
    elif success:
        print("rename " + dir + "...")
        os.rename(path + dir, path + replaceText)
print("Done!")
