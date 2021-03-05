import sys

print("百宝箱")
print("版本：4.0")
print("功能：\n1.温度转换\n2.圆面积计算\n3.分数工具\n4.算式成立检测\n5.网站解析\n6.进制转换\n7.平年和闰年")
w = float(input("请选择功能（填序号）："))
if w > 7:  # 判断序号是否正常
    print("⚠错误：序号不能超过4！\n终止程序！")
    input("按任意键退出")
    sys.exit()
if w == 1:
    print("温度转换")
    c = float(input("请输入摄氏度："))
    
    f = (c * 9 / 5) + 32
    print("转换后华氏度为：", f)
    input("按任意键退出")
if w == 2:
    print("圆面积计算")
    r = float(input("r:"))
    x = r ** 2 * 3.14
    print("S=", x)
    input("按任意键退出")
if w == 3:
    print("分数工具")
    a = float(input(">"))
    if a == 0:
        print("⚠错误：分子不能为0！")
        print("终止程序！")
        sys.exit()
    print("_____")
    b = float(input(">"))
    if b == 0:
        print("⚠错误：分母不能为0！")
        print("终止程序！")
        sys.exit()
    print("小数为：", a / b)
    print("百分数为：", a / b * 100, "%")  # 温度转换公式
    if a > b:
        print("分数类型：假分数")
        input("按任意键退出")
        sys.exit()
    elif a == b:
        print("分数类型：假分数")
        input("按任意键退出")
        sys.exit()
    else:
        print("分数类型：真分数")
        input("按任意键退出")
        sys.exit()
if w == 4:
    print("算式成立检测")
    z = float(input(">"))
    f = float(input("+/-/×/÷\n1/2/3/4\n>"))
    if f == 1:
        x = float(input("+>"))
        y = z+x
        a = float(input("=>"))
        if a == y:
            print("成立")
        else:
            print("不成立\n正解：")
            # print('%f+%f=%f' % (z, x, y))  # print(z+"+"+x+"+"+y)
            print('{}+{}={}'.format(z, x, y))
            input("按任意键退出")
            sys.exit
    elif f == 2:
        x = float(input("->"))
        y = z-x
        a = float(input("=>"))
        if a == y:
            print("成立")
        else:
            print("不成立\n正解：")
            # print('%f-%f=%f' % (z, x, y))  # print(z+"-"+x+"+"+y)
            print('{}-{}={}'.format(z, x, y))
            input("按任意键退出")
            sys.exit
    elif f == 3:
        x = float(input("×>"))
        y = z*x
        a = float(input("=>"))
        if a == y:
            print("成立")
        else:
            print("不成立\n正解：")
            # print('%f×%f=%f' % (z, x, y))  # print(z+"×"+x+"+"+y)
            print('{}×{}={}'.format(z, x, y))
            input("按任意键退出")
            sys.exit
    else:
        x = float(input("÷>"))
        y = z/x
        a = float(input("=>"))
        if a == y:
            print("成立")
        else:
            print("不成立\n正解：")
            # print('%f÷%f=%f' % (z, x, y))  # print(z+"÷"+x+"+"+y)
            print('{}÷{}={}'.format(z, x, y))
            input("按任意键退出")
            sys.exit
if w == 5:
    print("网站解析")
    import requests

    a = input(str("网址:"))
    h = {
        'User-Anget': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'}  # 头部信息
    b = 'http://'+a

    response = requests.get(b, headers=h)
    #response = requests.get(b)
    print("\n\n\n连接状态："+str(response.status_code))
    print("\n网址："+str(response.url))
    print("\n头部信息："+str(response.headers))
    print("\ncookie信息:"+str(response.cookies))
    print("\n网页源代码：\n"+str(response.text))
if w == 6:
    b = int(input("DEC>"))
    c = str((bin(b)))
    d = str(hex(b))
    e = str(oct(b))
    print("HEX:%s,BIN:%s,OCT:%s" % (d, c, e))
if w == 7:
    a = float(input("年份："))
    b = a % 4
    if b == 0:
        print("闰年")
    else:
        print("平年")
