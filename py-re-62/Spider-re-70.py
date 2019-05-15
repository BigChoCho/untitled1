
#indeed
from bs4 import  BeautifulSoup
from urllib import request



def qq():
    # 获取页面
    url = 'https://tw.indeed.com/jobs?q=%E5%BB%9A&l='
    rsp = request.urlopen(url)
    html = rsp.read()
    # print(html)
    #
    # # 提取数据
    # # 用bs解析
    soup = BeautifulSoup(html, 'lxml')
    # print(soup)
    #所有字點放置位置
    words =[]
    words2=[]
    words3=[]

    #存放對應關係
    # # 创建css选择器，得到相应的tags
    #公司名
    tr1 = soup.select("span[class='company']")
    #職缺
    tr2 = soup.select("div[class='title']")
    #薪資
    tr3 = soup.select("span[class='salary no-wrap']")

    # print(tr2)
    for tr in tr1:
        word = {}
        # 創建字典
        word.setdefault("Company_Name", [])
        #添加字典
        word["Company_Name"].append(tr.get_text().strip())
        # print(word)
        if word!={}:
            words.append(word)
    # print(words)
    for tr in tr2:
        word = {}
        # 創建字典
        word.setdefault("Job", [])
        # 添加字典
        word["Job"].append(tr.get_text().strip())
        # print(word)
        if word != {}:
            words2.append(word)
    # print(words2)

    #可用for循環自己搞,懶得搞了
    count =0
    while count<=len(tr1)-1:
        # print("公司名稱:"+str(words[count]),"職缺:"+str(words2[count]))
        count+=1




if __name__ == '__main__':
    qq()