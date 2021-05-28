# User.py
import random
from Train import *
import time


def getUserList():
    userList = []
    file = open("user.txt", "r")
    readfile = file.readlines()
    file.close()
    for i in readfile:
        i = i.replace('\n', '')
        user = i.split("\t")[0]
        userList.append(user)
    return userList


def getUserInfo():
    file = open("user.txt", "r")
    readfile = file.readlines()
    file.close()
    userInfoList = []
    for i in readfile:
        i = i.replace('\n', '')
        user = i.split("\t")[0]
        passwd = i.split("\t")[1]
        all = [user, passwd]
        userInfoList.append(all)
    return userInfoList


# 买票
def sale_ticket(username):
    id = input('请输入要购买的车次：')
    # 查询是否存在这个车次
    if checkId(id):
        # 检查是否购买过这个车票
        file1 = open("sale_info.txt", 'r')
        readfile1 = file1.readlines()
        file1.close()
        for i in readfile1:
            i1 = i.replace('\n', '')
            b3 = i1.split('\t')
            if b3[0] == username and b3[2] == id:
                print("该用户已经购买过这个车次的车票！")
                return False


        # print("----------------text1-----")
        # 得到这个车次的票价
        price = 0
        trains = open("trains.txt", 'r')
        trains_list = trains.readlines()
        trains.close()
        for i in trains_list:
            # print(i)
            xx1 = i.replace('\n','')

            xx2 = xx1.split('\t')
            if xx2[0] == id:
                price = float(xx2[4])
                # 如果没票了，那么就返回False
                if int(xx2[5]) == 0:
                    print("没票了~")
                    return False
                # print(price)
                break
        # print("----------------text2-----")
        # 先判断这个用户有没有钱买票
        myInfo1 = open("user.txt", "r")
        myInfo = myInfo1.readlines()
        myInfo1.close()
        for i in myInfo:
            tmp_i = i.replace("\n",'')
            tmp_i_1 = tmp_i.split('\t')
            if tmp_i_1[0] == username and tmp_i_1[1] == id:
                money = int(tmp_i_1[2]) - price
                if money < 0:
                    print("没钱买票！")
                    return False
        # print("----------------text3-----")
        # 买票过程开始！！！
        # 先将火车余票减1，并且返回购票的车次信息train_info1
        train_info1 = train_info_update_number_by_code(id, 0)
        train_info1 = train_info1.replace("\n", '')
        train_info = train_info1.split('\t')
        # print(train_info)
        # 如果火车余票减1执行成功
        if train_info1:
            # 有钱买票，则更新用户文件
            myInfoFile2 = open("user.txt", "w")
            # 从之前的文件中行行遍历
            for i in myInfo:
                tmp_i = i.replace('\n','')
                tmp_i_1 = tmp_i.split('\t')
                # print(i)
                if tmp_i_1[0] == username:
                    # print("test5")
                    money = float(tmp_i_1[2]) - price
                    i = tmp_i_1[0] + '\t' + tmp_i_1[1] + '\t' + str(money) + '\t\n'
                    # print(i)
                    myInfoFile2.writelines(i)
                    continue
                myInfoFile2.writelines(i)
            myInfoFile2.close()
            # print("test4")
            # 添加到已购文件中
            file = open("sale_info.txt", 'a')
            # 购票时间
            datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            # 要存储的用户信息
            info = username + '\t' + datetime + '\t' + train_info[0] + "\t" + train_info[1] + "\t" + train_info[
                2] + "\t" + train_info[3] + "\t" + train_info[4] + "\t\n"
            file.writelines(info)
            file.close()
            print("购买成功！")
            return True
        else:
            print("购票发生未知错误！")
            return False
    else:
        print("不存在这个车次")
        return False


# 注册
def userRegister():
    print("***用户注册***\n要求 : 密码长度>6")
    user = input('请输入用户名:')
    passwd = input('请输入密码:')
    passwd1 = input('请再次输入密码：')
    money = input("请输入钱包额度：")

    # 检查输入的金额是否是数字
    try:
        int(money)
    except Exception as e:
        print(e)
        print("钱包额度输入错误，请输入数字。。。")
        return False

    # 检车输入密码是否相同
    if passwd1 != passwd:
        print("注册用户失败\t两次输入密码不相同！")
        return False

    checkCode = random.randint(10000, 90000)
    checkCode1 = input("验证码：【{0}】\n请输入验证码:".format(checkCode))
    if int(checkCode1) != checkCode:
        print("验证码输入不成功！")
        return False
    userList = getUserList()
    if user in userList:
        print('该用户名已被注册，请重新输入！')
        return False
    else:
        fo = open("user.txt", "a+")
        userinfo = user + '\t' + passwd + '\t' + money + '\t\n'
        fo.write(userinfo)
        fo.close()
        print("注册成功")
        return True


# 用户登录
def userLogin():
    checkCode = str(random.randint(10000, 99999))
    input_name = input("请输入用户名：")
    input_passwd = input("请输入密码：")
    print('验证码[' + checkCode + ']', end='')
    check_number_input = input('请输入验证码:')
    if check_number_input != checkCode:
        print('验证码输入不正确！')
        return False
    userList = getUserList()
    if len(userList) == 0:
        print("用户空信息")
        return False
    if input_name in userList:
        userinfo = getUserInfo()

        for i in userinfo:
            if i[0] == input_name and i[1] == input_passwd:
                print("登录成功！")
                return input_name
        return False
    return False


# 退票
def return_ticket(username):
    # 读取买票信息
    file = open("sale_info.txt", 'r')
    readfile = file.readlines()
    file.close()
    # 打印我的购票信息
    print('我的车票：')
    print("姓名\t购买日期\t车次\t发车时间\t起始站\t终点站\t票价")
    for i in readfile:
        i1 = i.replace('\n', '')
        b2 = i1.split('\t')
        if b2[0] == username:
            print(i)
    while True:
        return_ticket_id = input('请输入要退车票的车次(输入q退出)：')
        if return_ticket_id == 'q' or return_ticket_id == 'Q':
            # 返回到用户选择菜单
            return False

        file = open("sale_info.txt", 'r')
        readSaleInfo = file.readlines()
        file.close()
        # 标志位
        flag = 0
        # 查找是否存在这个车次
        for j in readSaleInfo:
            i1 = j.replace("\n", "")
            b = i1.split('\t')
            if b[2] == return_ticket_id and b[0] == username:
                flag = 1
        if flag == 0:
            print("数据库中不存在该车次！")
            return False


        # 得到这个车次的票价
        price = 0
        trains = open("trains.txt", 'r')
        trains_list = trains.readlines()
        # print(trains_list)
        trains.close()
        for i in trains_list:
            xx1 = i.replace('\n', '')
            xx2 = xx1.split('\t')
            if xx2[0] == return_ticket_id:
                price = float(xx2[4])
        # 更新用户钱包
        file_user = open("user.txt","r")
        myInfo = file_user.readlines()
        file_user.close()
        myInfoFile2 = open("user.txt",'w')
        for i in myInfo:
            tmp_i = i.replace('\n', '')
            tmp_i_1 = tmp_i.split('\t')
            # print(i)
            if tmp_i_1[0] == username:
                # print("test5")
                money = float(tmp_i_1[2]) + price
                i = tmp_i_1[0] + '\t' + tmp_i_1[1] + '\t' + str(money) + '\t\n'
                # print(i)
                myInfoFile2.writelines(i)
                continue
            myInfoFile2.writelines(i)
        myInfoFile2.close()
        # 删除购票信息
        file = open("sale_info.txt", "w")
        for i in readSaleInfo:
            i1 = i.replace("\n", "")
            b = i1.split('\t')
            if b[0] == username and b[2] == return_ticket_id:
                continue
            file.writelines(i)
        file.close()
        info = train_info_update_number_by_code(return_ticket_id, 1)
        # print(info)
        if info:
            print("退票成功！")
            return True
        else:
            print("退票失败！")
            return False


# 乘车
def goTrain(username):
    # 读取买票信息
    file = open("sale_info.txt", 'r')
    readfile = file.readlines()
    # 打印我的购票信息
    print('我的车票：')
    print("姓名\t购买日期\t车次\t发车时间\t起始站\t终点站\t票价")
    for i in readfile:
        i1 = i.replace('\n', '')
        b2 = i1.split('\t')
        if b2[0] == username:
            print(i)
    while True:
        return_ticket_id = input('请输入要乘坐的车次(输入q退出)：')
        if return_ticket_id == 'q' or return_ticket_id == 'Q':
            # 返回到用户选择菜单
            return False
        file = open("sale_info.txt", 'r')
        readSaleInfo = file.readlines()
        file.close()
        # 检查文件中是否存在那个车次
        flag = 0  # 标志位
        # 查找是否存在这个车次
        for j in readSaleInfo:
            i1 = j.replace("\n", "")
            b = i1.split('\t')
            if b[2] == return_ticket_id and b[0] == username:
                flag = 1
        if flag == 0:
            print("数据库中不存在该车次！")
            return False

        """
        将之前文件的文件一行一行地写到trains.txt文件中，
        当写文件到要目标车次这一行信息时，就不写这一行到文件，执行下一行写入文件，
        并且会将之前保存的文件覆盖。
        """

        file = open("sale_info.txt", "w")
        for i in readSaleInfo:
            i1 = i.replace("\n", "")
            b = i1.split('\t')
            if b[0] == username and b[2] == return_ticket_id:
                continue
            file.writelines(i)
        file.close()
        print("乘坐成功！已经乘坐{0}车次！".format(return_ticket_id))
        return True
