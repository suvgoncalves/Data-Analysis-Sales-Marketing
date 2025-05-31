import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta
import os

# Inicializar Faker para Português de Portugal
fake = Faker('pt_PT')

# --- Definições de Dados ---
num_clientes = 500
num_produtos = 150  # Aumentar para ter mais variedade de nomes únicos
num_vendas = 10000
num_campanhas = 50

# --- Geração de Dados de Clientes ---
clientes_data = []
for i in range(1, num_clientes + 1):
    clientes_data.append({
        'ID_Cliente': f'CLI-{i:04d}',
        'Nome_Cliente': fake.name(),
        'Email': fake.email(),
        'Localizacao': fake.city(),
        'Segmento': random.choice(['Consumidor', 'Empresarial', 'Premium', 'Pequena Empresa'])
    })
df_clientes = pd.DataFrame(clientes_data)

# --- Geração de Dados de Produtos ---
produtos_data = []

# Listas de palavras em português para nomes de produtos mais genéricos
adjetivos = [
    'Avançado', 'Básico', 'Compacto', 'Conectado', 'Digital', 'Económico',
    'Eficiente', 'Elegante', 'Ergonómico', 'Essencial', 'Inteligente', 'Leve',
    'Moderno', 'Multifunções', 'Novo', 'Pequeno', 'Portátil', 'Potente',
    'Premium', 'Robusto', 'Sem Fios', 'Silencioso', 'Ultra', 'Versátil'
]
substantivos_base = [
    'Sistema', 'Aparelho', 'Dispositivo', 'Unidade', 'Máquina', 'Ferramenta',
    'Componente', 'Acessório', 'Central', 'Kit', 'Módulo', 'Painel'
]
tipos_genericos = [
    'Portátil', 'Desktop', 'Tablet', 'Smartphone', 'Smartwatch', 'Console', 'Drone',
    'TV', 'Monitor', 'Impressora', 'Projetor', 'Câmara', 'Auscultadores', 'Colunas',
    'Teclado', 'Rato', 'Router', 'Webcam', 'Microfone', 'Disco Externo', 'Aspirador',
    'Frigorífico', 'Máquina de Lavar', 'Forno', 'Micro-ondas', 'Máquina de Café',
    'Segurança', 'Sensor', 'Iluminação', 'Termostato', 'Robô'
]

# Categorias de produtos
categorias = [
    'Eletrónica', 'Wearables', 'Smartphones', 'Portáteis', 'Periféricos',
    'Eletrodomésticos', 'Áudio e Vídeo', 'Gaming', 'Segurança', 'Tvs', 'Impressoras',
    'Redes', 'Armazenamento', 'Smart Home'
]

# Marcas
marcas = [
    'TechCorp', 'InnovateX', 'GlobalTech', 'ElectroZen', 'FuturaSystems',
    'HP', 'Dell', 'Lenovo', 'Samsung', 'LG', 'Sony', 'Apple', 'Xiaomi',
    'Microsoft', 'Philips', 'Bosch', 'Canon', 'Dyson', 'Logitech', 'Razer'
]

# Para garantir nomes de produtos únicos
nomes_produtos_gerados = set()

for i in range(1, num_produtos + 1):
    nome_produto = ""
    tentativas = 0
    # Gera um nome de produto único por combinação aleatória
    while nome_produto in nomes_produtos_gerados or not nome_produto:
        # Tenta gerar nomes de produto mais variados em português
        escolha_tipo = random.choice(tipos_genericos)
        if random.random() < 0.6: # 60% chance de um nome mais composto
            nome_produto = f"{random.choice(adjetivos)} {random.choice(substantivos_base)} {escolha_tipo}"
        else: # 40% chance de um nome mais simples
            nome_produto = f"{random.choice(adjetivos)} {escolha_tipo}"

        # Adiciona o nome da marca para o tornar mais único e realista
        marca_temp = random.choice(marcas)
        nome_produto = f"{marca_temp} {nome_produto}"

        nome_produto = nome_produto.replace('  ', ' ').strip() # Limpa espaços duplos
        tentativas += 1
        if tentativas > 2000: # Aumentar limite para gerar mais nomes únicos
            print(f"Aviso: Não foi possível gerar um nome de produto único após {tentativas} tentativas. Considere aumentar as listas de palavras ou o num_produtos.")
            break
    nomes_produtos_gerados.add(nome_produto)
    marca_produto = marca_temp # Usa a marca que foi usada para gerar o nome

    # Lógica para garantir que a categoria do produto é consistente com o tipo de produto no nome
    categoria_produto = None
    if 'Portátil' in nome_produto or 'Desktop' in nome_produto:
        categoria_produto = 'Portáteis' if 'Portátil' in nome_produto else 'Desktops'
    elif 'Smartphone' in nome_produto:
        categoria_produto = 'Smartphones'
    elif 'Smartwatch' in nome_produto or 'Pulseira' in nome_produto:
        categoria_produto = 'Wearables'
    elif 'Impressora' in nome_produto:
        categoria_produto = 'Impressoras'
    elif 'Monitor' in nome_produto or 'TV' in nome_produto or 'Projetor' in nome_produto:
        categoria_produto = 'Áudio e Vídeo' if 'TV' in nome_produto else 'Periféricos' # Monitor também pode ser Periféricos
    elif 'Teclado' in nome_produto or 'Rato' in nome_produto or 'Webcam' in nome_produto or 'Microfone' in nome_produto:
        categoria_produto = 'Periféricos'
    elif 'Aspirador' in nome_produto or 'Frigorífico' in nome_produto or 'Máquina de Lavar' in nome_produto or 'Forno' in nome_produto or 'Micro-ondas' in nome_produto or 'Máquina de Café' in nome_produto:
        categoria_produto = 'Eletrodomésticos'
    elif 'Router' in nome_produto:
        categoria_produto = 'Redes'
    elif 'Disco Externo' in nome_produto or 'Armazenamento' in nome_produto:
        categoria_produto = 'Armazenamento'
    elif 'Câmara' in nome_produto or 'Segurança' in nome_produto or 'Sensor' in nome_produto:
        categoria_produto = 'Segurança'
    elif 'Auscultadores' in nome_produto or 'Colunas' in nome_produto:
        categoria_produto = 'Áudio e Vídeo'
    elif 'Robô' in nome_produto or 'Iluminação' in nome_produto or 'Termostato' in nome_produto:
        categoria_produto = 'Smart Home'
    else:
        categoria_produto = random.choice(categorias) # Fallback para categoria aleatória

    # Definir custo e preço unitário com base na categoria para ter alguma variação realista
    if categoria_produto in ['Smartphones', 'Portáteis', 'Desktops', 'Tvs']:
        custo_unitario = round(random.uniform(250, 1800), 2)
        preco_unitario = round(custo_unitario * random.uniform(1.15, 1.45), 2)
    elif categoria_produto in ['Wearables', 'Eletrodomésticos', 'Impressoras', 'Redes', 'Gaming', 'Segurança', 'Smart Home']:
        custo_unitario = round(random.uniform(70, 900), 2)
        preco_unitario = round(custo_unitario * random.uniform(1.10, 1.35), 2)
    else: # Periféricos, Áudio e Vídeo, Armazenamento
        custo_unitario = round(random.uniform(15, 400), 2)
        preco_unitario = round(custo_unitario * random.uniform(1.05, 1.25), 2)

    # Pequeno ajuste de preço para marcas premium como Apple
    if marca_produto == 'Apple':
        custo_unitario = round(custo_unitario * random.uniform(1.2, 1.5), 2) # custo base mais alto
        preco_unitario = round(custo_unitario * random.uniform(1.20, 1.50), 2) # margem mais alta
    # Pequeno ajuste para marcas mais económicas
    elif marca_produto == 'Xiaomi' and categoria_produto == 'Smartphones':
        custo_unitario = round(custo_unitario * random.uniform(0.7, 0.9), 2)
        preco_unitario = round(custo_unitario * random.uniform(1.08, 1.25), 2)


    produtos_data.append({
        'ID_Produto': f'PROD-{i:04d}',
        'Nome_Produto': nome_produto,
        'Marca': marca_produto,
        'Categoria': categoria_produto,
        'Custo_Unitario': custo_unitario,
        'Preco_Unitario': preco_unitario
    })

df_produtos = pd.DataFrame(produtos_data)
# Garantir unicidade FINAL do Nome_Produto, embora a lógica acima já force bastante
df_produtos.drop_duplicates(subset=['Nome_Produto'], keep='first', inplace=True)
# Recriar IDs_Produto se houver duplicados removidos (para manter a sequência)
df_produtos['ID_Produto'] = [f'PROD-{i:04d}' for i in range(1, len(df_produtos) + 1)]


# --- Geração de Dados de Vendas ---
vendas_data = []
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 12, 31)

ids_cliente = df_clientes['ID_Cliente'].tolist()
ids_produto = df_produtos['ID_Produto'].tolist()

for i in range(1, num_vendas + 1):
    data_venda = fake.date_time_between(start_date=start_date, end_date=end_date)
    id_cliente = random.choice(ids_cliente)
    id_produto = random.choice(ids_produto)
    quantidade = random.randint(1, 5)
    canal_venda = random.choice(['Online', 'Loja Física', 'App Mobile', 'Marketplace'])

    vendas_data.append({
        'ID_Venda': f'VENDA-{i:05d}',
        'Data_Venda': data_venda,
        'ID_Cliente': id_cliente,
        'ID_Produto': id_produto,
        'Quantidade': quantidade,
        'Canal_Venda': canal_venda
    })
df_vendas = pd.DataFrame(vendas_data)

# --- Geração de Dados de Campanhas de Marketing ---
campanhas_data = []
canais_marketing = ['Redes Sociais', 'Email Marketing', 'Google Ads', 'SEO', 'Marketing de Conteúdo', 'Influencers', 'Outdoors']

for i in range(1, num_campanhas + 1):
    data_inicio = fake.date_time_between(start_date=start_date, end_date=end_date - timedelta(days=30))
    data_fim = data_inicio + timedelta(days=random.randint(7, 60))
    custo = round(random.uniform(500, 10000), 2)
    impressoes = random.randint(10000, 1000000)
    cliques = random.randint(impressoes // 100, impressoes // 10) # 1-10% CTR
    conversoes = random.randint(cliques // 50, cliques // 10) # 2-10% CR
    canal = random.choice(canais_marketing)

    campanhas_data.append({
        'ID_Campanha': f'CAMP-{i:03d}',
        'Nome_Campanha': fake.sentence(nb_words=4),
        'Canal': canal,
        'Data_Inicio': data_inicio,
        'Data_Fim': data_fim,
        'Custo': custo,
        'Impressoes': impressoes,
        'Cliques': cliques,
        'Conversoes': conversoes
    })
df_marketing_campanhas = pd.DataFrame(campanhas_data)


# --- Salvar em CSV ---
output_dir = 'data'
os.makedirs(output_dir, exist_ok=True)

df_clientes.to_csv(os.path.join(output_dir, 'clientes.csv'), index=False)
df_produtos.to_csv(os.path.join(output_dir, 'produtos.csv'), index=False)
df_vendas.to_csv(os.path.join(output_dir, 'vendas.csv'), index=False)
df_marketing_campanhas.to_csv(os.path.join(output_dir, 'marketing_campanhas.csv'), index=False)

print(f"Dados gerados e salvos em '{output_dir}/'")
print("Clientes:", df_clientes.shape)
print("Produtos:", df_produtos.shape)
print("Vendas:", df_vendas.shape)
print("Campanhas de Marketing:", df_marketing_campanhas.shape)