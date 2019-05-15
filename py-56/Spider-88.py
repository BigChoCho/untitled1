import re
#\d是數字 +號表示出現1次或多次 r是避免反斜槓轉譯
s=r"\d+"
#從compole返回Pattern对象是不能直接实例化的，只能通过compile方法得到
pattern = re.compile(s)
#通過pattern.match進行匹配,返回一個math對象
m= pattern.match("one123dwa22daw3")
print(type(m))
#第一個找不到則直接返回空
print(m)
#從3~10尋找,一旦遇到非匹配對象直接結束尋找(從0開始計算)
m= pattern.match("one123dwa22daw3",3,10)
print(type(m))
print(m)
#取出match值
print(m.group())
#從0開始計算,從哪個下標開始
print(m.start(0))
#在哪個下標結束
print(m.end(0))
#顯示開始到結束的下標
print(m.span(0))
print(m.span(0)[0]-m.span(0)[1])