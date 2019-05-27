# ent = input("plass ent")
# ent=int(ent)
# if ent % 3 !=0 and ent % 5 !=0:
#     print(ent,'is not amultiple of 3 or 5')
# elif ent%3==0:
#     print(ent,'is multiple of 3')
# elif ent%5==0:
#     print(ent,'is multiple of 5')
# elif ent%3 and ent%5:
#     print(ent,'is a multiple of 3 and 5')
#_____________________________

# a,b = int(input('plase ent a ')),int(input('plase ent b '))
# all =0
# if a<b:
#     for i in range(a,b+1):
#         if i==a:
#             continue
#         elif i%2 ==0:
#             all+=i
#         else:
#             continue
#     if a%2 ==0:
#         print(all+a)
#     else:
#         print(all)

#____________________________________________
# count=0
# list =[]
# while True:
#    count= int(input('plase ent if ent=9999 break:'))
#    list.append(count)
#    print(count)
#    if count == 9999:
#         break
# index=list.index(min(list))
# print('最小值',list[index],'在第',index,'個')
#___________________________

def compute(x,y):
    return (x*y)
x,y=int(input('x:')),int(input('y:'))
print(compute(x,y))