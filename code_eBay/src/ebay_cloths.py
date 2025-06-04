import json
import requests
from bs4 import BeautifulSoup
urls=['https://www.ebay.com/sch/260012/i.html?_nkw=men&_from=R40&_ipg=100&_oac=1&_pgn=','https://www.ebay.com/sch/260012/i.html?_nkw=women&_from=R40&_ipg=100&_oac=1&_pgn=']
results = []
for index,url in enumerate(urls):
    for i in range(1,20):
        url=url+str(i)
        res=requests.get(url)
        soup=BeautifulSoup(res.text,'html.parser')
        div=soup.find_all('div',id='srp-river-results')
        for d in div:
            elements=d.find_all('li',class_='s-item s-item__pl-on-bottom')
            for element in elements:
                title=element.find('div',class_='s-item__title').text.strip()
                meta_info=element.find('div',class_='s-item__details-section--primary')
                details = meta_info.find_all('div', class_='s-item__detail s-item__detail--primary')
                fetch_details= [d.text.strip() for d in details]
                for detail in fetch_details:
                    if 'Shipping' in detail or "delivery" in detail:
                        delivery_price = detail
                        continue
                    elif '$' in detail:
                        price = detail
                        continue
                    elif 'Buy It Now' in detail or 'Auction' in detail:
                        delivery_type = detail
                        continue
                    elif 'from' in detail or 'located' in detail:
                        location = detail
                
                image_link=element.find('div',class_='s-item__image')
                link=image_link.find('a')['href']
                image=image_link.find('div',class_='s-item__image-wrapper image-treatment').find('img')['src']
                item_data = {
                                'title': title,
                                'price': price,
                                'delivery_type': delivery_type,
                                'delivery_price': delivery_price,
                                'location': location,
                                'product_link': link,
                                'image_link': image,
                                'sex':'M' if index==0 else "F"
                            }
                results.append(item_data)


with open('ebay_clothing_data.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)