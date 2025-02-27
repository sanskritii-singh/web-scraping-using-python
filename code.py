
import requests
from bs4 import BeautifulSoup
import pprint
res= requests.get('https://news.ycombinator.com/')
res2=requests.get('https://news.ycombinator.com/news?p=2')
soup=BeautifulSoup(res.text,'html.parser')
soup2=BeautifulSoup(res.text,'html.parser')
link=soup.select('.titleline a')
link2=soup2.select('.titleline a')
subtext=soup.select('.subtext')
subtext2=soup2.select('.subtext')

mega_links=link+link2
mega_subtext=subtext+subtext2
def sort_stories_by_votes(hnlist):
    return sorted(hnlist,key=lambda k:k['votes'],reverse=True)


def create_customhn(link,subtext):
    hn=[]
    for idx,item in enumerate(link):
        title=item.getText()
        href=item.get('href',None)
        vote=subtext[idx].select('.score')  if idx < len(subtext) else []
        if len(vote):
            points=int(vote[0].getText().replace(' points'," "))
            if points>99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)
pprint.pprint(create_customhn(mega_links,mega_subtext))   
