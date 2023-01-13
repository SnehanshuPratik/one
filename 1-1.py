a="adf1hh"
for i in range (len(a)):
    print(a[i],type(a[i]))
e=[]
for i in range(10):
    e.append(i)
    print(e)
print(e)
name=['ram','sam','tan','lan']
roll=[34,43,56,65]
for i in range(len(name)):
    print(name[i],roll[i]) 
mix=[]
for i in range(len(name)):
    mix.append(name[i])
    mix.append(roll[i])
    print(mix)
print(mix)
print(mix,type(mix))
dic={
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
}
print(dic)
newdic={
    'a':[
        {'k':1,'l':2,'m':3},
        {'n':4,'o':5,'p':6}
    ],
    'b':[
        {'q':7,'r':8},                    #dictionary is mutable
        {'s':9,'t':10}
    ]
}
print(newdic)
print(newdic['b'])
print(newdic['b'][1]['t'])
newdic['b'][1]['t']=11
print(newdic['b'][1]['t'])