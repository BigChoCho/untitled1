import re
#一行文字空格後的第一位
s = "i sing my life is good or not good"

content = re.findall(r"\b\w",s)
print(content)
print(re.findall(r"\b",s))
print(re.findall(r"\w",s))
#all數字開頭
s1 = "my age is 33old my live in the 1800yer 7m 14day 12hr  "
print(re.findall(r"\b\d",s1))
s2 ="my age is 33old my live in the 1800yer 7m 14day 12hr \n" \
    " i sing my life is good or not good\n " \
    "dadw22 dwd234 \n"
#包含數字和字母的行 re.M匹配多行
print(re.findall(r"\w+",s2,re.M))