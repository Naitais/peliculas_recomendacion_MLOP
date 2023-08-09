import csv, pandas as pd, json, numpy as np

#levanta datasets y los transforma en dataframes
def cargaCsvToDataFrame(dataset, carpeta_ubicacion): #toma el dataset y la carpeta que lo contiene
    path=f"{carpeta_ubicacion}//{dataset}.csv"
    list = [] #primero cargo el dataset que uso en esta funcion utilizando with open
    with open(path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            list.append(row)
            #transformo resultado en df
    df=pd.DataFrame(list)
    return df

#desanida columna y devuelve un dataframe
def desanidarColumna(columna):
    lista = []
    listaDict=[]
    counter=0
    for k, v in columna.items():
        if isinstance(v, str):
            lista.append(v)
        else:
            lista.append(None)
    for i in lista:   
                try:
                    i=json.loads(lista[counter].replace("'", '"'))
                    listaDict.append(i)
                    counter+=1
                except:
                    listaDict.append(None)
                    counter+=1
    listaDict=pd.json_normalize(listaDict)
    return listaDict

def desanidarVariasColumnas(columna):
    lista=[]
    for col in columna:            
        #normalizo cada columna
        colAnidada=pd.json_normalize(columna[col])
        lista.append(colAnidada) #meto cada columna en una lista

        #armo un df concatenando cada columna de la lista
        nuevoDF=pd.concat(lista)
    return nuevoDF

#esta funcion crea nuevos dfs para usarlos en las funciones de fastaPI segun las columnas que necesito
def creaDfFuncionesFastAPI(columnas, dfMovies):
    nuevoDF = []
    for i in dfMovies["movie_title"]:
        row=dfMovies.loc[dfMovies.movie_title == i, columnas]
        nuevoDF.append(row)
    #usando concatenar si ambos dfs estan en una lista, se unen facilmente
    nuevoDF = pd.concat(nuevoDF, ignore_index=True)
    nuevoDF = nuevoDF.dropna()
    return nuevoDF