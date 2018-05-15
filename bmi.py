while 1:
    test = eval(input("查询bmi值请输入1,退出请输入0:"))
    if test == 0:
        break
    weight = eval(input("请输入体重："))
    height = eval(input("请输入身高："))

    bmi = weight / (height**2)
    print("您的BMI值是",bmi,"属于：")

    if bmi<18.5:
        print("偏瘦")
    elif bmi <25:
        print("正常")
    elif bmi <30:
        print("偏胖")
    else:
        print("肥胖")
