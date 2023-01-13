avg=[
    ['spidy',10],
    ['groot',45],
    ['bat',85]
]
for i in avg:
    for j in i:
        print(j)

employlist=[{
    'name':'tony',
    'employee':3,
    'address':[
        {
            'line1':'fff',
            'line2':'dd',
            'state':'ko',
            'pin':74855
        },
        {
            'line1':'ff',
            'line2':'fdd',
            'state':'fff',
            'pin':'756666'
        }
    ]
},
{
    'name':'spidy',
    'employee':5,
    'address':[
        {
            'line1':'ffddf',
            'line2':'ddddd',
            'state':'koc',
            'pin':748455
        },
        {
            'line1':'dff',
            'line2':'fsddd',
            'state':'ffwdf',
            'pin':'75666746'
        }
    ]
}
]
# print(employlist[1]['name'])
for i in range(len(employlist)):
    print(employlist[i]['name'],employlist[i]['address'][i]['pin'])


emppin=[]
for emp in employlist:
    emppin.append({'name':emp['name']})
    # print(employlist)
    # print(employlist.index{emp})
    emppin[employlist.index(emp)]['pin']=[]

    for address in emp['address']:
        emppin[employlist.index(emp)]['pin'].append(address['pin'])
        print('pin',address['pin'])
print(emppin)

def multiply(a,b):
    c=a*b
    return c

y=multiply(5,4)
print(y)