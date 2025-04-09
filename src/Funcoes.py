import pandas as pd
import matplotlib.pyplot as plt

def gerar_histogramas(pais, dados_pais):  # função que gera histogramas

    plt.figure(figsize=(12, 6))

    # histograma temperatura diária
    plt.subplot(1, 2, 1)
    plt.hist(
        dados_pais["Average surface temperature daily"],
        bins=30,
        color="green",
        edgecolor="black",
    )
    plt.title(f"Média Diária - {pais}")
    plt.xlabel("Temperatura (°C)")
    plt.ylabel("Frequência")

    # histograma temperatura mensal
    plt.subplot(1, 2, 2)
    plt.hist(
        dados_pais["Average surface temperature monthly"],
        bins=30,
        color="red",
        edgecolor="black",
    )
    plt.title(f"Média Mensal - {pais}")
    plt.xlabel("Temperatura (°C)")

    plt.tight_layout()
    plt.show()
    
    
def identificar_outliers(coluna, peso):  # função para identificar outliers
    Q1 = coluna.quantile(0.25)
    Q3 = coluna.quantile(0.75)

    IQR = Q3 - Q1
    limite_inferior = Q1 - peso * IQR
    limite_superior = Q3 + 3 * IQR

    outliers = coluna[(coluna < limite_inferior) | (coluna > limite_superior)]
    return outliers


def remover_outliers(dados, peso):
    Q1 = dados.quantile(0.25)
    Q3 = dados.quantile(0.75)
    IQR = Q3 - Q1
    limite_inferior = Q1 - peso * IQR
    limite_superior = Q3 + 3 * IQR
    return dados[(dados >= limite_inferior) & (dados <= limite_superior)]

def gerar_boxplot(pais, dados_pais): # função que gera boxplot

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.boxplot(dados_pais["Average surface temperature daily"])
    plt.title(f"Boxplot - Temperatura diária - {pais}")
    plt.xlabel("Temperatura")

    plt.subplot(1, 2, 2)
    plt.boxplot(dados_pais["Average surface temperature monthly"])
    plt.title(f"Boxplot - Temperatura mensal - {pais}")
    plt.xlabel("Temperatura")

    plt.show()

## Entrega complemento de dados

def analisar_periodo(dataframe, coluna_data):
   
    dataframe['data_datetime'] = pd.to_datetime(dataframe[coluna_data])
    
    dataframe['ano_mes'] = dataframe['data_datetime'].dt.to_period('M')
    
    mes_inicial = dataframe['ano_mes'].min()
    mes_final = dataframe['ano_mes'].max()
    
    print(f"\nPeríodo de análise:")
    print(f"Primeiro mês: {mes_inicial}")
    print(f"Último mês: {mes_final}")
    
    return mes_inicial, mes_final
    

def identificar_meses_faltantes(dataframe):
    mes_inicial = dataframe['ano_mes'].min()
    mes_final = dataframe['ano_mes'].max()
    
    todos_os_meses = pd.period_range(start=mes_inicial, end=mes_final, freq='M')
    
    meses_existentes = dataframe['ano_mes'].unique()
    
    meses_faltantes = todos_os_meses.difference(meses_existentes)
    
    print(f"Numero de meses faltante: {len(meses_faltantes)}")
    print("Meses faltante: ")
    for mes in meses_faltantes:
        print (str(mes))

    return meses_faltantes

def interpolar_dados(dataframe):

    dataframe['Average surface temperature daily'] = dataframe['Average surface temperature daily'].interpolate(method='linear')
    dataframe['Average surface temperature monthly'] = dataframe['Average surface temperature monthly'].interpolate(method='linear')
    
    return dataframe

def gerar_histogramas_interpolados(pais, dados_pais):
    
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.hist(
        dados_pais["Average surface temperature daily"],
        bins=30,
        color="green",
        edgecolor="black",
    )
    plt.title(f"Média Diária Interpolada - {pais}")
    plt.xlabel("Temperatura (°C)")
    plt.ylabel("Frequência")


    plt.subplot(1, 2, 2)
    plt.hist(
        dados_pais["Average surface temperature monthly"],
        bins=30,
        color="red",
        edgecolor="black",
    )
    plt.title(f"Média Mensal Interpolada - {pais}")
    plt.xlabel("Temperatura (°C)")

    plt.tight_layout()
    plt.show()

