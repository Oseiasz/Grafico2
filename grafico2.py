
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

# Dados fornecidos
data_rescisoes = {
    'Código Cargo': [
        516, 989, 1080, 455, 455, 455, 1, 455, 1386, 1386, 1386, 516, 1386, 1386, 1386, 596, 1386, 989, 989, 1386, 1386, 
        455, 989, 989, 1386, 1386, 1386, 1372, 989, 455, 1415, 229, 229, 231, 229, 231, 229, 596, 1415, 1415, 1386, 1386, 
        1386, 1369, 422, 989, 330, 1386, 1, 1638, 476, 476, 476, 476
    ],
    'Cargo': [
        'BALCONISTA', 'FISCAL DE PREV DE PERDAS', 'GERENTE DE FRENTE DE LOJA', 'AUXILIAR DE LOJA II', 'AUXILIAR DE LOJA II', 
        'AUXILIAR DE LOJA II', 'ACOUGUEIRO', 'AUXILIAR DE LOJA II', 'REPOSITOR', 'REPOSITOR', 'REPOSITOR', 'BALCONISTA', 
        'REPOSITOR', 'REPOSITOR', 'REPOSITOR', 'CONFERENTE', 'REPOSITOR', 'FISCAL DE PREV DE PERDAS', 'FISCAL DE PREV DE PERDAS', 
        'REPOSITOR', 'REPOSITOR', 'AUXILIAR DE LOJA II', 'FISCAL DE PREV DE PERDAS', 'FISCAL DE PREV DE PERDAS', 'REPOSITOR', 
        'REPOSITOR', 'REPOSITOR', 'PROMOTOR DE VENDAS', 'FISCAL DE PREV DE PERDAS', 'AUXILIAR DE LOJA II', 'SEPARADOR', 'APRENDIZ', 
        'APRENDIZ', 'APRENDIZ', 'APRENDIZ', 'APRENDIZ', 'APRENDIZ', 'CONFERENTE', 'SEPARADOR', 'SEPARADOR', 'REPOSITOR', 'REPOSITOR', 
        'REPOSITOR', 'PROMOTOR DE MARCAS', 'AUXILIAR DE DEPOSITO', 'FISCAL DE PREV DE PERDAS', 'ASSISTENTE DE MARKETING', 
        'REPOSITOR', 'ACOUGUEIRO', 'VENDEDOR CHAO DE LOJA - COMISSIONADO', 'AUXILIAR DE PRODUCAO', 'AUXILIAR DE PRODUCAO', 
        'AUXILIAR DE PRODUCAO', 'AUXILIAR DE PRODUCAO'
    ],
    'Data Admissão': [
        '09/03/2023', '09/03/2023', '17/03/2023', '23/03/2023', '23/03/2023', '23/03/2023', '23/03/2023', '23/03/2023', 
        '03/04/2023', '03/04/2023', '10/04/2023', '10/04/2023', '10/04/2023', '10/04/2023', '10/04/2023', '10/04/2023', 
        '10/04/2023', '12/04/2023', '12/04/2023', '20/04/2023', '02/05/2023', '02/05/2023', '06/06/2023', '06/06/2023', 
        '15/06/2023', '17/06/2023', '20/06/2023', '24/06/2023', '15/07/2023', '26/07/2023', '05/08/2023', '09/08/2023', 
        '09/08/2023', '09/08/2023', '09/08/2023', '09/08/2023', '09/08/2023', '16/08/2023', '28/08/2023', '11/11/2023', 
        '24/11/2023', '14/12/2023', '22/12/2023', '27/12/2023', '07/02/2024', '26/02/2024', '20/04/2024', '26/04/2024', 
        '10/05/2024', '17/05/2024', '03/06/2024', '06/06/2024', '25/07/2024', '25/07/2024'
    ],
    'Data Rescisão': [
        '04/07/2024', '01/07/2024', '12/08/2024', '13/08/2024', '01/08/2024', '22/08/2024', '19/08/2024', '01/07/2024', 
        '12/08/2024', '04/07/2024', '09/08/2024', '01/08/2024', '04/07/2024', '16/07/2024', '01/08/2024', '05/08/2024', 
        '09/08/2024', '14/08/2024', '01/07/2024', '13/08/2024', '06/08/2024', '31/08/2024', '01/07/2024', '01/07/2024', 
        '18/07/2024', '01/08/2024', '08/07/2024', '13/08/2024', '01/07/2024', '17/07/2024', '06/08/2024', '16/08/2024', 
        '16/08/2024', '12/08/2024', '16/08/2024', '01/08/2024', '16/08/2024', '08/07/2024', '05/08/2024', '05/07/2024', 
        '14/08/2024', '05/07/2024', '08/07/2024', '23/07/2024', '10/08/2024', '09/08/2024', '18/07/2024', '17/07/2024', 
        '07/08/2024', '09/07/2024', '04/07/2024', '19/07/2024', '19/08/2024', '09/08/2024'
    ]
}

# Criar o DataFrame
df_rescisoes = pd.DataFrame(data_rescisoes)

# Contagem dos cargos
cargo_counts_rescisoes = Counter(df_rescisoes['Cargo'])

# Gerando o gráfico
plt.figure(figsize=(10, 6))  # Tamanho ajustado
plt.bar(cargo_counts_rescisoes.keys(), cargo_counts_rescisoes.values(), color='lightcoral')
plt.xticks(rotation=90)
plt.title('Distribuição de Rescisões por Cargo')
plt.xlabel('Cargo')
plt.ylabel('Número de Rescisões')
plt.tight_layout()

# Exibir o gráfico
plt.show()
