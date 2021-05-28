def selectAllTrain():
    try:
        # 尝试打开文件，并且返回读取后的文件信息
        file = open("trains.txt", "r")
        result = file.readlines()
        file.close()
        return result
    except Exception as e:
        # 文件要是打开失败，则打印报错信息
        print(e)
        return


def addTrain(id, dateTime, startStation, endStation, prise, number):
    info = id + '\t' + dateTime + '\t' + startStation + '\t' + endStation + '\t' + prise + '\t' + number + '\t\n'
    try:
        file = open("trains.txt", "a")
        file.writelines(info)
        file.close()
        return True
    except Exception as e:
        print(e)
        return False


def delTrain(id):
    # 按车次删除火车信息
    try:
        file = open("trains.txt", "r")
        tmpRead = file.readlines()
        file.close()
        file = open("trains.txt", "w")
        for i in tmpRead:
            if id in i:
                continue
            file.writelines(i)
        file.close()
        print("删除成功")
        return True
    except Exception as e:
        print(e)
        return False


def train_info_add():
    # 添加列车信息
    id = input('列表车次：')
    start_time = input('发车时间：')
    start_station = input('起始站：')
    end_station = input('终点站：')
    price = input('价格：')
    number = input('票数:')
    # 检查车次是否已经存在
    allTrainInfo = selectAllTrain()
    if allTrainInfo:
        for i in allTrainInfo:
            if id == i.split('\t')[0]:
                print("列车已经存在")
                return False
    if id and start_station and start_time and end_station and price and number:
        tmpCode = addTrain(id, start_time, start_station, end_station, price, number)
    else:
        print("输入信息存在为空！添加失败！")
        return False
    if tmpCode:
        print("添加成功")
        return True
    else:
        print("添加失败！")
        return False


def train_info_update():
    # 修改列车信息
    id = input('请输入要修改的列表车次：')
    allTrain = selectAllTrain()
    file = open("trains.txt", "w")
    # 标志位
    flag = 0
    # 查找是否存在这个车次
    for j in allTrain:
        i1 = j.replace("\n", "")
        b = i1.split('\t')
        if b[0] == id:
            flag = 1
    if flag == 0:
        print("数据库中不存在该车次！")
        return False

    for i in allTrain:
        i1 = i.replace("\n", "")
        b = i1.split('\t')
        if b[0] == id:
            print("查找成功！请修改:\n")
            start_time = input('发车时间：')
            start_station = input('起始站：')
            end_station = input('终点站：')
            price = input('价格：')
            number = input('票数:')
            i = b[0] + '\t' + start_time + '\t' + start_station + '\t' + end_station + '\t' + price + '\t' + number + '\t\n'
        file.writelines(i)
    file.close()
    return True


def train_info_update_number_by_code(id_sale, code):
    # code为0 自减，否则增
    allTrain = selectAllTrain()
    # 标志位
    flag = 0
    # 查找是否存在这个车次
    for j in allTrain:
        i1 = j.replace("\n", "")
        b = i1.split('\t')
        if b[0] == id_sale:
            flag = 1
    if flag == 0:
        print("数据库中不存在该车次！")
        return False
    file = open("trains.txt", "w")
    for i in allTrain:
        flag = 0
        i1 = i.replace("\n", "")
        b1 = i1.split('\t')
        if b1[0] == id_sale:
            start_time = b1[1]
            start_station = b1[2]
            end_station = b1[3]
            price = b1[4]
            if code == 0:
                if int(b1[5]) == 0:
                    flag = 1
                    number = b1[5]
                else:
                    number = str(int(b1[5]) - 1)
            else:
                number = str(int(b1[5]) + 1)
            traininfoById = b1[
                       0] + '\t' + start_time + '\t' + start_station + '\t' + end_station + '\t' + price + '\t' + number + '\t\n'
            file.writelines(traininfoById)
            continue
        file.writelines(i)
    file.close()
    if flag == 1:
        print("没票了~")
        return False
    return traininfoById


def train_info_del():
    id = input('请输入要删除的列表车次：')
    allTrain = selectAllTrain()
    file = open("trains.txt", "w")
    # 标志位
    flag = 0
    # 查找是否存在这个车次
    for j in allTrain:
        i1 = j.replace("\n", "")
        b = i1.split('\t')
        if b[0] == id:
            flag = 1
    if flag == 0:
        print("数据库中不存在该车次！")
        return False
    for i in allTrain:
        i1 = i.replace("\n", "")
        b = i1.split('\t')
        if b[0] == id:
            continue
        file.writelines(i)
    file.close()
    return True


def checkId(id):
    # 查找是否存在这个车次
    for j in selectAllTrain():
        i1 = j.replace("\n", "")
        b = i1.split('\t')
        if b[0] == id:
            return True
    return False
