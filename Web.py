import sys
import urllib.request
from bs4 import BeautifulSoup
import requests
from datetime import datetime

def main():
   
    vectorLinks=[]
    vectorImagenes=[]
    vectorLinks=Links('https://www.falabella.com/falabella-cl/category/cat1320012/Chalecos-y-Sweaters','a','href')#aqui va la direccion
    
    
    for url in vectorLinks:
        vectorImagenes.append(imagenes(url))    
    
    for imagen in vectorImagenes:
        Descarga(imagen)
        #print(imagen)
        
     


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
            if "http" in image['src'] :
                vectorImagenes.append(image['src'])
                pass
            
        except Exception as e :
            print(e,'/n')


                    
    
    return vectorImagenes


def Descarga(link):
    now=datetime.now()

    for url in link:
        url_imagen = url # El link de la imagen
        nombre_local_imagen = "img"+str(now.minute)+"_"+str(now.second)+"_"+str(now.microsecond)+".png" # El nombre con el que queremos guardarla
        try:
            imagen = requests.get(url_imagen).content
            with open(str(nombre_local_imagen), 'wb') as handler:
	            handler.write(imagen)
            pass

            pass
        except Exception as e:
            print(e)
            pass
    pass
    

if __name__ == '__main__':
    main()