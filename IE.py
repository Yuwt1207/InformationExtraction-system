import re

def InfoExtraction(docset:set):
    result=list()
    for docname in docset:
        with open("data/"+docname,encoding="utf-8") as fp:
            data=fp.read()
            fp.close()
        typereg="#.*#"
        resultreg="【[A-Z0-9.]+\s[0-9]-[0-9]\s[A-Z0-9.]+】"
        timereg="[0-9]+分[钟半]|[0-9]+[:：][0-9]+"
        temp=dict()
        temp["filename"]=docname
        temp["type"]=re.findall(typereg,data)
        temp["result"]=re.findall(resultreg,data)
        temp["time"]=re.findall(timereg,data)
        result.append(temp)
    return result