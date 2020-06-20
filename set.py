import pandas as pd
import numpy as np
#随机生成一批数据
pd.set_option("display.max_columns",None)
userList=[]
for i in range(1,51):
    userList.append("user_"+str(i))#添加用户user_1.....
userInfo=pd.DataFrame({'userName':userList,#随机生成列表
                       'GoodA':np.random.randint(0,6,50),
                       'GoodB':np.random.randint(0,6,50),
                       'GoodC':np.random.randint(0,6,50),
                       'GoodD':np.random.randint(0,6,50),
                       'GoodE':np.random.randint(0,6,50),
                       'GoodF':np.random.randint(0,6,50),
                       'GoodG':np.random.randint(0,6,50),
                       'GoodH':np.random.randint(0,6,50),
                       'GoodI':np.random.randint(0,6,50),
                       },index=None)

print(userInfo["GoodH"][0])

for i in userInfo.columns.tolist()[1:]:#模拟生成数据
    for j in np.random.randint(0,51,8):
        userInfo[i][j]=0

print(userInfo)
userInfo.to_excel('BrowseNumber.xlsx',index=False)

'''
for i in  userInfo.columns.values.tolist()[1:]:
        userInfo[i][userInfo[i]==1]=0
userInfo.index = userInfo['userName']
userInfo = userInfo.drop('userName', axis=1)
userDist = userInfo.T.to_dict()
lists=list(userDist.keys())#[user_1,.....]
list_1=list(userDist[lists[0]].keys())#['GoodA', 'GoodB', 'GoodC', 'GoodD', 'GoodE', 'GoodF']
for k in lists:
    for j in list_1:
        if userDist[k][j]==0:
            userDist[k].pop(str(j))
print(userDist)'''