# print("hello world")
# a=7
# print(type(a))
# b=True
# print(type(b))
# c=444.45
# print(type(c))
# x=7
# y=9
# print("sum =",x+y)
# ele=[]
# for i in range(10):
#     ele.append(i)
#     print(ele)
# print(ele)
# a=input("fname ")
# b=input("lname ")
# print(a+" "+b)
# n=int(input("give num "))
# m=int(input("give 2nd num "))
# print(type(n))
# a="asdfgh"
# print(a[1])
# print(a[4])
# print(a[-5:4])
# print(a[0:5])
# print(len(a))
# for i in range(len(a)):
#     print(a[i],type(a[i]))
# avglist=["im","ca","th","sm"]
# print(avglist[1])
# rali=[12,3,45,54]
# ratavg=[]
# for i in range(len(avglist)):                      #[]-used in list,()used in tuple,{}used in dictionary
#     print(avglist[i],rali[i])
#     ratavg.append(avglist[i])
#     ratavg.append(rali[i])
# print(ratavg)
# print(type(ratavg))
#dictionary
avgdis={
    "ddf":45,
    "ffd":56,                                                   #no duplication
    "ffd":56,
    "hjh":78
}
print(avgdis)
print(type(avgdis))
#nested dictionary
newdic={
    "dff":[
        {"hjh":87},
        {"ddd":77}
    ],
    "ess":[
        {"fdd":74},
        {"edd":41}
    ]
}
print(newdic["dff"])
print("rating of hjh: ",newdic["dff"][0]["hjh"])