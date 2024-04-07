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

