import sys
import urllib.request
from bs4 import BeautifulSoup
def main():
    vectorLinks=[]
    vectorLinks=Links()
    for url in vectorLinks:
         print (url)


def Links():
    url='https://www.falabella.com.co/falabella-co/category/cat5390977/Sacos-y-Hoodies'
    headers={}
    headers['User-Agent']='Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 safari/537.17'
    req=urllib.request.Request(url,headers=headers)
    resp=urllib.request.urlopen(req)
    respData=resp.read()
    saveFile=open('headers.txt','w')
    soup=BeautifulSoup(respData)
    tags=soup('a')
    direcciones=[]
    cont=0
    for tag in tags:
     aux=tag.get('href')
     if aux != None:
           if "www" in aux:
                direcciones.append()=aux
                cont+=1
    return direcciones

        
if __name__ == '__main__':
    main()

        
