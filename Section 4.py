def sum(list):
    if len(list) == 1:
        return  list[0]
    else:
        a = list[0]
        list.remove(list[0])
        return a + sum(list)
def count(list):
    if not list:
        return 0
    else:
        list.remove(list[0])
        return 1 + count(list)

def Max_num(lsit):
    if len(list) == 1:
        return list[0]
    else:
        if list[1] >= list[0]:
            list.remove(list[0])
            return Max_num(list)
        else:
            list.remove(list[1])
            return Max_num(list)
def find_num(list,target):
    if len(list) == 1:
        return list[0]
    else:
        if list[len(list)//2-1] == target:
            return target
        elif list[len(list)//2-1] < target:
            del list[0:len(list)//2-1]
            return find_num(list, target)
        else:
            del list[len(list)//2-1:len(list)-1]
            return find_num(list, target)

if __name__ == '__main__': #__name__当前模块名，模块直接运行时，name==main,模块被导入时，name==模块名
    list = [2,12,43,52,333]
    # print("求和:",sum(list))
    # print("计数：",count(list))
    # print("最大数：",Max_num(list))
    print("二分法",find_num(list,43))