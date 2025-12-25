from mongoengine import connect
from sina.models.newsEmbedding import NewsEmbedding
from common_module import init_common

# 初始化配置
init_common()

# 模拟 main.py 的连接方式
connect("news_db", alias="source")
connect("news_recommender", alias="default")

# 1. 查总数
count = NewsEmbedding.objects.count()
print(f"【查询结果】NewsEmbedding 表里共有: {count} 条数据")

# 2. 查它到底连的哪个库、哪个表
if count > 0:
    # 获取真实连接的数据库名
    db_name = NewsEmbedding._get_db().name
    # 获取真实的集合名
    collection_name = NewsEmbedding._get_collection_name()

    print(f"【藏身之处】")
    print(f"  -> 数据库(Database): {db_name}")
    print(f"  -> 集合(Collection): {collection_name}")
    print("请去 MongoDB Compass 里找这两个名字！")
else:
    print("表中确实没数据，可能是 save() 没成功，或者连接被重置了。")