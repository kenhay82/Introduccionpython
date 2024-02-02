#1. Importar el paquete o paquetes con los que voy a analizar la informacion
import pandas as pd
from analysis.helpers.creacionTabla import crearTabla
from analysis.helpers.creacionGraficas import generarGrafica

def analizarSiembra():
    #2. Sin importar la fuente (sql, xls, JSON, csv...)
    #crear una tabla tabulada que se llama DATAFRAME
    tabla=pd.read_csv('./data/Siembras.csv')
    #print(tabla)
    #crearTabla(tabla,"Siembras")

    #3. filtros para limpiar o seleccionar datos
    #print(tabla.head(20)) 
    #primeros N registros
    #print(tabla.tail())

    #Filtro para obtener las siembras en Medellín que superan los 200 Arboles
    #filtroMedellin200 = tabla.query("(Ciudad=='Medellín' and Arboles>200)")
    #print(filtroMedellin200)
    #crearTabla(filtroMedellin200,"filtroMedellin200")
    #generarGrafica(filtroMedellin200,"filtroMedellin200")

    #Filtro Santa fe Antioquia: Veredas Paso real y Tanusco arriba
    #filtroSantaFe = tabla.query("(Ciudad=='Santa Fe de Antioquia' and (Vereda=='Tonusco Arriba' or Vereda=='Paso Real'))")
    #print(filtroSantaFe)
    #crearTabla(filtroSantaFe,'filtroSantaFe')
    #generarGrafica(filtroSantaFe,'filtroSantaFe')

    #Filtro El Bagre > 60 Arboles
    #filtroElBagre = tabla.query("(Ciudad=='El Bagre' and Arboles>60)")
    #print(filtroElBagre)
    #crearTabla(filtroElBagre,'filtroElBagre')
    #generarGrafica(filtroElBagre,'filtroElBagre')

    #Filtro Santa Rosa de Osos
    #filtroSantaRosas = tabla.query("(Ciudad=='Santa Rosa de Osos' and (Vereda=='Las Cruces' or Vereda=='Mina Vieja'))")
    #print(filtroSantaRosas)
    #crearTabla(filtroSantaRosas,'filtroSantaRosas')
    #generarGrafica(filtroSantaRosas,'filtroSantaRosas')

    #Filtro Yondó
    filtroYondo = tabla.query("(Ciudad=='Yondó')")
    print(filtroYondo)
    crearTabla(filtroYondo,'filtroYondo')
    generarGrafica(filtroYondo,'filtroYondo')
