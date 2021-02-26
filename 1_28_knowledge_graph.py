import pymongo
from py2neo import Graph, Node, Relationship, Subgraph

graph = Graph("http://localhost:11005", username='test', password='ZHANGYAWEIsw8812')
print("连接Neo4j成功")
client = pymongo.MongoClient(
    "mongodb://monetware:monetware2020%40sh.com@49.74.204.78:20000/admin?connectTimeoutMS=10000&authSource=admin")
db = client["index"]
collection = db["journal"]
print("连接mongodb成功")
a = Node("title", name="大学生安全手册")
b = Node("author", name="李三")
c = Node("subject_1", name="dasda")
d = Node("subject_2", name="dsadasdsa")
new_nodes = [c, d]
sub = Subgraph(nodes=new_nodes)
ab = Relationship(a, "作者", b)
graph.create(ab)
ac = Relationship(a, "主题", sub)
graph.create(ac)
# for journal in collection.find():
#     print(journal)
#     title = journal["title"]
#     author = journal["author"]
#     first_author = journal["first_author"]
#     author_organization = journal["author_organization"]
#     key_words = journal["keywords"]
#     digest = journal["digest"]
#     subject = journal["subject"]
#     label = journal["label"]
#     source = journal["source"]
#     pub_time = journal["pub_time"]
#     clc_number = journal["clc_number"]
#     page = journal["page"]
#     node_list = []
#
#     a = Node("title", name=title)
#     b = Node("author", name=author)
#     c = Node("first_author", name=first_author)
#     d = Node("author_organization", name=author_organization)
#     e = Node("key_words", name=key_words)
#     f = Node("digest", name=digest)
#     g = Node("subject", name=subject)
#     h = Node("label", name=label)
#     i = Node("source", name=source)
#     j = Node("pub_time", name=pub_time)
#     k = Node("clc_number", name=clc_number)
#     l = Node("page", name=page)
#
#     ab = Relationship(a, "作者", b)
#     graph.create(ab)
#     ac = Relationship(a, "第一作者", c)
#     graph.create(ac)
#     ad = Relationship(a, "作者所属机构", d)
#     graph.create(ad)
#     ae = Relationship(a, "关键词", e)
#     graph.create(ae)
#     af = Relationship(a, "摘要", f)
#     graph.create(af)
#     ag = Relationship(a, "主题", g)
#     graph.create(ag)
#     ah = Relationship(a, "标签", h)
#     graph.create(ah)
#     ai = Relationship(a, "来源", i)
#     graph.create(ai)
#     aj = Relationship(a, "发布时间", j)
#     graph.create(aj)
#     ak = Relationship(a, "期刊名称", k)
#     graph.create(ak)
#     al = Relationship(a, "页数", l)
#     graph.create(al)
