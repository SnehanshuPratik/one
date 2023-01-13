avg=[
    ['spidy',10],
    ['groot',45],
    ['bat',85]
]
print(avg,type(avg))
print(avg[1][1])

for i in range(len(avg)):
    print(avg[i][0])
    print(avg[i][1])


for i in range(len(avg)):
    for j in range(len(avg[i])):
        print(avg[i][j])


employid={
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
}
print(employid['address'])
for i in range(len(employid['address'])):
    print(employid['address'][i]['pin'])
