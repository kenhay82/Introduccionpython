import matplotlib.pyplot as plt

def generarGrafica(dataFrame,nombreGrafica):
    rutaArchivo = f"./assets/graphs/{nombreGrafica}.png"

    #Filtro Medellín
    '''
    #Agrupar datos del DataFrame según el analisís que quiera graficar
    ## EJE X= (), EJE Y=values[]
    plantacionPromedioMedellin = dataFrame.groupby('Vereda')['Arboles'].mean()
    ##print(preciosPromedioPais)
    #Generando lista de colores.
    colores=['#CEC627','#C8E675','#B88836']
    #1. Generar una FIGURA 
    plt.figure(figsize=(10,10))
    #2. Generar el tipo de GRAFICA que se deasea
    ## EJE X= index, EJE Y=values
    plt.bar(plantacionPromedioMedellin.index,plantacionPromedioMedellin.values,color=colores)
    #3. Muestrar la grafica
    #plt.show()
    #4. Agregar un titulo a la tabla
    plt.title('Veredas con plantaciones superiores a 200 Arboles en Medellín')
    #5. Agregar un nombre al EJE X
    plt.xlabel('Vereda')
    #6. Agregar un nombre al EJE Y
    plt.ylabel('Arboles')
    #7. Activar el grid
    plt.grid(True)
    #8. Inclinar los X labels
    plt.xticks(rotation=38)
    #9. Guardar nuestra Gráfica
    plt.savefig(rutaArchivo)
    '''

    #Filtro SantaFe
    ''' 
    plantacionSantaFe = dataFrame.groupby('evento')['Arboles'].mean()
    ##print(preciosPromedioPais)
    #0. Generando lista de colores.
    colores=['#CEC627','#C8E675','#B88836']
    #1. Generar una FIGURA 
    plt.figure(figsize=(15,15))
    #2. Generar el tipo de GRAFICA que se deasea
    ## EJE X= index, EJE Y=values
    plt.bar(plantacionSantaFe.index,plantacionSantaFe.values, color=colores)
    #3. Muestrar la grafica
    #plt.show()
    #4. Agregar un titulo a la tabla
    plt.title('Arboles plantados por Evento en el Municipio de Santa Fe Antioquia')
    #5. Agregar un nombre al EJE X
    plt.xlabel('Evento')
    #6. Agregar un nombre al EJE Y
    plt.ylabel('Arboles')
    #7. Activar el grid
    plt.grid(True)

    #8. Inclinar los X labels
    plt.xticks(rotation=38)

    #9. Guardar nuestra Gráfica
    plt.savefig(rutaArchivo)
    '''
    
    #Filtro El Bagre
    '''
    plantacionElBagre = dataFrame.groupby('Vereda')['Arboles'].mean()
    ##print(preciosPromedioPais)
    #0. Generando lista de colores.
    colores=['#CEC627','#C8E675','#B88836']
    #1. Generar una FIGURA 
    plt.figure(figsize=(15,15))
    #2. Generar el tipo de GRAFICA que se deasea
    ## EJE X= index, EJE Y=values
    plt.bar(plantacionElBagre.index,plantacionElBagre.values,color=colores)
    #3. Muestrar la grafica
    #plt.show()
    #4. Agregar un titulo a la tabla
    plt.title('Arboles plantados por Vereda en el Municipio de El Bagre')
    #5. Agregar un nombre al EJE X
    plt.xlabel('Vereda')
    #6. Agregar un nombre al EJE Y
    plt.ylabel('Arboles')
    #7. Activar el grid
    plt.grid(True)

    #8. Inclinar los X labels
    plt.xticks(rotation=38)

    #9. Guardar nuestra Gráfica
    plt.savefig(rutaArchivo)
    '''

    #Filtro Santa Rosa de Osos
    '''
    plantacionSantaRosa = dataFrame.groupby('evento')['Arboles'].mean()
    ##print(preciosPromedioPais)
    #0. Generando lista de colores.
    colores=['#CEC627','#C8E675','#B88836']
    #1. Generar una FIGURA 
    plt.figure(figsize=(15,15))
    #2. Generar el tipo de GRAFICA que se deasea
    ## EJE X= index, EJE Y=values
    plt.bar(plantacionSantaRosa.index,plantacionSantaRosa.values,color=colores)
    #3. Muestrar la grafica
    #plt.show()
    #4. Agregar un titulo a la tabla
    plt.title('Arboles plantados por evento en Las Cruces y Mina Vieja (Santa Rosa de Osos)')
    #5. Agregar un nombre al EJE X
    plt.xlabel('Evento')
    #6. Agregar un nombre al EJE Y
    plt.ylabel('Arboles')
    #7. Activar el grid
    plt.grid(True)

    #8. Inclinar los X labels
    plt.xticks(rotation=38)

    #9. Guardar nuestra Gráfica
    plt.savefig(rutaArchivo)
    '''

    #Filtro Yondó
    '''
    plantacionYondo = dataFrame.groupby('Vereda')['Arboles'].sum()
    ##print(preciosPromedioPais)
    #0. Generando lista de colores.
    colores=['#CEC627','#C8E675','#B88836']
    #1. Generar una FIGURA 
    plt.figure(figsize=(15,15))
    #2. Generar el tipo de GRAFICA que se deasea
    ## EJE X= index, EJE Y=values
    plt.bar(plantacionYondo.index,plantacionYondo.values,color=colores)
    #3. Muestrar la grafica
    #plt.show()
    #4. Agregar un titulo a la tabla
    plt.title('Arboles plantados en Yondó')
    #5. Agregar un nombre al EJE X
    plt.xlabel('Veredas')
    #6. Agregar un nombre al EJE Y
    plt.ylabel('Arboles')
    #7. Activar el grid
    plt.grid(True)

    #8. Inclinar los X labels
    plt.xticks(rotation=38)

    #9. Guardar nuestra Gráfica
    plt.savefig(rutaArchivo)
    '''