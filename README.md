# Projeto de Análise de Dados: Vendas e Marketing

Este projeto demonstra uma análise completa de dados de vendas e campanhas de marketing, desde a geração de dados sintéticos até a extração de *insights* acionáveis e a formulação de recomendações de negócio.

## Objetivos do Projeto

* Gerar um conjunto de dados realistas para simular operações de vendas e marketing.
* Realizar Análise Exploratória de Dados (EDA) para entender as características dos dados.
* Limpar e preparar os dados para análise, tratando valores ausentes e convertendo tipos de dados.
* Integrar dados de diferentes fontes (vendas, produtos, marketing) para uma visão unificada.
* Criar novas métricas de negócio (e.g., margem bruta, ROI, CAC).
* Visualizar tendências de vendas, desempenho de produtos e eficácia de campanhas.
* Fornecer *insights* claros e recomendações estratégicas baseadas em dados para otimizar vendas e marketing.

## Ferramentas e Tecnologias

* **Linguagem de Programação:** Python
* **Bibliotecas Python:** `pandas` (manipulação de dados), `numpy` (cálculos numéricos), `matplotlib` e `seaborn` (visualização de dados), `faker` (geração de dados sintéticos).
* **Ambiente de Desenvolvimento:** Visual Studio Code (VS Code)
* **Ambiente Interativo:** Jupyter Notebook (`.ipynb`)
* **Controlo de Versão:** Git e GitHub

## Estrutura do Projeto

* `gerar_dados.py`: Script Python para criar os ficheiros CSV de vendas, produtos e campanhas de marketing.
* `data/`: Pasta contendo os ficheiros CSV gerados (`vendas.csv`, `produtos.csv`, `marketing_campanhas.csv`).
* `analise_vendas_marketing.ipynb`: Jupyter Notebook principal contendo toda a análise de dados, visualizações, *insights* e recomendações.

## Como Executar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/suvgoncalves/Data-Analysis-Sales-Marketing.git](https://github.com/suvgoncalves/Data-Analysis-Sales-Marketing.git)
    cd Data-Analysis-Sales-Marketing
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python -m venv .venv
    # No Windows:
    .\.venv\Scripts\activate
    # No macOS/Linux:
    source ./.venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install pandas numpy faker matplotlib seaborn
    ```

4.  **Gere os dados sintéticos:**
    ```bash
    python gerar_dados.py
    ```
    Os ficheiros CSV serão criados na pasta `data/`.

5.  **Abra o Jupyter Notebook:**
    * No VS Code, abra o ficheiro `analise_vendas_marketing.ipynb`.
    * Certifique-se de que o kernel do Jupyter está a usar o ambiente `.venv` que você ativou.
    * Execute as células do Notebook sequencialmente para ver a análise completa.

## Insights Chave

* **Vendas:** Identificação de picos sazonais de vendas no final do ano (Novembro e Dezembro) e um crescimento constante ao longo do período. As categorias "Wearables" e "Smartphones" são os principais impulsionadores de receita. O canal "Online" é o mais forte, e "Lisboa" a região de maior contribuição.
* **Produtos:** Produtos como "Axiomatic digital printer" e "Intelligent security camera" são consistentemente os mais vendidos por quantidade.
* **Marketing:** O "Email Marketing" apresenta um excelente ROI e um CAC baixo, sugerindo uma alocação de orçamento mais eficiente. "Redes Sociais" têm alto custo e alto volume de vendas atribuídas.

## Recomendações

* **Otimização do Orçamento de Marketing:** Aumentar o investimento em canais de alto ROI como "Email Marketing" e reavaliar campanhas de baixo desempenho, redirecionando fundos.
* **Foco Estratégico em Produtos:** Desenvolver estratégias de *cross-selling* e *up-selling* para os produtos mais populares e de alta margem.
* **Expansão Regional e de Canais:** Explorar o potencial de crescimento em regiões menos desenvolvidas e otimizar canais como "App Mobile" para aumentar as vendas.
* **Gestão Sazonal de Vendas:** Planeamento antecipado de stock e marketing para os picos de vendas de fim de ano, e campanhas de estabilização em períodos de menor atividade.
* **Monitorização Contínua:** Implementar um dashboard para monitorizar em tempo real as métricas de vendas e marketing, permitindo decisões ágeis.

---
*Este projeto foi desenvolvido como parte de um estudo e demonstra habilidades em análise de dados, Python e visualização.*
