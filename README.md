# House Rocket


#### This project was made by Leandro Faria.

# 1. Business Problem.
  
A House Rocket é uma plataforma digital que tem como modelo de negócio, a compra e a venda de imóveis usando tecnologia. Sua principal estratégia é comprar boas casas em ótimas localizações com preços baixos e depois revendê-las posteriormente à preços mais altos. Quanto maior a diferença entre a compra e a venda, maior o lucro da empresa e, portanto, maior sua receita. Entretanto, as casas possuem muitos atributos que as tornam mais ou menos atrativas aos compradores e vendedores e a localização e o período do ano também podem influenciar os preços. A seguir vamos responder as seguintes perguntas:

	- 1 Quais recursos de uma casa mais impactam no preço?
	- 2 A House Rocket deveria fazer uma reforma para aumentar o preço da venda? Quais seriam as sugestões de mudanças ?
	- 3 Uma vez a casa em posse da empresa, quais são as melhores características para sua venda?


# 2. Business Assumptions.
	Seja qual for a metodologia utilizada, o objetivo deve ser atingido utilizando somente os dados fornecidos pela empresa.

# 3. Solution Strategy

My strategy to solve this challenge was:

**Step 01. Data Description:**
	- Etapa onde será analisada a existência de dados errôneos/faltantes, tipo de dados e quantidade de informação para ser trabalhada.

**Step 02. Feature Engineering:**
	- Criação de novas features com base nos dados para possibilitar a análise mais direta 	possível, bem como a criação de hipóteses que podem ajudar a entender       mais sobre o 	problema e como resolvê-lo;


**Step 03. Data Filtering:**
	- Remoção/substituição de valores não condizentes com o atributo selecionado.


**Step 04. Exploratory Data Analysis:**
	- Análise dos dados, com foco na validação de hipóteses definidas no passo 2 e nas respostas 	de negócio demandadas pela contratante.

**Step  05. Deploy Modelo to Production:**
	- Deploy do modelo para utilização de maneira fácil e intuitiva para usuários de áreas não técnicas.
  
  O deploy do modelo final será feito através do web app https://hou-rocket.herokuapp.com/.

# 4. Top 3 Data Insights

**Hypothesis 01:**
	- Imóveis que nunca passaram por reformas são em média 30% mais baratos.


**True.**

**Hypothesis 02:**
	- Imóveis com mais banheiros são em média 15% mais caros.

**True.**

**Hypothesis 03:**
	- Imóveis com data de construção inferior a 1955 são em média 50% mais baratos

**False.**

# 7. Business Results
  - Ao fim de nosso projeto, podemos verificar cada uma das perguntas feitas inicialmente.
  - 1 Quais recursos de uma casa mais impactam no preço? O recurso mais relevante para precificar a casa é o grade,sqft_living e Waterfront.
  - 2 A House Rocket deveria fazer uma reforma para aumentar o preço da venda? Quais seriam as sugestões de mudanças ? Para estes casos, deveria haver uma análise       mais profunda caso a caso.
  - 3 Uma vez a casa em posse da empresa, quais são as melhores características para sua venda? Não existe uma época ideal de venda, muito mais importa a condição em que se encontra a casa.


# 8. Conclusions
  - O resultado final da análise de dados gerou um lucro mínimo de até 25%, podendo em alguns casos superar 80% do valor investido.


# 9. Lessons Learned
	- Este projeto foi importante para análise de dados e para aprendizado de deploy utilizando o streamlit para montar o webapp.

# 10. Next Steps to Improve
	- Utilizar está análise em períodos maiores.

# LICENSE

# All Rights Reserved - Comunidade DS 2021
