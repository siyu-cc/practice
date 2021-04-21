from bs4 import BeautifulSoup
import urllib.request
from urllib import request
import lxml
import requests
import urllib.parse
import sys,re

#region 声明变量
urls = "https://www.44txt.cc"
dict1 = {}
dict2 = {}
nlClass = ""
list2 = []
urlnovel = []
pageNum = 1   #初始化第一页为 20
#endregion

#region   通过网址 拉取网页信息保存到本地
def get_html(urls):
    try:
        html = request.urlopen(urls)
        rd = html.read()
        rd.decode('utf-8')
        c = open(r"D:\csy\htmlNovel\html.txt", 'wb')
        c.write(rd)
        c.close()
        return rd
    except Exception as ex:
        print('出现异常: % s' % ex)
#endregion

#region 选择小说分类
def get_classify(text_html):
    try:
        soup1 = text_html.find_all("a", limit=12)[2:]
        # 用正则匹配 获取想要的内容
        re1 = r'<a href="(.*?)">(.*?)</a>'
        str1 = re.findall(re1, str(soup1))
        # print(str1)
        list1 = []
        str2 = ""
        num = 0
        for s in str1:
            list1.append(s)  # 把分类类别存放在一个列表中
            str2 += list1[num][1] + ','
            num += 1
        # print(str2)
        global dict1  # 声明为全局变量
        dict1 = dict(list1)
        print('请选择小说类别: %s ' % str2[:len(str2) - 1])
        return dict1
    except Exception as ex:
        print('出现异常: %s ' % ex)

#endregion

#region  解析具体的小说分类页面
def get_jiexi(text_html):
    #查找 a标签
    soup = text_html.findAll(name='div',attrs={"class":"list"}) #先找到大范围
    re2 = r'<a href="/book/(.*?)">(.*?)</a>'
    re3 = r'/>(.*?)'
    soup1 = re.findall(re2,str(soup))  #找到 小说名称和链接
    i = 0
    str2 = ""
    for num in soup1:           #展示页面主要推荐的小说
        ss = num[1]          #获取小说名称
        index = ss.index(">") + 1   #找到关键字 关键词之后就是小说名称
        index1 = len(ss)            #找到第2个列表中的字符串总长度
        str1 = ss[index:index1-8]   #截取小说名称
        str2 += str1 + ','
        global  list2,dict2,urlnovel
        list2.append(num[0])          #把小说对应的网址保存起来
        urlnovel = '%s/book/%s'% (urls,str(num[0]))     #合成一个完整的小说网址
        # a = '"%s":"%s"'% (urlnovel,str1)    #构造一个字典  key:小说网址  value:小说名称
        # print(a)
        dict2.setdefault(urlnovel,str1)
        i += 1
    print('主要推荐书籍:%s'% str2[:len(str2)-1])
    # print(dict2)
    # return dict2
#endregion

#region  小说分类翻页功能
def GetnextPage(text_html,page):
    # 0：下一页  1:上一页  2-624：具体页数  624:最后一页
    # 不是每个分类的页数都一样的，需要修改
    '''  所有小说分类的页数
    玄幻奇幻:2000页
    都市言情：2329页
    武侠修真:624页
    历史军事:377页
    网游竞技:443页
    科幻离奇：501页
    恐怖惊奇:65页
    文学名著:8页
    最新全本:2000页
    在线试读:1000页
    '''
    listpage = [i for i in range(0,625)]
    urlpage = ['{}/index_{}.html'.format(url2,i) for i in range(2,625)]
    global pageNum,url2
    url3 = ""

    if page in listpage:        #判断输入的数字是否再列表范围内
        if page == 0:           #转入到下页的链接中
            if pageNum == 1:
                url3 = '{}/index_2.html'.format(url2)
                pageNum += 1
            else:
                pageNum += 1         #下一页  页数+1
                url3 = '{}/index_{}.html'.format(url2,pageNum)
        elif page == 1:         #转入到上一页的链接中
            pageNum -= 1
            print('页数：%d' % pageNum)
            url3 = urlpage[pageNum-2]   #上一页  页数-1
        elif page >= 2 and page <= 624:   #转入到2-624中的链接中
            if pageNum == 2:
                url3 == url2
            else:
                pageNum = page
                url3 = urlpage[page-2]   #2-624 有固定的链接
        else:                   #输入其它页数无效
            print('没有该页数了')
    else:
        print('超出页数范围！！！')
    print(url3)
    print('当前页数: %d  输入的页数: %d' % (pageNum, page))
    html = get_html(url3)  # 进入新的网页，保存新的网页信息
    nlNovel = BeautifulSoup(html, 'html.parser')
    get_jiexi(nlNovel)

#endregion

#region 读取小说内容
# def get_novel(text_html):
#endregion

#region 小说翻页功能
#endregion

if __name__ == "__main__":
    print('~~~~~~~~~~~~~~~~~~~~~~~~~欢迎进入44小说网首页~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    Html = get_html(urls)  # 调用函数: 把网页上的信息保存到文本
    nlClass = BeautifulSoup(Html, 'html.parser')
    get_classify(nlClass)  # 解析本地文本中的信息，对小说进行分类整理
    global url2

    nl = input("请输入小说类别:")
    if nl in str(dict1):
        # print('选择的小说类别是: %s '% nl)
        url2 = urls + list(dict1.keys())[list(dict1.values()).index(nl)]  #查找类别在列表中的位置 ，找到对应的网址
        print('网址:%s'% url2)
        Html1 = get_html(url2)  #进入新的网页，保存新的网页信息
        nlClass = BeautifulSoup(Html1, 'html.parser')
        get_jiexi(nlClass)    #解析新的网页
        print('--0:跳转到当前页面的下一页, 1:跳转到当前页面的上一页(第一页除外)，(2-624):跳转到具体页数,624:最后一页，1000:退出----')
        while(True):
            instr = input('输入:')  # 搜索下一页
            if instr.isdigit():
                instr = int(instr)
                if instr == 1 and pageNum == 1:  #向上翻页
                    print('当前页面是第一页，不能查看上一页哦！')
                elif instr == 1 and (pageNum > 1 and pageNum < 625):
                    GetnextPage(url2,instr)     #当前网页的页数
                    # break
                elif instr == 0 and pageNum == 624:   #向下翻页
                    print('当前页面已经是最后一页了哦！')
                elif instr == 0 and (pageNum >=1 and pageNum < 624):
                    GetnextPage(url2, instr)  # 当前网页的页数
                elif instr >= 2 and instr <= 624:
                    GetnextPage(url2, instr)  # 当前网页的页数
                    # break;
                elif instr == 1000:
                    print('退出！！')
                    break
            else:
                print('请输入数字！！！')
    else:
        print('该小说网没有您要搜索的小说类别')





