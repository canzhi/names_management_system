# -*- coding:utf-8 -*-

# 声明一个列表，用来存储用户名。
users = []

# 1.打印功能提示
print("*" * 20)
print("   用户管理系统v0.0")
print("*" * 20)
print(" 1.添加一个用户")
print(" 2.删除一个用户")
print(" 3.修改一个用户")
print(" 4:查询一个用户")
print(" 5:退出")
print("*" * 20)

while True:
    # 2.获取用户的选择
    num = int(input("请输入您的功能需求："))

    # 3.根据用户的选择，执行相应的功能
    if num == 1:
        user_name = input("请输入要添加的用户名：")
        users.append(user_name)
        print(user_name)
    elif num == 2:
        user_name = input("请输入要删除的用户名：")
        users.remove(user_name)
    elif num == 3:
        user_name = input("请输入要旧的用户名：")
        users.remove(user_name)
        user_name = input("请输入要修改为的用户名：")
        users.append(user_name)
    elif num == 4:
        user_name = input("请输入要查询的用户名：")
        if user_name in users:
            print("用户存在")
        else:
            print("用户不存在")
    elif num == 5:
        break
    else:
        print("您的输入有误，请重新输入!")
