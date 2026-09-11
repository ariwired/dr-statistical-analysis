![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%2311557C.svg?style=for-the-badge&logo=Matplotlib&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=white)
![Statsmodels](https://img.shields.io/badge/Statsmodels-4051B5?style=for-the-badge)

# Análise Bioestatística da Retinopatia Diabética

Seleção de datasets e pré-processamento de dados para a disciplina de Projeto em Computação.

## Objetivo

Este repositório apresenta um estudo prático de datasets públicos relacionados à **Retinopatia Diabética (RD)**, com foco na seleção de dados, pré-processamento, análise exploratória e aplicação de métodos estatísticos em dados oftalmológicos.

O projeto foi desenvolvido no contexto da disciplina de **Projeto em Computação**.

## Estrutura conceitual

O projeto foi organizado em duas etapas principais:

```text
00_dataset_comparison.ipynb

Objetivo e princípio de comparação
        ↓
Datasets candidatos e fontes
        ↓
Carregamento e padronização
        ↓
Definição semântica das variáveis
        ↓
Inspeção estatística padronizada
        ↓
Compatibilidade com os requisitos
        ↓
Elegibilidade e critérios de desempate
        ↓
Seleção do dataset
        ↓
01_diabetic_retinopathy_analysis.ipynb
        ↓
Análise bioestatística principal
```

O primeiro notebook realiza uma etapa complementar de investigação e seleção. A partir dessa comparação, um único dataset é selecionado para a execução da análise estatística solicitada na atividade.

## Estrutura do projeto

O projeto é organizado em dois notebooks principais.

### `00_dataset_comparison.ipynb`

Notebook complementar destinado à **busca, triagem e comparação de datasets públicos** relacionados à Retinopatia Diabética.

Os datasets são avaliados considerando critérios como:

* disponibilidade e formato dos dados;
* quantidade e diversidade de variáveis;
* relevância das variáveis para análise estatística;
* presença de variáveis clínicas e demográficas;
* tamanho e unidade de análise da amostra;
* natureza e definição do desfecho;
* qualidade e documentação da fonte;
* acessibilidade;
* possibilidade de reprodução;
* adequação às técnicas estatísticas propostas na atividade.

A adequação estatística é comparada por meio de critérios objetivos relacionados aos requisitos da atividade, como disponibilidade de variáveis numéricas, categóricas, clínicas e demográficas, possibilidade de correlação e comparação entre grupos e presença de desfecho relacionado à RD. Aspectos como proveniência, documentação e confiabilidade da fonte são considerados separadamente na elegibilidade dos datasets para a seleção final.

O objetivo deste notebook é identificar **qual estrutura de dados apresenta maior adequação às análises estatísticas exigidas pela atividade** e, a partir disso, fundamentar a seleção de um único dataset.

### `01_diabetic_retinopathy_analysis.ipynb`

Notebook correspondente à **análise principal desenvolvida para responder à atividade da disciplina**.

A análise é realizada utilizando um único dataset selecionado na etapa anterior e contempla:

* descrição do dataset;
* limpeza e preparação dos dados;
* análise de valores ausentes;
* verificação de duplicidades;
* identificação de inconsistências;
* padronização dos tipos de dados;
* estatística descritiva;
* visualização dos dados;
* análise de correlação;
* comparação entre grupos;
* testes estatísticos;
* interpretação dos resultados;
* limitações;
* conclusão.

## Fontes dos dados

Os datasets investigados durante a etapa de seleção são provenientes de repositórios públicos, incluindo:

* [Kaggle](https://www.kaggle.com/)
* [UCI Machine Learning Repository](https://archive.ics.uci.edu/)
* [PhysioNet](https://physionet.org/)

A fonte original e as referências de cada dataset são identificadas nos respectivos notebooks.

## Reprodutibilidade

As análises são desenvolvidas em Python, utilizando Jupyter Notebook/Google Colab e bibliotecas para manipulação, análise estatística e visualização de dados.

As principais decisões de pré-processamento e análise são documentadas nos notebooks, permitindo a reprodução dos procedimentos realizados.

## Estrutura do repositório

```text
.
├── README.md
├── 00_dataset_comparison.ipynb
└── 01_diabetic_retinopathy_analysis.ipynb
```

## Observação

O `00_dataset_comparison.ipynb` possui caráter **complementar**, sendo utilizado para investigar e comparar datasets candidatos e fundamentar a seleção da base de dados.

O `01_diabetic_retinopathy_analysis.ipynb` constitui a **análise principal desenvolvida para atender aos requisitos da atividade da disciplina de Projeto em Computação**, utilizando um único dataset selecionado com base nos critérios estabelecidos na etapa de comparação.
