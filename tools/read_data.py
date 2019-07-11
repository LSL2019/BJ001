# class ReadData(object):
#     def read_login_data(self):
#         with open('../data/data.login.txt','r',encoding='utf-8') as f:
#             print(f.read())

with open('../data/data_login.txt', 'r', encoding='utf-8') as f:
    arr=[]
    for data in f.readlines():
        arr.append(tuple(data.strip().split(',')))
    print(arr[1::])
