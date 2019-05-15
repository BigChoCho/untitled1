import re

#有match就可以group

#搜尋1段數字
s=r'\d+'
pattern = re.compile(s)
#這個方法的搜尋結果<re.Match object; span=(4, 9), match='11993'>
m =pattern.search("fuck11993inthernow2019old")

print(m)
print(m.group())

#搜查範圍
m=pattern.search("fuck11993inthernow2019old",10,40)
print(m.group())
#搜尋數字,並且以數字以外字符以外為區隔返回list型,並讀取所有數字
m1 = pattern.findall("fuck11993inthernow2019old")
print(m1)
#返回的是迭代器,需要添加group
m2 = pattern.finditer("fuck11993inthernow2019old")
for i in m2:
    print(i.group())