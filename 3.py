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
emppin=[]
for emp in employlist:
    emppin.append({'name':emp['name']})
print(emppin)
# def exp(x):
#     if 'x' in employlist:

