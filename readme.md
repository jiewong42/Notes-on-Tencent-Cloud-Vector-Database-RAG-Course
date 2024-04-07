# 腾讯云向量数据库《 RAG 七天入门训练营》学习笔记
- [课程学习入口](https://mc.tencent.com/HpC5MZty)

- [全套 PPT 下载地址](https://drive.weixin.qq.com/s?k=AJEAIQdfAAoLG4kLZk)

- [腾讯云向量数据库免费 1 个月测试版实例](https://mc.tencent.com/jxnlFsSD)

以上是官方链接。 PPT 存档在此仓库
## 测试代码
vdb_url , vdb_api_key 需在腾讯云向量数据库平台获取
```python
import tcvectordb
import os
vdb_url=""
vdb_api_key=""
db_name="testdb"
collView_name="knowledge"
file_path="pdf/"
vdbclient = tcvectordb.VectorDBClient(url=vdb_url, username="root",key=vdb_api_key)
db = vdbclient.create_ai_database(database_name=db_name+"01")
collView= db.create_collection_view(name=collView_name+"01")

def konwledgeInit():
    for file_name in os.listdir(file_path):
        if file_name.endswith(".pdf"):
            print("上传:{}\n".format(file_name))
            collView.load_and_split_text(local_file_path=file_path+file_name)
    print("上传完成")
def searchKnowledge(question):
    doc_list=collView.search(
        content=question,
        limit=3,
        expand_chunk=[2,2]
    )
    for doc in doc_list:
        print(doc.data.text)
def generate_answer():
    pass
if __name__ == '__main__':
    konwledgeInit()
    question=input("请输入问题:\n")
    print("问答:",question)
    print("===========")
    searchKnowledge(question)

```
## 心得
此课程无需 7 天即可完成，大多为概念知识，建议直接上手测试代码。
![结营证书](/结营证书.png)

## 课程背景
>随着大模型的快速发展，RAG（检索增强生成）作为一种新兴的开发范式，能有效解决大模型的幻觉和知识停滞的问题，并已成为企业构建智能问答应用的最佳实践。RAG技术易于入门，但要满足企业级应用的高标准仍具挑战。 为此，腾讯云向量数据库团队与腾讯云安灯团队联合推出了《RAG七天入门训练营》课程，将从基础理论到实际应用，由鹅厂大牛带你快速学习RAG，并配有专属社群，讲师一对一答疑，在AGI时代助你轻松上手，