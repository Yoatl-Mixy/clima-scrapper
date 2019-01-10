import requests
import bs4
import geocoder
from pygeocoder import Geocoder

gmaps = Geocoder(api_key='AIzaSyC0dFtlqf4bBU5awtGDXWdCNW3Zrey_WTE')

def funcionUbicacion(x):
        localidad=x
        localidad=localidad.split()
        print(localidad)
        localidad=[x for x in localidad if not any(c.isdigit() for c in x)]
        print(localidad)
        localidad=' '.join(localidad[-5:])
        print(localidad)
        peticion='clima en '
        print(peticion+localidad)
        r = requests.get("https://www.google.com.mx/search?q="+peticion.replace(' ','+')+localidad.replace(' ','+'),headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'})
        html=r.text
        soup= bs4.BeautifulSoup(html, "html.parser")
        cuadro=soup.find('div',attrs={'id':'wob_dcp'})
        cuadro2=soup.find('span',attrs={'class':'wob_t'})
        cuadro3=soup.find('span',attrs={'id':'wob_pp'})
        print(cuadro3.text)
        print(type(cuadro3.text))
        clima3=cuadro3.text
        clima3=clima3.replace('%','')
        clima3=int(clima3)
        if clima3 > 60:
            clima3='con una probabilidad de '+clima3+' por ciento de lluvia'
        elif clima3 < 10:
            clima3='sin probabilidad de lluvia'
        else:
            clima3='con una baja probabilidad de lluvia'
       
        try:
            if cuadro.text and cuadro2.text:
                # ubicacion=cuadro.text
                # ubicacion=ubicacion.replace(' h ',' horas ').replace(' min ',' minutos ').replace('(','a una distancia de ').replace('km','kilometros').replace(')','').replace('-','de autopista').replace('Av.','Avenida').replace("\xa0",'').replace('Ã©','é').replace('/',' ').replace(' Av ',' Avenida ')
                # return 'Te encuentras a un tiempo aproximado de '+ubicacion

                print(cuadro.text)
                clima1=cuadro.text
                print(cuadro2.text)
                clima2=cuadro2.text
                return {'operacion': 'respuesta','status':'success', 'respuesta': 'En '+localidad+' se encuentra '+clima1+'a una temperatura de '+clima2+' grados centigrados '+clima3,'accion': 'mapa','microfono':1}
        except AttributeError:
            return 'No hay Cuados'
            # return {'operacion': 'respuesta','status':'success', 'respuesta': 'No hay Respuesta','accion': 'mapa','microfono':0}
def funcionCoordenadas(x):
    vec_ubicacion=['19.3579615','-99.2738635']
    results = gmaps.reverse_geocode(float(vec_ubicacion[0].strip().strip("'")), float(vec_ubicacion[1].strip().strip("'")))
    print(results.route)
    ubicacionActual=results.neighborhood+', '+results.locality
    print(ubicacionActual)
    peticion='clima en '+ubicacionActual
    print(peticion)
    r = requests.get("https://www.google.com.mx/search?q="+peticion.replace(' ','+'),headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'})
    html=r.text
    soup= bs4.BeautifulSoup(html, "html.parser")
    cuadro=soup.find('div',attrs={'id':'wob_dcp'})
    cuadro2=soup.find('span',attrs={'class':'wob_t'})
    cuadro3=soup.find('span',attrs={'id':'wob_pp'})
    print(cuadro3.text)
    print(type(cuadro3.text))
    clima3=cuadro3.text
    clima3=clima3.replace('%','')
    clima3=int(clima3)
    if clima3 > 60:
        clima3='con una probabilidad de '+clima3+' por ciento de lluvia'
    elif clima3 < 10:
        clima3='sin probabilidad de lluvia'
    else:
        clima3='con una baja probabilidad de lluvia'
    try:
        if cuadro.text and cuadro2.text:
            print(cuadro.text)
            clima1=cuadro.text
            print(cuadro2.text)
            clima2=cuadro2.text
            return 'En '+ubicacionActual+' se encuentra '+clima1+'a una temperatura de '+clima2+' grados centigrados '+clima3
    except AttributeError:
        return 'Lo siento. no encontre información'

while 1:
    x=input('>> ')
    print(funcionCoordenadas(x))

