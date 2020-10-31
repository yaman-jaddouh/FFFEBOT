#!/usr/ env python
# -*- coding: utf-8 -*-
import json
a={ 'users':[123,434]}

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
    if id in data['users']:
        return True
    else:
        data['users'].append(id)    
        fileW=open('data.json','w')
        fileW.write(json.dumps(data))  
        fileW.close()
        fileR.close()










