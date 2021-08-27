from pandas.core.base import NoNewAttributesMixin
import geopandas
import pandas as pd
import streamlit as st
import numpy as np
import folium
import plotly.express as px
import  base64

from streamlit_folium import folium_static
from folium.plugins    import MarkerCluster   
from datetime import datetime
from PIL import Image



st.set_page_config( page_title="House Rocket Project", layout= 'wide' )


def image(foto,hypothese):

    st.image(Image.open(foto),
          caption=hypothese,
          use_column_width=False)

main_bg = "sample.jpg"
main_bg_ext = "jpg"

st.sidebar.image(Image.open('rocket-house.jpg'),
          caption='Projeto House Rocket',use_column_width=True)


st.markdown(
   f"""
   <style>
   .reportview-container {{
       background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
   }},
     
   </style>
   """,
   unsafe_allow_html=True
)

st.markdown(
   f"""
   <style>
   .reportview-container {{
     url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
   }},
     
   </style>
   """,
   unsafe_allow_html=True
)



##################################
####Testes de opções

html_header="""
<head>
<title>PControlDB</title>
<meta charset="utf-8">
<meta name="keywords" content="project control, dashboard, management, EVA">
<meta name="description" content="project control dashboard">
<meta name="author" content="Leandro Faria">
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<h1 style="font-size:300%;  font-family:Georgia"> House Rocket <br>
 <h2 style=" font-family:Georgia"> Description</h3> <br>
 <hr style= "  display: block;
  margin-top: 0.5em;
  margin-bottom: 0.5em;
  margin-left: auto;
  margin-right: auto;
  border-style: inset;
  border-width: 1.5px;"></h1>
"""



dash_sector= ['Home','Vizualização de dados','Atributos comerciais','Categorias físicas','Teste de Hipóteses','Conclusão']
                               
                               

selected_sector = st.sidebar.radio('DashBoard Fields', dash_sector) 





@st.cache( allow_output_mutation=True )
def get_data( path ) :
    data = pd.read_csv(path)
    

    return data   
    

@st.cache( allow_output_mutation=True )
def get_geofile( url ):
    geofile = geopandas.read_file( url )

    return geofile


def set_feature (data):
    data['price_m2'] = data['price'] / data ['sqft_lot']
    

    return data

def df_map(data):

    df_map = data[['zipcode','date', 'bedrooms', 'bathrooms','yr_built', 'lat', 'long']].copy()

    return df_map

def Home():
    if selected_sector == 'Home':
        html_header='''<h1 style="font-size:300%; font-family:Georgia"> Projeto House Rocket  <br>
                       <h2 style=" font-family:Georgia">Problema de Negócio </h2>
                       <h3 style=" font-family:Georgia">A House Rocket é uma plataforma digital que tem como modelo de negócio, a compra e a venda de imóveis usando tecnologia. Sua principal estratégia é comprar boas casas em ótimas localizações com preços baixos e depois revendê-las posteriormente à preços mais altos. Quanto maior a diferença entre a compra e a venda, maior o lucro da empresa e, portanto, maior sua receita.
                       Entretanto, as casas possuem muitos atributos que as tornam mais ou menos atrativas aos compradores e vendedores e a localização e o período do ano também podem influenciar os preços. A seguir vamos responder as seguintes perguntas:
                       <h3 style=" font-family:Georgia"> -1 Quais recursos de uma casa mais impactam no preço?
                       <h3 style=" font-family:Georgia"> -2 A House Rocket deveria fazer uma reforma para aumentar o preço da venda? Quais seriam as sugestões de mudanças ?
                       <h3 style=" font-family:Georgia"> -3 Uma vez a casa em posse da empresa, quais são as melhores características para sua venda? 
                       <h3 style=" font-family:Georgia"> No menu lateral é possível escolher entre as opções do dashboard:
                       <h3 style=" font-family:Georgia">-Home- Descriçao geral do projeto
                       <h3 style=" font-family:Georgia">-Vizualização de dados- Nesta opção podemos verificar os dados do nosso dashboard e analisar de maneira individual ou coletiva as casas e seus atributos,além, da vizualizaçao do mapa iterativo. 
                       <h3 style=" font-family:Georgia">-Comerciais- Nesta opão é possível alterar atributos comerciais, como data de construção,preço médio...etc.
                       <h3 style=" font-family:Georgia">-Teste de Hipóteses- Nesta opção é possível verificar questões de negócio que foram levantadas pela equipe de negócio.
                       <h3 style=" font-family:Georgia">-Conclusão- Nesta opção apresenta o resultado final da análise de dados '''
                       
        st.markdown(html_header, unsafe_allow_html=True)






def Conclusão():
    if selected_sector == 'Conclusão':

        html_Conclusão='''<h1 style="font-size:500%; font-family:Georgia"> Conclusão <br>
                       <h2 style=" font-family:sans-serife"> Ao fim de nosso projeto, podemos verificar cada uma das perguntas feitas inicialmente.</h2>
                       <h2 style=" font-family:sans-serife"> -1 Quais recursos de uma casa mais impactam no preço?
                       O recurso mais relevante para precificar a casa é o grade,sqft_living e Waterfront.
                       <h2 style=" font-family:sans-serife"> -2 A House Rocket deveria fazer uma reforma para aumentar o preço da venda? Quais seriam as sugestões de mudanças ?
                       Para estes casos, deveria haver uma análise mais profunda caso a caso.
                       <h2 style=" font-family:sans-serife"> -3 Uma vez a casa em posse da empresa, quais são as melhores características para sua venda?
                       Não existe uma época ideal de venda, muito mais importa a condição em que se encontra a casa.
                       <h2 style=" font-family:sans-serife">  O resultado final da análise de dados gerou um lucro  mínimo de até 25%,  podendo em alguns casos superar 80% do valor investido.</h2>
                       '''
        st.markdown(html_Conclusão, unsafe_allow_html=True)


def insights():

    if selected_sector == 'Teste de Hipóteses':
        html_insights='''<h1 style="font-size:300%; font-family:Georgia"> Teste de Hipóteses <br>
                         <h2 style=" font-family:sans-serif">Este campo é destinado a compartilhamento dos dados disponibilizados pela empresa. 
                         Aqui podemos verificar as hipotéses selecionadas pelas empresas a serem verificadas, e se cada uma é verdadeira ou falsa.</h2>
                         '''


        st.markdown(html_insights, unsafe_allow_html=True)
        html_hypotheses='''<h1 style="font-size:300%; font-family:Georgia">List of hypotheses<br>'''
        
      
      
        st.markdown(html_hypotheses, unsafe_allow_html=True)

        st.markdown('''<h2 style=" font-family:sans-serif">Hipótese 1: Imóveis com vista para o mar são em média 30% mais caros.''', unsafe_allow_html=True)
        image('Hypothesis 1.png','Hipótese 1')

        st.markdown('''<h2 style=" font-family:sans-serif">Hipótese 2: Imóveis com data de construção inferior a 1955 são em média 50% mais baratos.''', unsafe_allow_html=True)
        image('Hypothesis 2.png','Hipótese 2')

        st.markdown('''<h2 style=" font-family:sans-serif">Hipótese 3: As propriedades sem subsolo têm uma área total 40% maior do que as propriedades com subsolo.''', unsafe_allow_html=True)
        image('Hypothesis 3.png','Hipótese 3')

        st.markdown('''<h2 style=" font-family:sans-serif">Hipótese 4: Imóveis que nunca passaram por reformas são em média 30% mais baratos.''', unsafe_allow_html=True)
        image('Hypothesis 4.png','Hipótese 4')

        st.markdown('''<h2 style=" font-family:sans-serif">Hipótese 5: Imóveis com mais banheiros são em média 15% mais caros.''', unsafe_allow_html=True)
        image('Hypothesis 5.png','Hipótese 5')

        st.markdown('''<h2 style=" font-family:sans-serif">Hipótese 6: Imóveis com mais quartos são em média 15% mais caros.''', unsafe_allow_html=True)
        image('Hypothesis 6.png','Hipótese 6')
        
        st.markdown('''<h2 style=" font-family:sans-serif">Hipótese 7: The YoY( Year over Year) property price growth is 10%.''', unsafe_allow_html=True)
        st.markdown('''<h2 style=" font-family:sans-serif">Não foi possível avaliar devido ao período disponível no conjunto de dados.''', unsafe_allow_html=True)

        st.markdown('''<h2 style=" font-family:sans-serif">Hipótese 8: Os imóveis com um medidor mais caro têm maior probabilidade de serem vendidos.''', unsafe_allow_html=True)
        image('Hypothesis 8.png','Hipótese 8')
        


def overview_data(data):
    if selected_sector == 'Vizualização de dados':


        html_overview='''<h1 style="font-size:300%; font-family:Georgia"> Vizualização de dados  <br>
                         <h2 style="font-family:sans-serif">Este campo é destinado a compartilhamento dos dados disponibilizados pela empresa. 
                         Aqui podemos alterar as colunas que iremos visualizar e o código postal desejado. 
                         Na parte inferior da página é possível verificar o mapa com as informações selecionadas em nosso filtro da barra lateral.  </h2>
                         '''





        st.markdown(html_overview, unsafe_allow_html=True)
    
    
        f_columns = ['date', 'bedrooms', 'bathrooms',
                'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
                'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated',
                'lat', 'long', 'sqft_living15', 'sqft_lot15']
        df_columns =['id', 'price', 'zipcode', 'sqft_living', 'price_m2']
        

        f_attributes = st.sidebar.multiselect('Enter Columns', f_columns)
        f_zipcode = st.sidebar.multiselect('Enter zipcode', data['zipcode'].unique() )
        total_attributes = df_columns + f_attributes
        
        
        new_data = '<i style="font-family:sans-serif; font-size: 30px;">Data</i>'
        st.markdown(new_data, unsafe_allow_html=True)

        if ( f_zipcode != [] ) & ( f_attributes != [] ):
            data = data.loc[data['zipcode'].isin( f_zipcode ), total_attributes]

        elif ( f_zipcode != [] ) & ( f_attributes == [] ):
            data = data.loc[data['zipcode'].isin( f_zipcode ), :]

        elif ( f_zipcode == [] ) & ( f_attributes != [] ):
            data = data.loc[:, total_attributes]

        else:
            data = data.copy()


        st.dataframe(data.head())

        c1, c2 = st.beta_columns((1,1))

        #*************************
        #Average Metrics
        #*************************
        df1 = data[['id','zipcode']].groupby('zipcode').count().reset_index()
        df2 = data[['price','zipcode']].groupby('zipcode').mean().reset_index()
        df3 = data[['sqft_living','zipcode']].groupby('zipcode').mean().reset_index()
        df4 = data[['price_m2','zipcode']].groupby('zipcode').mean().reset_index()


        #===========================================
        #Merge
        #===========================================

        m1 = pd.merge( df1, df2,on ='zipcode',how='inner' )
        m2 = pd.merge(  m1, df3,on ='zipcode', how='inner')
        df = pd.merge(  m2, df4,on ='zipcode', how='inner')

        df.columns = ['ZIPCODE', 'TOTAL HOUSES', 'PRICE','SQRT LIVING', 'PRICE/M2' ]

        Average_Values = '<i style="font-family:sans-serif; font-size: 30px;">Average Values</i>'
        c1.markdown(Average_Values, unsafe_allow_html=True)
        
        c1.dataframe(df,height= 550)


        #============================================
        #Statistic Descriptive
        #============================================

        num_attributes = data.select_dtypes(include = ['int64','float64'] )
        media =   pd.DataFrame( num_attributes.apply( np.mean   ) )
        mediana = pd.DataFrame( num_attributes.apply( np.median ) )
        std =     pd.DataFrame( num_attributes.apply( np.std    ) )

        max_=pd.DataFrame( num_attributes.apply (np.max)) 
        min_=pd.DataFrame( num_attributes.apply (np.min))

        df1 = pd.concat( [ max_, min_, media, mediana,std ],axis=1).reset_index()
        df1.columns = ['attritutes','max','min','mean','median','std']

        Attributes_Analysis = '<i style="font-family:sans-serif; font-size: 30px;">Attributes Analysis</i>'
        c2.markdown(Attributes_Analysis, unsafe_allow_html=True)
        


        
        c2.dataframe(df1,height= 800)

        return None


def portifolio_density( data, geofile):
#====================================================
# Densidade de Portfolio
#====================================================
    if selected_sector == 'Vizualização de dados':
        df_map = data[['zipcode','date', 'bedrooms', 'bathrooms','yr_built', 'lat', 'long']].copy()
        
        Region_Overview= '<i style="font-family:Georgia;  font-size: 30px;">Region Overview</i>'
        st.markdown(Region_Overview, unsafe_allow_html=True)
        
        
        c1,c2 = st.beta_columns ( ( 1,1 ) )
        Portifolio_Density= '<i style="font-family:sans-serif;  font-size: 30px;">Region Overview</i>'
        c1.markdown(Portifolio_Density, unsafe_allow_html=True)


        df = pd.merge(data, df_map)

        #====================================================
        # Base Map - Folium
        #====================================================

        density_map = folium.Map(location = [df['lat'].mean(),df['long'].mean()],default_zoom_start=15)


        marker_cluster = MarkerCluster().add_to( density_map)
        for name, row in df.iterrows():


            folium.Marker( [row['lat'],row['long']],
                popup = 'Sold R${0} on:{1}.Features:{2} sqft, {3} bedrooms, {4} bathrooms,year built:{5}'.format(row['price'],
                row['date'],
                row['sqft_living'],
                row['bedrooms'],
                row['bathrooms'],
                row['yr_built'])).add_to(marker_cluster)



        with c1:
            folium_static(density_map)

        #====================================================
        # Base Map - Folium
        #====================================================
        Price_Density= '<i style="font-family:sans-serif;  font-size: 30px;">Price Density</i>'
        c2.markdown(Price_Density, unsafe_allow_html=True)
        
        #c2.header('Price Density')

        #df = data[['price','zipcode']].groupby('zipcode').mean().reset_index()
        df2 = data[['price','zipcode']].groupby('zipcode').mean().reset_index()

        df2.columns = ['ZIP','PRICE']

        #df = df.sample(10)

        geofile = geofile[geofile['ZIP'].isin( df2['ZIP'].tolist() )]

        region_price_map = folium.Map(location = [df['lat'].mean(),
                                                df['long'].mean()],
                                                default_zoom_start=15)


        region_price_map.choropleth( data = df2,
                                    geo_data = geofile,
                                    columns =['ZIP','PRICE'],
                                    key_on='feature.properties.ZIP',
                                    fill_color= 'YlOrRd',
                                    fill_opacity= 0.7,
                                    line_opacity=0.2,
                                    legend_name='AVG PRICE' )


        with c2:

            folium_static(region_price_map)

        return None


def commercial_distribution( data ):
    ######################################################
    #    Distrituição de imoveis por categorias comerciais
    ######################################################
    if selected_sector == 'Atributos comerciais':
        html_commercial='''<h1 style="font-size:300%;  font-family:Georgia"> Commercial Attributes  <br>
                           <h2 style=" font-family:sans serife">Este campo é destinado a compartilhamento dos dados disponibilizados pela empresa. 
                           Aqui podemos alterar os dados comerciais que iremos visualizar,como, ano máximo de construção
                           ,preço médio no ano, preço médio no ano, preço médio...etc. </h2>'''
        
        
        st.markdown(html_commercial, unsafe_allow_html=True)


        st.sidebar.title('Commercial Options')
        st.title('Atributos comerciais')

        ######################################################
        #                AVERAGE PRICE PER YEAR
        ######################################################
        
        data['date'] = pd.to_datetime( data['date']).dt.strftime('%Y-%m-%d')

        #Filters
        min_year_built = int(data['yr_built'].min())
        max_year_built = int(data['yr_built'].max())

        st.sidebar.subheader('Select Max Year Built')
        f_year_built = st.sidebar.slider( 'Year Built',
                                        min_year_built,
                                        max_year_built,
                                        min_year_built)

                                        
        st.header('Average Price per Year Built')


        # Data Selection
        df = data.loc[data['yr_built'] < f_year_built]

        df = df[['yr_built','price']].groupby('yr_built').mean().reset_index()
        fig = px.line( df, x= 'yr_built', y= 'price' )

        st.plotly_chart( fig,use_container_width= True)


        ######################################################
        #                AVERAGE PRICE PER DAY
        ######################################################

        st.header('Average Price per Day')
        st.sidebar.subheader('Select Max Date')

        # Filters
        min_date = datetime.strptime( data['date'].min(),'%Y-%m-%d')
        max_date = datetime.strptime( data['date'].max(),'%Y-%m-%d')

        f_date = st.sidebar.slider('Date', min_date, max_date, min_date)


        # Data Filtering
        data['date'] = pd.to_datetime(data['date'])
        df = data.loc[data['date'] < f_date]
        df = df[['date','price']].groupby('date').mean().reset_index()

        # Plot
        fig = px.line( df, x= 'date', y= 'price' )

        st.plotly_chart( fig,use_container_width= True)


        ######################################################
        #                Histogram
        ######################################################

        st.header('Price Distribution')
        st.sidebar.subheader('Select Max Price')

        # Filters
        min_price = int(data['price'].min())
        max_price = int(data['price'].max())
        avg_price = int(data['price'].mean())

        # Data Filtering

        f_price = st.sidebar.slider('Price',min_price,max_price,avg_price)

        df = data.loc[data['price'] < f_price]

        # Data Plot

        fig = px.histogram ( df, x = 'price',nbins= 50 )
        st.plotly_chart(fig,use_container_width= True)
        
        return None


def attributes_distribution( data ):
    ######################################################
    # Distribution of Properties by Categorias físicas
    ######################################################
    if selected_sector == 'Categorias físicas':

        html_physical='''<h1 style="font-size:300%;  font-family:Georgia"> Categorias físicas  <br>
                         <h2 style=" font-family:Georgia">Este campo é destinado a compartilhamento dos dados disponibilizados pela empresa. 
                         Aqui podemos selecionar qual atributos nos interessa no imóveis que serão vistos em nosso dashboard,tais como, número máximo de quartos, número máximo de banheiros...etc.</h2>
                         '''

        st.markdown(html_physical, unsafe_allow_html=True)
        st.sidebar.title( 'Attributes Option')
        st.title ('Categorias físicas')

        # Filters
        f_bedrooms = st.sidebar.selectbox( 'Max number of bedrooms',
                                        sorted(set(
                                        data['bedrooms'].unique())))

        f_bathooms = st.sidebar.selectbox( 'Max number of bathrooms',
                                            sorted(set(
                                            data['bathrooms'].unique())))



        c1,c2 = st.beta_columns(2)

        # House per Bedrooms
        c1.header( 'House per Bedrooms')
        df = data [ data[ 'bedrooms'] < f_bedrooms ]
        fig = px.histogram ( df, x= 'bedrooms', nbins = 19)
        st.plotly_chart( fig, use_container_width= True )

        # House per Bathrooms
        c2.header( 'Houses per Bathrooms')
        df = data[data['bathrooms'] < f_bathooms]
        fig = px.histogram ( df, x='bathrooms', nbins= 19)
        st.plotly_chart( fig, use_container_width = True )


        # Filters 
        f_floors = st.sidebar.selectbox ( 'Max number of Floors',
                                        sorted( set( 
                                        data['floors'].unique())))

        f_waterview = st.sidebar.checkbox( 'Only Houses with Water View')




        c1,c2 = st.beta_columns(2)
        # House per Floors
        c1.header( 'Houses per Floor')
        df = data[data['floors'] < f_floors]
        fig = px.histogram ( data, x='floors', nbins= 19)
        c1.plotly_chart( fig, use_container_width = True )

        # House per Water View

        if f_waterview :
            df = data[data['waterfront'] == 1]

        else:
            df = data.copy()

        fig = px.histogram (df , x = 'waterfront', nbins = 10)
        c2.plotly_chart( fig, use_container_width = True)  


if __name__ == '__main__':
    #ETL
    
    #data extration

    path = 'kc_house_data.csv'
    url = 'https://opendata.arcgis.com/datasets/83fc2e72903343aabff6de8cb445b81c_2.geojson'
    
    data = get_data( path )
    geofile = get_geofile( url )

    
    
    #transformation
    data = set_feature ( data )
    
    Home()
    
    insights()

    Conclusão()

    df_map( data )
    
    overview_data( data )

    portifolio_density( data, geofile ) 

    commercial_distribution( data )

    attributes_distribution( data )

html_line="""
<br>
<br>
<br>
<br>
<hr style= "  display: block;
  margin-top: 0.5em;
  margin-bottom: 0.5em;
  margin-left: auto;
  margin-right: auto;
  border-style: inset;
  border-width: 1.5px;">
<p style=" text-align: right;">By: leandro_faria@yahoo.com.br</p>
"""
st.markdown(html_line, unsafe_allow_html=True)