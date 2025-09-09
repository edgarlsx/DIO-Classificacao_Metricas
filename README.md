# 📊 Avaliação de Modelos de Classificação com Métricas de Desempenho

Este projeto em Python tem como objetivo demonstrar, de forma prática e visual, como calcular as principais métricas de avaliação para modelos de classificação utilizando uma matriz de confusão arbitrária.

---

## ✅ Funcionalidades

- Cálculo automático das seguintes métricas:
  - Acurácia
  - Sensibilidade (Recall)
  - Especificidade
  - Precisão
  - F1-Score
- Visualização dos resultados em formato de tabela com `pandas`
- Gráfico de barras para facilitar a interpretação dos resultados com `matplotlib`

---

## 🧠 Conceitos Aplicados

Este projeto utiliza uma **matriz de confusão** para ilustrar o comportamento das métricas em um problema de classificação binária.  
Os componentes da matriz são:

| Classe Real | Classe Predita Positiva | Classe Predita Negativa |
|-------------|--------------------------|--------------------------|
| **Positivo** | VP (Verdadeiro Positivo) | FN (Falso Negativo)     |
| **Negativo** | FP (Falso Positivo)      | VN (Verdadeiro Negativo)|

---

## 📦 Bibliotecas Utilizadas

- `pandas` → para organização dos dados em tabelas
- `matplotlib` → para visualização gráfica

---


## 🧪 Exemplo de Dados Usados

No script, os seguintes valores foram definidos como exemplo:

VP = 70
FN = 30
FP = 10
VN = 90

---

## 📈 Exemplo de Saída
Tabela
Métrica	Valor
Acurácia	0.80
Sensibilidade (Recall)	0.70
Especificidade	0.90
Precisão	0.875
F1-Score	0.7778

---

## 📈 Gráfico
