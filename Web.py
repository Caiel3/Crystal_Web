import sys
import urllib.request
from bs4 import BeautifulSoup
def main():
   
    vectorLinks=[]
    vectorImagenes=[]
    vectorLinks=Links('https://www.falabella.com.co/falabella-co/category/cat5390977/Sacos-y-Hoodies','a','href')
    
    
    for url in vectorLinks:
        vectorImagenes.append(imagenes(url))    
    
    for imagen in vectorImagenes:
        print(imagen)
        
     


def Links(url,ppalTag,scundTag):
    headers={}
    headers['User-Agent']='Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 safari/537.17'
    req=urllib.request.Request(url,headers=headers)
    resp=urllib.request.urlopen(req)
    respData=resp.read()    
    soup=BeautifulSoup(respData)
    tags=soup(ppalTag)
    direcciones=[]
    cont=0
    for tag in tags:
     aux=tag.get(scundTag)
     if aux != None:
           if "www" in aux:
                direcciones.append(aux)
                cont+=1
    return direcciones


def imagenes(url):
    headers={}
    headers['User-Agent']='Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 safari/537.17'
    req=urllib.request.Request(url,headers=headers)
    resp=urllib.request.urlopen(req)
    respData=resp.read()    
    soup=BeautifulSoup(respData)
    imagenes=soup.findAll('img')
    vectorImagenes=[]
    for image in imagenes:
        try:
            vectorImagenes.append(image['src'])
        except Exception as e :
            print(e)


                    
    
    return vectorImagenes


if __name__ == '__main__':
    main()

        
