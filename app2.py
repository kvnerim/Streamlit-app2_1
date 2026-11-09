import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    df = pd.read_excel("ibm_hr_attrition.xlsx")
    return df 

data = load_data()

st.set_page_config(
    page_title="Dashboard des Ventes",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

page = st.sidebar.selectbox(
    "Navigation",
    ["Accueil", "Analyse", "Graphiques"]
)

page = st.sidebar.radio(
    "Navigation",
    ["Accueil", "Analyse", "Graphiques"]
)

if page == "Accueil":
    st.title("Bienvenue sur le Dashboard")

    # Texte introductif
    st.write(
        "Ceci est la page d'accueil avec un résumé des informations principales."
    )

    # Lien vers la documentation officielle Streamlit
    st.markdown(
        "Pour en savoir plus sur Streamlit, visitez [la documentation](https://docs.streamlit.io/library)."
    )

    # Ajouter une image depuis une URL publique (version moderne)
    st.image(
        "https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png",
        caption="Logo Streamlit",
        use_container_width=True
    )

    # Ajouter un résumé ou indicateur simple
    st.metric(label="Nombre de visiteurs", value="10 025", delta="+42%")
    
    # Texte explicatif supplémentaire
    st.write(
        "Ce dashboard est conçu pour vous fournir une vue d'ensemble rapide de vos données et analyses."
    )

elif page == "Analyse":
    st.title("Analyse des données")
    st.write("Cette page contient des tableaux et statistiques des ventes.")



    # Widgets interactifs
    option = st.selectbox(
        "Choisissez une catégorie",
        ["Travel_Rarely", "Travel_Frequently", "Non-Travel"]
    )
    rate = st.slider(
        "Sélectionner un taux (top 10, top 20...)", 0, 40, 10
    )
    
    st.write(f"Catégorie sélectionnée : {option}")
    st.write(f"Top choisi : {rate} (rangé par orde décroissant de DailyRate)")

    #nb_row = int(data.shape[0]*rate/100)
    select1 = data.sort_values(by="DailyRate",ascending=False).head(rate)
    select = select1.head(rate)
    st.table(select1)

    # Sélecteurs de date
   # st.date_input("Date de début")
   # st.date_input("Date de fin")
    
    # Exemple de tableau
    
  
    
    # Bouton pour télécharger le tableau
    st.download_button(
        label="Télécharger les données",
        data=data.to_csv(index=False).encode('utf-8'),
        file_name='ventes.csv',
        mime='text/csv'
    )

    # Lien vers la documentation
    st.link_button(
        "Voir la documentation du link_button",
        "https://docs.streamlit.io/develop/api-reference/widgets/st.link_button"
    )

elif page == "Graphiques":
    st.title("Visualisations interactives")
    
    # Dataset simulé
    #df_data = pd.DataFrame({
    #    "Jour": ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"],
    #    "Ventes": [100, 150, 200, 170, 220],
    #    "Commandes": [15, 60, 10, 36, 87],
    #    "Clients": [5, 8, 12, 7, 10]
    #})
    
    # Sélection de la variable à visualiser
    variable = st.selectbox(
               "Choisissez la variable à visualiser", 
               ["Répartion H/F", "Commandes", "Clients"]
           )
    
    # Colonnes pour graphiques côte à côte
    col1, col2 = st.columns(2)
    
    # Graphique linéaire dynamique
    col1.header(f"Repartition H/F{variable}")
    variable2 = st.selectbox(
                      "Choisissez la catégorie à visualiser", 
                      ["Travel_Rarely", "Travel_Frequently", "Non-Travel"]
                  )
    #col1.line_chart(df_data.set_index("Jour")[variable])
    #st.subheader(f"BusinessTraver = {variable2}")
    fig = px.pie(
            data[data["BusinessTravel"]==variable2],
           names="Gender",
           title=f"Répartition H/F dans {variable2}",
           color_discrete_sequence=px.colors.qualitative.Pastel
           )
    fig.update_traces(textfont=dict(size=40))
    fig.update_layout( legend_font_size=35)
    col1.plotly_chart(fig)
    # Graphique à barres dynamique
    #col2.header(f"Répartition de {variable} par jour")
    #col2.bar_chart(df_data.set_index("Jour")[variable])
    
    # Graphique Plotly interactif
    
    
   

    test = data.groupby("BusinessTravel").agg({"DailyRate" : "sum"})
    col2.bar_chart(test.reset_index().set_index("BusinessTravel")["DailyRate"])
    
    
    # Expander pour détails supplémentaires
    with st.expander("Détails supplémentaires"):
        st.write("Données complètes utilisées pour les visualisations :")
        #st.dataframe(data)
