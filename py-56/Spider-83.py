import lxml.html
etree = lxml.html.etree

# 使用lxml解析html代碼
text ='''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CSS盒子模塊</title>
    <link rel="stylesheet"type="text/css"href="CSS-37.css">
</head>
<body>
<!--頂層-->
    <div class="top">
<!--        頂內層-->
        <div class="top_content"></div>
</body>
</html>
'''
# 先把上部內容轉換成html(自動對中文字進行邊碼,以及代碼不足處)
html = etree.HTML(text)
s= etree.tostring(html)
print(s)
#只能讀取xml檔
htm2 =etree.parse(".\Spider-81.xml")
rst2 = etree.tostring(htm2,pretty_print=True)
print(rst2)