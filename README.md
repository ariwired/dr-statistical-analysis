![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%2311557C.svg?style=for-the-badge&logo=Matplotlib&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=white)
![Statsmodels](https://img.shields.io/badge/Statsmodels-4051B5?style=for-the-badge)

# Análise Bioestatística da Retinopatia Diabética

Seleção de datasets públicos e análise bioestatística de dados clínicos e demográficos relacionados à Retinopatia Diabética.

## Objetivo

Este repositório apresenta um estudo prático de dados públicos relacionados à **Retinopatia Diabética (RD)**, desenvolvido no contexto da disciplina de **Projeto em Computação**.

O trabalho foi dividido em duas etapas. A primeira compara diferentes datasets públicos e identifica qual estrutura de dados é mais adequada às análises propostas na atividade. A segunda realiza a análise bioestatística do dataset selecionado, incluindo pré-processamento, análise exploratória, visualizações, correlação, comparação entre grupos e interpretação dos resultados.

## Estrutura conceitual

O projeto foi organizado em duas etapas principais:

```text
00_dataset_comparison.ipynb

Objetivo e critérios de comparação
        ↓
Datasets candidatos e fontes
        ↓
Carregamento e padronização
        ↓
Definição semântica das variáveis
        ↓
Inspeção estatística padronizada
        ↓
Compatibilidade com os requisitos da atividade
        ↓
Elegibilidade científica
        ↓
Seleção do dataset
        ↓
mBRSET
        ↓
01_diabetic_retinopathy_analysis.ipynb
        ↓
Auditoria e pré-processamento
        ↓
Reorganização em nível de paciente
        ↓
Análise exploratória
        ↓
Visualizações
        ↓
Correlação
        ↓
Comparação entre estágios ICDR
        ↓
Análise pós-hoc
        ↓
Interpretação e conclusão
```

O primeiro notebook possui caráter complementar e fundamenta a escolha da base. O segundo concentra a análise estatística principal.

## Estrutura do projeto

### `00_dataset_comparison.ipynb`

Notebook complementar destinado à **busca, triagem e comparação de datasets públicos** relacionados à Retinopatia Diabética.

Os datasets são avaliados considerando aspectos como:

- disponibilidade e formato dos dados;
- quantidade e diversidade de variáveis;
- presença de variáveis clínicas e demográficas;
- tamanho e unidade de análise da amostra;
- natureza e definição do desfecho;
- qualidade e documentação da fonte;
- acessibilidade;
- possibilidade de reprodução;
- compatibilidade com análise descritiva;
- possibilidade de correlação entre variáveis numéricas;
- possibilidade de comparação entre grupos;
- presença de desfecho relacionado à RD.

A compatibilidade estatística é analisada por critérios objetivos relacionados aos requisitos da atividade. Proveniência, documentação e confiabilidade da fonte são consideradas separadamente na elegibilidade dos datasets para a seleção final.

Entre os datasets investigados estão:

- mBRSET;
- BRSET;
- Diabetic Retinopathy Debrecen;
- ODIR-5K;
- Diabetic Retinopathy Study (DRS).

A comparação resultou na seleção do mBRSET para a análise principal, por apresentar dados tabulares clínicos e demográficos estruturados, além da classificação da Retinopatia Diabética segundo a escala ICDR.

### `01_diabetic_retinopathy_analysis.ipynb`

Notebook principal do projeto, responsável pelo pré-processamento, análise exploratória e análise estatística do **mBRSET**.

O arquivo original analisado possui:

- 5.164 registros de imagem;
- 1.291 pacientes;
- 24 colunas;
- 4 imagens por paciente.

Como várias informações clínicas e demográficas se repetem entre as imagens de um mesmo indivíduo, as análises estatísticas não são realizadas diretamente sobre as 5.164 linhas.

Antes das análises, os dados são reorganizados em uma tabela com **uma observação por paciente**, evitando que imagens pertencentes ao mesmo indivíduo sejam tratadas como observações independentes.

A construção dessa tabela considera:

- mediana dos valores disponíveis para características numéricas do paciente;
- moda para características categóricas;
- maior estágio ICDR observado entre as imagens disponíveis para representar o estágio analisado do paciente;
- presença de edema quando o achado está registrado em pelo menos uma imagem;
- manutenção da quantidade de imagens e rótulos disponíveis para acompanhamento da cobertura dos dados.

O maior estágio ICDR é uma decisão adotada nesta análise e não corresponde a um rótulo oficial do mBRSET em nível de paciente.

#### Pré-processamento

A preparação dos dados inclui:

- identificação de valores ausentes;
- diferenciação entre ausência de informação e não aplicabilidade;
- verificação de registros duplicados;
- padronização dos tipos;
- validação dos códigos categóricos;
- identificação de valores inconsistentes;
- aplicação de regras de plausibilidade;
- verificação da consistência das características repetidas entre imagens do mesmo paciente.

Não é realizada imputação geral dos valores ausentes. Cada procedimento estatístico considera os pacientes com as informações necessárias para as variáveis analisadas.

O tempo de insulinoterapia é tratado separadamente, pois essa informação se aplica apenas aos pacientes que fazem uso de insulina.

#### Análise exploratória

A análise descritiva apresenta:

- média;
- mediana;
- desvio-padrão;
- mínimo;
- máximo;
- quartis;
- intervalo interquartil;
- coeficiente de variação;
- frequências absolutas e relativas das variáveis categóricas.

A população também é caracterizada segundo idade, sexo, escolaridade, tratamentos, hipertensão, estágio ICDR e edema macular.

#### Visualizações

O notebook apresenta quatro tipos de visualização:

- histograma da distribuição da idade;
- gráfico de barras da distribuição dos estágios ICDR;
- boxplot da duração da diabetes segundo o estágio ICDR;
- gráfico de dispersão entre idade e duração da diabetes.

Cada gráfico é acompanhado de interpretação relacionada aos resultados observados.

#### Correlação

A associação entre idade e duração da diabetes é avaliada após a verificação da distribuição das variáveis.

Como a hipótese de normalidade foi rejeitada, a análise é realizada por meio da correlação de Spearman.

O resultado encontrado foi:

- ρ = 0.220;
- p < 0.05;
- IC95% bootstrap aproximadamente entre 0.165 e 0.273.

Os resultados indicam uma associação positiva de baixa magnitude entre idade e duração da diabetes.

#### Comparação entre grupos

A duração da diabetes é comparada entre os cinco estágios ICDR.

Após a avaliação dos pressupostos, é aplicado o teste de Kruskal-Wallis, com resultado:

- H = 167.699;
- p < 0.05.

O resultado indica diferença na distribuição da duração da diabetes entre pelo menos dois estágios.

Como o teste global rejeitou a hipótese nula, são realizadas comparações par a par pelo teste de Mann-Whitney, com correção de Holm para múltiplas comparações.

Após a correção, não foram encontradas diferenças estatisticamente detectáveis entre: 

- sem RD e RDNP leve;
- RDNP moderada e RDNP grave.

Os demais pares apresentaram diferenças estatisticamente detectáveis.

#### Interpretação dos resultados

A interpretação final relaciona os resultados descritivos, gráficos e estatísticos.

Entre os principais resultados observados:

- idade média de 61.45 anos;
- 65.07% dos pacientes eram do sexo feminino;
- 1.287 pacientes possuíam classificação ICDR disponível;
- entre os pacientes com ICDR disponível, 69.3% foram classificados como sem RD;
- entre os pacientes com RD, a RDNP moderada foi o estágio mais frequente;
- a associação entre idade e duração da diabetes foi positiva e de baixa magnitude;
- a duração da diabetes apresentou diferenças entre os estágios ICDR;
- as medianas de duração da diabetes tenderam a aumentar nos estágios mais avançados.

A interpretação considera a magnitude das associações, a sobreposição entre grupos, a diferença no tamanho das categorias ICDR e as limitações do conjunto de dados.

Os resultados são restritos à população representada pelo mBRSET e não são interpretados como relações causais.

## Dataset selecionado

A análise principal é realizada com o **mBRSET — Mobile Brazilian Retinal Dataset**.

- PhysioNet: [https://physionet.org/content/mbrset/1.0/](https://physionet.org/content/mbrset/1.0/)
- Repositório dos autores: [https://github.com/luisnakayama/mBRSET](https://github.com/luisnakayama/mBRSET)
- DOI do dataset: [https://doi.org/10.13026/qxpd-1y65](https://doi.org/10.13026/qxpd-1y65)
- Artigo: [https://doi.org/10.1038/s41597-025-04627-3](https://doi.org/10.1038/s41597-025-04627-3)

## Fontes dos dados

Os datasets investigados durante a etapa de seleção são provenientes de repositórios públicos, incluindo:

- [Kaggle](https://www.kaggle.com/)
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/)
- [PhysioNet](https://physionet.org/)

A fonte original, a documentação e as referências de cada dataset são identificadas nos respectivos notebooks.

## Reprodutibilidade

As análises são desenvolvidas em Python com Jupyter Notebook/Google Colab.

As principais bibliotecas empregadas são:

- Pandas;
- NumPy;
- Matplotlib;
- SciPy;
- Statsmodels.

As decisões de limpeza, transformação e análise estatística são documentadas ao longo dos notebooks.

O código mantém a unidade de análise em nível de paciente e registra as regras aplicadas aos valores ausentes e inconsistentes.

Uma execução completa do notebook permite reproduzir as tabelas, gráficos e resultados estatísticos apresentados.

## Estrutura do repositório

```text
.
├── README.md
├── requirements.txt
├── 00_dataset_comparison.ipynb
└── 01_diabetic_retinopathy_analysis.ipynb
```

## Observação

O `00_dataset_comparison.ipynb` possui caráter **complementar**, sendo usado para investigar datasets candidatos e documentar os critérios que levaram à seleção do mBRSET.

O `01_diabetic_retinopathy_analysis.ipynb` constitui a **análise principal do projeto**, reunindo o pré-processamento, a análise exploratória, as visualizações, os testes estatísticos e a interpretação dos resultados a partir dos dados do mBRSET.