import pandas as pd
import matplotlib.pyplot as plt

#Utilizando a biblioteca Pandas, é possível realizar um tratamento simples na base
#de dados utilizando os parâmetros adequados
base = pd.read_csv('Arquivo', skiprows=33, delimiter='\t')

#Após a leitura numa variável, utiliza-se a função DataFrame para realizar o tratamento
df = pd.DataFrame(base)

df_trat = df.loc[1050:] #Notação para iniciar a partir de determinado valor de linha

#Plot Gráfico
df_trat.plot()
plt.show()
