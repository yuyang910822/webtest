personal_information = {'name':'韩','age':'28','sex':'女'}
list1 = ['interest']
list2 = ['唱','游泳','跳舞']
data = dict.fromkeys(list1,list2)
print(data)
personal_information.update(data)
print(personal_information)