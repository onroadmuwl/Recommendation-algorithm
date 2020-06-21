# Recommendation-algorithm
基于用户协调过滤推荐算法

# set.py
随机生成一组关于用户浏览量的数据，商品数目设为9，用户数设为50

# recommandIO.py
获取数据，并将DataFrame转化为字典数据类型<br>
采用欧几里得距离，余弦相似度方式计算相似度<br>
然后根据相似度获取推荐的用户<br>
根据推荐用户和被推荐用户对比，得出推荐的结果<br>
