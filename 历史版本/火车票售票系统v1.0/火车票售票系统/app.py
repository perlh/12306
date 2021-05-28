from Common import *
from Admin import *


# 主界面
def main_screen():
    while True:
        opt_str = opt_screen(0, opt_strs)
        # 用户选择操作编号
        if opt_str == '0':
            # 查看列车信息
            trainInfo = selectAllTrain()
            train_query(trainInfo)
        elif opt_str == '1':
            if manager_login():
                manager_screen(opt_strs)
            else:
                print("登录失败，账号或者密码错误！")
        elif opt_str == '2':
            username = userLogin()
            if username:
                user_screen(username, opt_strs)
            else:
                print("登录失败，账号或者密码错误！")
        elif opt_str == '3':
            userRegister()
        elif opt_str == '4':
            print("退出...")
            return True
        else:
            print("输入错误，请重新输入!")
            # return True


if __name__ == '__main__':
    main_screen()



