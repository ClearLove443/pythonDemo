with open(r'data.txt', 'r') as f:
    lines = f.readlines()  # print len(lines)
    print(len(lines))
    dic = {}
    for age in lines:
        age = age.strip()
        if age not in dic.keys():
            dic[age] = 1
        else:
            dic[age] += 1
    print('统计各个值的总数：', dic)
    total = sum(dic.values())
    for key in dic.iterkeys():
        dic[key] = (dic[key], float(dic[key])/total)
    print('统计总数和百分比：', dic)
    dicnew = {}
    li = []
    for key in dic.iterkeys():
        li.append((key, float("%0.2f" % dic[key][1])))
    print('百分比格式化为两位小数：', li)
    print('按值进行排序：', sorted(li, key=lambda item: item[0]))
    dic = dict(li)
    print('四舍五入之后的总百分比：', sum(dic.values()))
    # print li
