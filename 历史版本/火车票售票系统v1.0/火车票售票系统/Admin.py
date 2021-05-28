import random
def manager_login():
    check_number = str(random.randint(10000, 99999))
    input_name = input("请输入用户名：")
    input_passwd = input("请输入密码：")
    print('验证码[' + check_number + ']', end='')
    check_number_input = input('请输入验证码:')
    if check_number_input != check_number:
        print('验证码输入不正确！')
        return False
    if input_name == "admin" and input_passwd == "admin":
        print("登录成功！")
        return True
    return False
