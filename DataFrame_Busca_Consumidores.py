import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
 
# Gerando dados aleatórios
np.random.seed(0)
datas = pd.date_range(start='1/1/2023', end='12/1/2023', freq='MS')
visitas = np.random.randint(100, 1000, size=(12))

 
# Criando um DataFrame de visitas ao site por data
dados = pd.DataFrame({'Data': datas, 'Visitas': visitas})
print(dados)

# Criando um gráfico de linha das visitas mensais ao site
plt.figure(figsize=(10, 6))
plt.plot(dados['Data'], dados['Visitas'], marker='o', linestyle='-', color='c')
plt.title('Visitas Mensais ao Site')
plt.xlabel('Data')
plt.ylabel('Número de Visitas')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Criando um DataFrame de visitas por região
regioes = ['Sudeste', 'Sul', 'Norte', 'Nordeste', 'Centro-Sul']
visitas = np.random.randint(100, 1000, size=(5))
dados = pd.DataFrame({'Região': regioes, 'Visitas': visitas})

# Criando um gráfico de barras das visitas por região
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
sns.barplot(x='Região', y='Visitas', data=dados, estimator=sum, ci=None, palette='muted')
plt.title('Visitas por Região')
plt.xlabel('Região')
plt.ylabel('Número de Visitas')
plt.show()