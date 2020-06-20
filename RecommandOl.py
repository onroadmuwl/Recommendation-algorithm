#encoding:utf-8--
import pandas as pd
from math import sqrt,pow
class recommand():
    # 获得初始化数据
    def __init__(self):
        userInfo = pd.read_excel('BrowseNumber.xlsx')
        userInfo.index = userInfo['userName']
        userInfo = userInfo.drop('userName', axis=1)
        self.userDist = userInfo.T.to_dict()
        lists = list(self.userDist.keys())  # [user_1,.....]
        list_1 = list(self.userDist[lists[0]].keys())  # ['GoodA', 'GoodB', 'GoodC', 'GoodD', 'GoodE', 'GoodF']
        for k in lists:  # 删除为0的值
            for j in list_1:
                if self.userDist[k][j] == 0:
                    self.userDist[k].pop(str(j))




    # 欧几里得距离
    def Euclid(self, user1_data, user2_data):
        distance = 0
        for key in user1_data.keys():
            if key in user2_data.keys():
                # 注意，distance越小表示两者越相似
                distance += pow(float(user1_data[key]) - float(user2_data[key]), 2)
        return 1 / (1 + sqrt(distance))  # 这里返回值越大，相似度越大,表示在0到1区间


    # 采用余弦相似度计算
    def cosSimilar(self, user1_data, user2_data):  # 采用余弦相似度计算
        # 余弦相似度是利用两个向量之间的夹角的余弦值来衡量两个向量之间的余弦相似度。两个向量越相似夹角越小，余弦值越接近1。
        a2 = 0.0
        b2 = 0.0
        ab = 0.0
        for key in user1_data.keys():
            if key in user2_data.keys():
                a2 += pow(float(user1_data[key]), 2)
                b2 += pow(float(user2_data[key]), 2)
                c = float(user1_data[key]) * float(user2_data[key])
                ab += c
        score = ab / (sqrt(a2) * sqrt(b2))
        return  score


    #选取一种距离表示方法
    def chooseMethod(self,word, user1_data, user2_data):
        if word=="cosSimilar":
            score=self.cosSimilar(user1_data, user2_data)
            return  score
        elif word=="Euclid":
            score = self.Euclid(user1_data, user2_data)
            return  score
        else :
            print("没有这种方式")


    #计算最近距离
    def closestUser(self,user,n,method):
        df=pd.DataFrame({"user":{},"score":{}})
        for elseUser,item in self.userDist.items():#遍历字典
            if elseUser!=user:
                score=self.chooseMethod(method,self.userDist[user],self.userDist[elseUser])
                df=df.append({'user': elseUser, 'score': score}, ignore_index=True)
        df=df.sort_values(by="score",ascending=False)
        print("最相似的前",str(n),"名客户:")
        print(df.head(n))
        print("\n")
        return df.head(n)

    #返回推荐结果
    def CommandResult(self,user,n,method):
        print("被推荐用户："+user)
        print("采取的推荐用户数："+str(n))
        print("采取的相似度算法（欧几里得相似度/余弦相似度）："+method)
        print("\n")
        df=self.closestUser(user,n,method)
        userList=df["user"].tolist()
        scoreList=df["score"].tolist()
        number=0
        for k in range(0,len(userList)):
            for good,item in self.userDist[userList[k]].items():
                if good not in self.userDist[user].keys():
                    print("通过"+str(userList[k])+"用户为"+str(user)+"推荐保险产品"+str(good)+"推荐度为"+str(scoreList[k]))
                    number+=1
        print("共有"+str(number)+"条建议")




if __name__=='__main__':
    d=recommand()
    d.CommandResult(user='user_1',n=1,method="Euclid")









