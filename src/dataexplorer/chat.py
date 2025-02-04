import streamlit as st
import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from anthropic import Anthropic
from io import StringIO

def create_homepage():
    st.set_page_config(
        page_title="DataExplorer",
        page_icon="📊",
        layout="centered"
    )

    st.markdown("""
        <style>
        .title {
            font-size: 50px !important;
            font-weight: bold !important;
            text-align: center !important;
            padding: 30px 0 !important;
            color: #900C3F !important;
            animation: fadeIn 1.5s ease-in;
        }
        .welcome-text {
            font-size: 24px !important;
            text-align: center !important;
            color: #900C3F !important;
            margin-bottom: 20px !important;
        }
        .description-box {
            background-color: #f8f9fa;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin: 20px 0;
            animation: slideUp 1s ease-out;
        }
        .start-button {
            text-align: center;
            padding: 20px 0;
            animation: pulse 2s infinite;
        }
        .feature-item {
            color: #900C3F !important;
            font-size: 18px !important;
            padding: 8px 0 !important;
            text-align: center !important;
        }
        .license {
            font-size: 14px !important;
            color: gray !important;
            text-align: center !important;
            margin-top: 40px !important;
            padding-top: 10px !important;
            border-top: 1px solid #ccc !important;
        }
        .streamlit-expanderHeader {
            background-color: #900C3F !important;
            color: white !important;
            border-radius: 10px !important;
            padding: 20px !important;
            font-size: 24px !important;
            font-weight: bold !important;
            margin: 30px 0 !important;
            text-align: center !important;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1) !important;
            cursor: pointer !important;
            transition: all 0.3s ease !important;
        }
        .streamlit-expanderHeader:hover {
            background-color: #600828 !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2) !important;
        }
        .streamlit-expanderContent {
            background-color: #f8f9fa !important;
            border-radius: 10px !important;
            padding: 25px !important;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1) !important;
            margin-top: 10px !important;
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        @keyframes slideUp {
            from { 
                transform: translateY(50px);
                opacity: 0;
            }
            to { 
                transform: translateY(0);
                opacity: 1;
            }
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        .stButton button {
            background-color: #900C3F !important;
            color: white !important;
            border: none !important;
            padding: 15px 30px !important;
            font-size: 18px !important;
            transition: all 0.3s ease !important;
        }
        .stButton button:hover {
            background-color: #600828 !important;
            transform: translateY(-2px) !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="title">DataExplorer</h1>', unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="description-box">', unsafe_allow_html=True)
        st.markdown('<p class="welcome-text">Bienvenue sur DataExplorer, votre assistant intelligent d\'analyse de données. Notre plateforme vous permet d\'explorer et de comprendre vos données tabulaires de manière intuitive grâce à l\'intelligence artificielle.</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with st.expander("✨ Pourquoi utiliser notre produit ? ✨"):
        features = [
            "🔍 Chargez n'importe quel jeu de données tabulaire",
            "💬 Posez vos questions en langage naturel",
            "📊 Obtenez des visualisations pertinentes et des interprétations claires"
        ]
        
        for feature in features:
            st.markdown(f'<p class="feature-item">{feature}</p>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<div class="start-button">', unsafe_allow_html=True)
    if st.button("Commencez votre exploration", type="primary", use_container_width=True):
        with st.spinner('Préparation de votre espace de travail...'):
            time.sleep(1.5)
            st.session_state.page = "chat"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="license">', unsafe_allow_html=True)
    st.markdown('<p>© 2025 DataExplorer. Tous droits réservés.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)



def create_chat_interface():
    st.set_page_config(
        page_title="DataExplorer - Chat",
        page_icon="📊",
        layout="wide"
    )

    st.markdown("""
        <style>
        .chat-container {
            max-width: 800px;
            margin: 0 auto;
        }
        .chat-message {
            padding: 15px;
            border-radius: 10px;
            margin: 10px 0;
            position: relative;
            animation: fadeIn 0.5s ease-in;
        }
        .user-message {
            background-color: #e3f2fd;
            margin-left: 100px;
            margin-right: 20px;
            border: 1px solid #bbdefb;
        }
        .assistant-message {
            background-color: #f8f9fa;
            margin-right: 100px;
            margin-left: 20px;
            border: 1px solid #e9ecef;
        }
        .message-header {
            font-size: 0.8em;
            color: #666;
            margin-bottom: 5px;
            font-weight: bold;
        }
        .user-header {
            color: #1976d2;
        }
        .assistant-header {
            color: #900C3F;
        }
        .message-content {
            line-height: 1.5;
        }
        .sidebar-content {
            padding: 20px;
            color: #900C3F;
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        </style>
    """, unsafe_allow_html=True)

    # Initialisation de l'historique des messages
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    with st.sidebar:
        st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
        st.title("⚙️ Paramètres")

        language = st.selectbox(
            "Choisissez votre langue",
            ["Français", "English", "Arabe"]
        )

        st.markdown("⚠️ **Important** :")
        st.markdown("""
        - Format de fichier accepté : CSV
        - Les données doivent être tabulaires
        - Taille maximum : 200MB
        - Encodage recommandé : UTF-8
        """)

        if st.button("🔄 Nouvelle conversation"):
            st.session_state.messages = []
            st.rerun()

    st.title("💬 Assistant DataExplorer")
    st.markdown("👋 Bonjour ! Je suis votre assistant DataExplorer. Pour commencer, veuillez télécharger votre fichier de données au format CSV.")

    # Chargement du fichier CSV
    uploaded_file = st.file_uploader("Choisissez votre fichier CSV", type=['csv'])

    if uploaded_file is not None:
        if 'data_loaded' not in st.session_state:
            df = pd.read_csv(uploaded_file)
            st.session_state.df = df
            st.session_state.data_loaded = True


        # Affichage du message de réception du fichier
        st.markdown("✅ Fichier reçu ! Voici un aperçu des données :")

        # Affichage du tableau des données
        st.dataframe(st.session_state.df.head())

        # Message demandant à poser une question
        st.markdown("💡 Posez vos questions sur les données fournies.")

        # Affichage des messages existants
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        for message in st.session_state.messages:
            message_class = "assistant-message" if message['role'] == 'assistant' else "user-message"
            header_class = "assistant-header" if message['role'] == 'assistant' else "user-header"
            header_text = "🤖 Assistant" if message['role'] == 'assistant' else "👤 Vous"
            
            st.markdown(f'''
                <div class="chat-message {message_class}">
                    <div class="message-header {header_class}">{header_text}</div>
                    <div class="message-content">{message['content']}</div>
                </div>
            ''', unsafe_allow_html=True)

            if 'figure' in message:
                st.pyplot(message['figure'])
        st.markdown('</div>', unsafe_allow_html=True)

        # Zone de saisie utilisateur
        user_question = st.chat_input("💭 Posez votre question...")

        if user_question:
            # Ajout du message utilisateur
            st.session_state.messages.append({
                'role': 'user',
                'content': user_question
            })

            with st.spinner('Analyse en cours...'):
                sample_data = st.session_state.df.head(50).to_csv(index=False)
                client = Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])

                prompt = f""" 
                    Données d'exemple :
                    {sample_data}
                    Question : {user_question}
                    Si l'utilisateur demande "hello", répondez par une salutation et demandez-lui s'il est prêt à commencer l'analyse des données.
                    Si l'utilisateur demande "describe data", générez une description des données fournies (par exemple, dimensions du dataset, types de colonnes, etc.).
                    Si l'utilisateur pose une question comme "combien de ...", générez un graphique pertinent à cette question, comme un histogramme ou un graphique en barres.
                    Si l'utilisateur pose d'autres questions, générez un script Python concis utilisant Matplotlib ou Seaborn pour visualiser les données de manière pertinente.
                """

                response = client.messages.create(
                    model="claude-3-5-sonnet-20240620",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=300
                )

                response_content = response.content[0].text
                message_with_response = {
                    'role': 'assistant',
                    'content': response_content.strip()
                }

                st.session_state.messages.append(message_with_response)
                st.rerun()




def main():
    if 'page' not in st.session_state:
        st.session_state.page = "home"

    if st.session_state.page == "home":
        create_homepage()
    elif st.session_state.page == "chat":
        create_chat_interface()

if __name__ == "__main__":
    main()