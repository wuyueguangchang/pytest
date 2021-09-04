import json
userdata={'user':'zhaofang',
          'password':'123'}
table=[]
print(userdata['user'])
print('name:{name}\n password:{password}'.format(name=userdata['user'],password=userdata['password']))
print(userdata.items())
print(userdata.keys())
print(list(userdata.values()))
for key in userdata:
    print(key,userdata[key])

userdata.update({'password':'12345'})
print(userdata['password'])
userdata.update({'database':'test'})
print(userdata['database'])
userdata.pop('database')
#print(userdata['database'])

table=[userdata,userdata,userdata]
jsonData=json.dumps(userdata)
with open('userPwd.json','w') as f:
    json.dump(table,f)
with open('userPwd.json') as f:
    data=json.load(f)