while True:
    tmp = input("请输入温度：(输入q退出)")
    if tmp == 'q':
        break
    if tmp[-1] == 'f':
        temperature = eval(tmp[0:-1])*1.8+32
        print("您输入的是华氏温度，转换成摄氏温度为：",temperature)
    elif tmp[-1] == 't':
        temperature = (eval(tmp[0:-1])-32)/1.8
        print("您输入的是摄氏温度，转换成华氏温度为：",temperature)
    else :
        print("请输入标准格式！")
