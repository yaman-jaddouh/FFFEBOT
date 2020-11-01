#!/usr/ env python
# -*- coding: utf-8 -*-
import json
def historyW(id,array):
    a={}
    fileR=open('history.json','r')
    a=json.loads(fileR.read())
    if str(id) not in a:
        a[id]=array
    else:
        a[str(id)]=array
    fileW=open('history.json','w')
    fileW.write(json.dumps(a))
    fileW.close()

def historyR(id):
    pass

#historyW(880941251,[1,23,4,2])

def check_old(id):
    fileR=open('data.json','r')
    data=json.loads(fileR.read())
    oldUsers=data['old_users']
    newUsers=data['users']
    fileR.close()
    if id in oldUsers and id not in newUsers :
        return True
    else:
        return False

def check_or_add(id): #check or add user if exist or not
    #result=False
    fileR=open('data.json','r')
    data=json.loads(fileR.read())
    if check_old(id) :
        data['old_users'].remove(id)
    if id in data['users']:
        return True
    else:
        data['users'].append(id)    
        fileW=open('data.json','w')
        fileW.write(json.dumps(data))  
        fileW.close()
        fileR.close()










