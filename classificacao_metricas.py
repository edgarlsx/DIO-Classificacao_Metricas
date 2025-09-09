# 📌 Importação de bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

# 📊 Função para calcular métricas de classificação
def calcular_metricas(vp, fn, fp, vn):
    total = vp + fn + fp + vn

    # Cálculo das métricas com tratamento para divisão por zero
    acuracia = (vp + vn) / total if total != 0 else 0
    sensibilidade = vp / (vp + fn) if (vp + fn) != 0 else 0
    especificidade = vn / (vn + fp) if (vn + fp) != 0 else 0
    precisao = vp / (vp + fp) if (vp + fp) != 0 else 0
    f1_score = 2 * (precisao * sensibilidade) / (precisao + sensibilidade) if (precisao + sensibilidade) != 0 else 0

    # Dicionário com resultados
    metricas = {
        'VP (Verdadeiros Positivos)': vp,
        'FN (Falsos Negativos)': fn,
        'FP (Falsos Positivos)': fp,
        'VN (Verdadeiros Negativos)': vn,
        'Total de Elementos (N)': total,
        'Acurácia': round(acuracia, 4),
        'Sensibilidade (Recall)': round(sensibilidade, 4),
        'Especificidade': round(especificidade, 4),
        'Precisão': round(precisao, 4),
        'F1-Score': round(f1_score, 4)
    }

    return metricas

# 🧪 Valores de exemplo da matriz de confusão
vp = 70
fn = 30
fp = 10
vn = 90

# ✅ Cálculo das métricas
resultado = calcular_metricas(vp, fn, fp, vn)

# 📋 Exibir os resultados em tabela com pandas
df_metricas = pd.DataFrame(resultado.items(), columns=['Métrica', 'Valor'])
print(df_metricas)

# 📊 Visualização gráfica das métricas (exceto valores brutos da matriz)
metricas_plot = df_metricas[~df_metricas['Métrica'].str.startswith(('VP', 'FP', 'FN', 'VN', 'Total'))]

plt.figure(figsize=(10, 6))
plt.barh(metricas_plot['Métrica'], metricas_plot['Valor'], color='steelblue')
plt.xlabel('Valor')
plt.title('Métricas de Avaliação de Classificação')
plt.xlim(0, 1)
plt.grid(axis='x', linestyle='--', alpha=0.7)
for i, v in enumerate(metricas_plot['Valor']):
    plt.text(v + 0.01, i, str(v), va='center', fontsize=10)
plt.tight_layout()
plt.show()
