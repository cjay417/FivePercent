import requests
from bs4 import BeautifulSoup

base_url = 'http://www.hyundaihmall.com'
#2050137927 - 비에비어
#2050137927 - 보국
product_id = 2050137927

def get_number_of_review(product_code):
    url = base_url+'/front/pda/itemPtc.do?slitmCd='+str(product_code)
    #print(url)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")
    for link in soup.findAll('span', {'class': 'font_sstpl_pk '}):
        start = str(link).index('총')+2
        end = str(link).index('건')
        value = str(link)[start:end]

    if (int(value) % 10 == 0):
        v = int(value) / 10
    else:
        v = int(value) / 10 + 1

    return v

def trade_spider(max_pages, id):
    page = 1
    while(page <= max_pages):
        #url = 'http://www.hyundaihmall.com/front/pda/itemPtc.do?slitmCd=2050137927&sectId=141253'

        url=base_url+'/front/pdc/selectOptItemEvalList.do?optSlitmMstCd='+str(id)+'&optImgNm=2050137927_0_170.jpg&optYn=N&page='+str(page)+'&slitmCd='+str(id)

        print(url)

        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")
        #print(soup)
        #for link in soup.findAll('div', {'class':'reply_num'}):
        for link in soup.findAll('td', {'class': 'center pt20 pb20'}):
            start_review = str(link).index('</p><p>') + 7
            end_review = str(link).index('</p>\n</td>')
            review_content = str(link)[start_review:end_review]
            #print(link)
            print(review_content)
        page+=1

#review_count = get_number_of_review(str(2050137927))

review_count = get_number_of_review(str(product_id))
trade_spider(review_count, product_id)
#trade_spider(1)

#<a href="/front/pdc/selectOptItemEvalList.do?optSlitmMstCd=2050137927&amp;optImgNm=2050137927_0_170.jpg&amp;optYn=N&amp;page=2&amp;slitmCd=2050137927">2</a>
#&amp; &


