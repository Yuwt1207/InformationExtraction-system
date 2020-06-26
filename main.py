import jieba
import pynlpir
import re
from index import *
from searching import *
from IE import *

if __name__=='__main__':
    print("-----------getting index--------------")
    word, index = getIndex()
    print("-----------load complete!-------------")

    print("-----------Search Start---------------")
    pynlpir.open()
    while True:
        print("Please input the query keywords:")
        keywords=input()
        tokens=pynlpir.get_key_words(keywords)
        print(tokens)
        docset=search(tokens,index)
        print("共找到"+str(len(docset))+"个文档")
        results=InfoExtraction(docset)
        for result in results:
            print("文档："+result["filename"])
            print("赛事类型:"+(''.join(result["type"])).strip("#"))
            temp=''.join(result["result"])
            teamnamereg="[A-Z][A-Z0-9.]*"
            goalreg="[0-9]"
            team=re.findall(teamnamereg,temp)
            goal=re.findall(goalreg,temp)
            if int(goal[0])<int(goal[1]):
                win=team[1]
                lose=team[0]
                wingoal=int(goal[1])
                losegoal=int(goal[0])
            else:
                win = team[0]
                lose = team[1]
                wingoal = int(goal[0])
                losegoal = int(goal[1])
            print("胜者:"+win)
            print("败者:"+lose)
            print("比分:"+str(wingoal)+"-"+str(losegoal))
            if(wingoal==1):
                print("赛事规则:一局一胜")
            elif(wingoal==3):
                print("赛事规则:三局两胜")
            else:
                print("赛事规则:五局三胜")
            print("关键时间点:"+','.join(result["time"]))
            print()




