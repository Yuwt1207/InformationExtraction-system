
def search(tokens:list,index:dict):
    docset=set()
    if len(tokens)==0:
        return list(docset)
    else:
        for token in tokens:
            if token in index:
                for doc in index[token]:
                    docset.add(doc)
    return docset