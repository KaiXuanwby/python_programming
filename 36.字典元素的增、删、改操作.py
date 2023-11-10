#key的判断：
#in    :指定的key在字典中存在返回True-->'XXX' in scores
#not in:指定的key在字典中不存在返回True-->'XXX' not in scores

#字典元素的删除
# del scores['XXX']

#字典元素的新增
# scores['XXX'] = XXX

#键的判断
scores = {'Bob':'23','kaixuan':'20','people':'11'}
print('Bob' in scores)
print('Bob' not in scores)

del scores['Bob']
print(scores)
#scores.clear()

scores['jianghaowen'] = 98   #字典元素的新增
print(scores)
