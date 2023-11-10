#for item in scores
#   print(item)
#遍历时，只遍历字典的键
scores = {'Bob':'23','kaixuan':'20','people':'11'}
for item in scores:
    print(item)
    print(item,scores[item],scores.get(item))
    print('-------------------------------------')


