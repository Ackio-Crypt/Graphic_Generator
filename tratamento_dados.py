import pandas as pd
import matplotlib as plt

base = pd.read_csv('/home/ackio/Documentos/Projects ACK/Python/Gerador_Graf/Graphic_Generator/indice.csv')
df = pd.DataFrame(base)
print(df['NumAno'])



