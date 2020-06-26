import json
import os
import pynlpir
# coding:UTF-8

def getIndex():
    if os.path.exists("index.json"):
        with open("index.json") as fp:
            index=json.load(fp)
            word=index.keys()
    else:
        pynlpir.open()#记得open加载nlpir的库，这步是必要的
        dir="data"
        filelist=os.listdir(dir)
        index=dict()
        for filename in filelist:
            with open(dir+"/"+filename,encoding="utf-8") as fp:
                data=fp.read()
                fp.close()
            result=pynlpir.get_key_words(data)
            for word in result:
                if word not in index:
                    index[word]=list()
                index[word].append(filename)

        idxjson=json.dumps(index)
        with open("index.json","w") as fp:
            fp.write(idxjson)

        word=index.keys()
    return word,index
