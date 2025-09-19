import pandas as pd
import matplotlib.pyplot as plt

data_clients = pd.read_csv("clientes.csv")
avg_expenses = data_clients.groupby("cidade")["gasto_total"].mean()
print(avg_expenses)


avg_expenses.plot(kind="bar", color="skyblue", edgecolor="black")

# Títulos e legendas
plt.title("Gasto médio por cidade")
plt.xlabel("Cidade")
plt.ylabel("Gasto médio (R$)")

# Mostrar gráfico
plt.show()