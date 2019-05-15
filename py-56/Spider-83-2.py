import lxml.html
etree = lxml.html.etree
#返回了一個解釋器,意味著可用path檔進行解析
html =etree.parse(".\Spider-81.xml")
print(type(html))
#利用xpath獲取相關節點
rst = html.xpath("//book")
print(type(rst))
print(rst)
#注意 '' 的使用,查找該節點的屬性
rst = html.xpath('//book[@categor="cood"]')
print(rst)
#查找該節點下的子節點,返回list類型
rst = html.xpath('//book[@categor="cood"]/year')
#在year的list下取出第1位year
rst = rst[0]
print(rst)
#year的標籤
print(rst.tag)
#year的內文
print(rst.text)
