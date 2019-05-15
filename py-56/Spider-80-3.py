import re
#漢字的匹配方式
hello =u"倪好 笨蛋"
#unicode编码[\u4e00-\u9fa5]匹配所有中文-
pattern = re.compile(r"[\u4e00-\u9fa5]+")

m = pattern.findall(hello)
print(m)