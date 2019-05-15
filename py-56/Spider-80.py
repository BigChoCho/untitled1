#正則爬取
import re
#a-z任意至母,+表示少執行一次(第1小組)(第二小組)
s = r'([a-z+]+) ([a-z]+)'
pattern =re.compile(s,re.I)#re.I=忽略大小寫
#匹配字符串
m=pattern.match("happy not today is so bad")

#返回匹配成功的字串(0代表所有小組)
s=m.group(0)
print(s)
#表回所有匹配成功的跨度
a = m.span(0)
print(a)
#返回第1小組的字串
s = m.group(1)
print(s)
#返回第1小組跨度
a = m.span(1)
print(a)
#所有預設組別
s =m.group()
print(s)
