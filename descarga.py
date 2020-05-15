import requests
import csv
from datetime import datetime
def Descargaindividual(link):
    link="https://www.gef.com.co/wcsstore/CrystalCo_CAT_AS/"+str(link)
    now=datetime.now()
    url_imagen = link # El link de la imagen
    print(link)
    nombre_local_imagen = "img"+str(now.minute)+"_"+str(now.second)+"_"+str(now.microsecond)+".jpg" # El nombre con el que queremos guardarla
    try:
        imagen = requests.get(url_imagen).content
        with open(str(nombre_local_imagen), 'wb') as handler:
	        handler.write(imagen)
        pass
            
    except Exception as e:
        print(e)
        pass
    pass
    
def leerArchivo(url):
    vector=[]
    with open(url, newline='') as File:  
        reader = csv.reader(File)
        for row in reader:
            vector.append(row)
            
    return vector
    pass
if  __name__ == '__main__':
   # main()
    vector=leerArchivo("C:/Users/didie/Desktop/Imagenes.txt")
    for dir in vector:
        for i in dir:
            Descargaindividual(i)
            pass

        pass
    print('termino!!')
  # Descargaindividual("https://www.gef.com.co/wcsstore/CrystalCo_CAT_AS /Gef/ES-CO/Imagenes/Masculino_Exterior/POLOS/Teo/1000x1263/Camiseta-Polo-Hombres-Teo-Negro-791-Frente-GEF.jpg")