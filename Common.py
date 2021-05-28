from User import *

opt_strs = [["查询列车信息", "管理员 登 录", "用 户  登 录", "用 户  注 册", "退        出"],
            ["查询列车信息", "添加列车信息", "删除列车信息", "修改列车信息", "退        出"],
            ["查询列车信息", "购        票", "退        票", "乘        车", "退        出"]]


def opt_screen(opt,opt_strs):
    opt_strs = opt_strs[opt]
    for i in range(len(opt_strs)):
        print("{:*<12} {}:{} {:*<12}".format("", i, opt_strs[i], ""))
    opt_str = input("请输入操作编号(0-{}:)".format(len(opt_strs) - 1))
    return opt_str


def manager_screen(opt_strs):
    while True:
        opt_str = opt_screen(1, opt_strs)
        # 管理员选择操作编号
        # 列车查询
        if opt_str == '0':
            train_query(selectAllTrain())
        elif opt_str == '1':
            # 列车信息添加
            train_info_add()

        elif opt_str == '2':
            # 列车信息删除
            statusCode = train_info_del()
            if statusCode:
                print("删除成功！")
            else:
                print("删除失败！")

        elif opt_str == '3':
            # 列车信息修改
            statusCode = train_info_update()
            if statusCode:
                print("修改成功！")
            else:
                print("修改失败！")
        elif opt_str == '4':
            print("退出...")
            return True
        else:
            print("输入错误，请重新输入!")


def user_screen(username,opt_strs):
    while True:
        # 打印用户钱包
        file = open("user.txt", 'r')
        file_read = file.readlines()
        file.close()
        for i in file_read:
            i = i.replace('\n', '')
            if i.split('\t')[0] == username:
                print("****************")
                print("用户 |  钱包额度")
                print(i.split('\t')[0]," |  ", i.split('\t')[2])

        opt_str = opt_screen(2,opt_strs)
        # 用户选择操作编号
        if opt_str == '0':
        # 列车查询
            train_query(selectAllTrain())
        elif opt_str == '1':
        # 购票
            if not sale_ticket(username):
                print("购买失败！")
        # 退票
        elif opt_str == '2':
            return_ticket(username)

        elif opt_str == '3':
            goTrain(username)

        elif opt_str == '4':
            print("退出...")
            return True
        else:
            print("输入错误，请重新输入!")


def train_query(traininfoList):
    print('输出列车信息')
    print('-------------------------------------------------------------------')
    print('车次' + '\t', '\t' + '时间' + '\t\t', '起始站' + '\t', '终点站' + '\t', '价格' + '\t', '数量')
    for i in traininfoList:
        # a = "ff"
        i = i.replace("\n", '')
        b = i.split('\t')
        print(b[0] + '\t', b[1] + '\t', b[2] + '\t', b[3] + '\t', b[4] + '\t' + b[5])
    print('--------------------train_query-----------------------------------------------')
    return True
