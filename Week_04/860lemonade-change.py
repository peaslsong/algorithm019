def lemonadeChange(bills):
    '''
    建立一个字典v，用来存现在有多少5元和10元。
    如果顾客付的是5元，则5元数量加1；
    如果顾客付的是10元，则5元数量减1，10元数量加1；如果5元数量不够，则无法找零；
    如果顾客付的是20元，首先先用10元来找零，没有10元，则用5元找零，如果5元或10元数量不够，则无法找零。
    :param bills:
    :return:
    '''
    v = {'five': 0, 'ten': 0}
    for i in range(len(bills)):
        if bills[i] == 5:
            v['five'] = v['five'] + 1
        elif bills[i] == 10:
            v['five'] = v['five'] - 1
            v['ten'] = v['ten'] + 1
            if v['five'] < 0 or v['ten'] < 0:
                return False
                break
        elif bills[i] == 20:
            if v['ten'] >= 1:
                v['ten'] = v['ten'] - 1
                v['five'] = v['five'] - 1
            else:
                v['five'] = v['five'] - 3
            if v['five'] < 0 or v['ten'] < 0:
                return False
                break
    return True



# bills = [5, 5, 5, 10, 20]
bills = [5, 5, 5, 5, 20, 20, 5, 5, 5, 5]
print(lemonadeChange(bills))
