import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

# Inicializar o gerador de dados Faker (com localização para Português de Portugal)
fake = Faker('pt_PT')

# --- Definição de Parâmetros ---
NUM_VENDAS = 50000
NUM_PRODUTOS = 500
NUM_CLIENTES = 10000
NUM_CAMPANHAS = 100
DATA_INICIO_DADOS = datetime(2023, 1, 1)
DATA_FIM_DADOS = datetime(2024, 12, 31)

# --- 1. Gerar Dados de Produtos ---
print("A gerar dados de produtos...")
categorias = ['Smartphones', 'Portáteis', 'Tablets', 'Acessórios', 'Wearables', 'Gaming', 'TVs']
marcas = ['Samsung', 'Apple', 'Xiaomi', 'HP', 'Dell', 'Lenovo', 'Sony', 'LG', 'JBL', 'Logitech', 'Nintendo', 'Microsoft']

produtos_data = []
for i in range(NUM_PRODUTOS):
    id_produto = f'PROD-{i+1:04d}'
    nome_produto = fake.catch_phrase() + ' ' + random.choice(categorias) # Nome mais criativo
    categoria = random.choice(categorias)
    marca = random.choice(marcas)
    preco_unitario = round(random.uniform(20, 2000), 2)
    custo_unitario = round(preco_unitario * random.uniform(0.5, 0.8), 2) # Custo entre 50% e 80% do preço
    produtos_data.append([id_produto, nome_produto, categoria, marca, preco_unitario, custo_unitario])

df_produtos = pd.DataFrame(produtos_data, columns=[
    'ID_Produto', 'Nome_Produto', 'Categoria', 'Marca', 'Preco_Unitario', 'Custo_Unitario'
])
df_produtos.to_csv('data/produtos.csv', index=False, encoding='utf-8')
print(f"Ficheiro 'produtos.csv' criado com {len(df_produtos)} registos.")

# --- 2. Gerar Dados de Campanhas de Marketing ---
print("A gerar dados de campanhas de marketing...")
canais_marketing = ['Google Ads', 'Facebook Ads', 'Email Marketing', 'Influencers', 'Parcerias']
periodo_campanha_max = timedelta(days=90) # Campanhas duram no máximo 90 dias

marketing_campanhas_data = []
for i in range(NUM_CAMPANHAS):
    id_campanha = f'CAMP-{i+1:03d}'
    nome_campanha = fake.word().capitalize() + ' ' + fake.word().capitalize() + ' Campanha'
    canal_marketing = random.choice(canais_marketing)
    
    data_inicio = DATA_INICIO_DADOS + timedelta(days=random.randint(0, (DATA_FIM_DADOS - DATA_INICIO_DADOS).days - periodo_campanha_max.days))
    data_fim = data_inicio + timedelta(days=random.randint(7, periodo_campanha_max.days)) # Min 7 dias
    
    custo_campanha = round(random.uniform(500, 50000), 2)
    
    # Simular cliques e impressões proporcionalmente ao custo
    impressoes = int(custo_campanha * random.uniform(50, 200))
    cliques = int(impressoes * random.uniform(0.01, 0.05)) # CTR entre 1% e 5%
    
    # Vendas atribuídas: um pouco aleatório, mas com correlação com custo/cliques
    # Vamos gerar vendas atribuidas que podem ser 0, para simular campanhas ineficazes
    vendas_atribuidas = int(cliques * random.uniform(0.01, 0.1)) if random.random() < 0.9 else 0 # 1% a 10% de conversão do clique, 10% de chance de ser 0
    
    marketing_campanhas_data.append([
        id_campanha, nome_campanha, canal_marketing, 
        data_inicio.strftime('%Y-%m-%d'), data_fim.strftime('%Y-%m-%d'), 
        custo_campanha, impressoes, cliques, vendas_atribuidas
    ])

df_marketing_campanhas = pd.DataFrame(marketing_campanhas_data, columns=[
    'ID_Campanha', 'Nome_Campanha', 'Canal_Marketing', 'Data_Inicio', 'Data_Fim',
    'Custo_Campanha', 'Impressoes', 'Cliques', 'Vendas_Atribuidas'
])
df_marketing_campanhas.to_csv('data/marketing_campanhas.csv', index=False, encoding='utf-8')
print(f"Ficheiro 'marketing_campanhas.csv' criado com {len(df_marketing_campanhas)} registos.")

# --- 3. Gerar Dados de Vendas ---
print("A gerar dados de vendas...")
canais_venda = ['Online', 'App Móvel', 'Loja Física']
regioes_cliente = ['Lisboa', 'Porto', 'Coimbra', 'Braga', 'Faro', 'Aveiro', 'Setúbal']

vendas_data = []
for i in range(NUM_VENDAS):
    id_venda = f'VENDA-{i+1:05d}'
    
    # Data da venda dentro do período definido
    data_venda = DATA_INICIO_DADOS + timedelta(days=random.randint(0, (DATA_FIM_DADOS - DATA_INICIO_DADOS).days))
    
    # Escolher um produto aleatório
    produto_aleatorio = df_produtos.sample(1).iloc[0]
    id_produto = produto_aleatorio['ID_Produto']
    preco_unitario_venda = produto_aleatorio['Preco_Unitario'] # Usar o preço definido para o produto
    
    quantidade = random.randint(1, 5) # Vender entre 1 e 5 unidades
    total_venda = round(quantidade * preco_unitario_venda, 2)
    
    id_cliente = f'CLI-{random.randint(1, NUM_CLIENTES):05d}'
    canal_venda = random.choice(canais_venda)
    regiao_cliente = random.choice(regioes_cliente)
    
    # Adicionar alguns dados ausentes (simular erros ou falhas na recolha)
    if random.random() < 0.01: # 1% de chance de ter preço unitário ausente
        preco_unitario_venda = np.nan
    if random.random() < 0.005: # 0.5% de chance de ter região ausente
        regiao_cliente = np.nan
    
    vendas_data.append([
        id_venda, data_venda.strftime('%Y-%m-%d %H:%M:%S'), id_produto, quantidade,
        preco_unitario_venda, total_venda, id_cliente, canal_venda, regiao_cliente
    ])

df_vendas = pd.DataFrame(vendas_data, columns=[
    'ID_Venda', 'Data_Venda', 'ID_Produto', 'Quantidade', 'Preco_Unitario',
    'Total_Venda', 'ID_Cliente', 'Canal_Venda', 'Regiao_Cliente'
])
df_vendas.to_csv('data/vendas.csv', index=False, encoding='utf-8')
print(f"Ficheiro 'vendas.csv' criado com {len(df_vendas)} registos.")

print("\nGeração de dados concluída com sucesso!")
print("Os ficheiros foram guardados na pasta 'data/'.")