import requests
from lxml import etree
#725586  ：小说开始             726355：小说结束
urls = ['https://www.uubiqu.com/read/726/{}.html'.format(i) for i in range(725586,726355)]  #存放小说每章节的网址
path = r'D:\csy\python\novel'      #存储小说的路径

def get_novel(url):
    try:
        r = requests.get(url) #获取每章小说的网址
        r.encoding = 'utf-8'  #转换为UTF-8格式
        selector = etree.HTML(r.text)   #把所有的网页内容放到一个变量里面保存
        title = selector.xpath('//div[@class="bookname"]/h1/text()')[0] #获取章节 名称
        text = selector.xpath('//p/text()')  #获取 章节内容
        print(title)
        num = 0
        with open(path + "\\" + title + '.doc', 'w', encoding='utf-8') as f:  #打开要存储的文件路径
            for i in text:
                f.write(i)                    #写入到Word文档中
                num += 1                      #记录次数
            print('成功写入 %d 章' % num)
    except Exception as ec:                   #异常处理    所以会有露掉的章节
        print('出现异常:%s' % ec)

if __name__ == '__main__':                    #主函数:程序的入口
    for url in urls:                          #循环  每个章节的网址
        get_novel(url)                        #调用函数:获取网页中想要的内容并写入word文档