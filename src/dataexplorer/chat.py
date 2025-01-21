import streamlit as st
import time
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import StreamlitCallbackHandler

def create_chat_interface():
    # Configuration de la page
    st.set_page_config(
        page_title="DataExplorer - Chat",
        page_icon="📊",
        layout="wide"
    )

    # CSS personnalisé
    st.markdown("""
        <style>
        .sidebar-content {
            padding: 20px;
            color: #900C3F;
        }
        .chat-message {
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
            background-color: #f8f9fa;
            animation: fadeIn 0.5s ease-in;
        }
        .warning-box {
            background-color: #fff3cd;
            border-left: 5px solid #900C3F;
            padding: 15px;
            margin: 10px 0;
            border-radius: 5px;
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        </style>
    """, unsafe_allow_html=True)

    # Sidebar pour les paramètres
    with st.sidebar:
        st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
        st.title("⚙️ Paramètres")

        # Sélection de la langue
        language = st.selectbox(
            "Choisissez votre langue",
            ["Français", "English", "Español", "Deutsche"]
        )

        # Sélection du modèle LLM
        llm_model = st.selectbox(
            "Choisissez votre modèle",
            ["Claude", "GPT-4", "GPT-3.5"]
        )

        st.markdown("### ℹ️ Prérequis")
        st.markdown("""
        - Format de fichier accepté : CSV
        - Les données doivent être tabulaires
        - Taille maximum : 200MB
        - Encodage recommandé : UTF-8
        """)

        st.markdown("### 🔑 API Configuration")
        if llm_model in ["GPT-4", "GPT-3.5"]:
            openai_api_key = st.text_input("OpenAI API Key", type="password")
        else:
            anthropic_api_key = st.text_input("Anthropic API Key", type="password")

        st.markdown('</div>', unsafe_allow_html=True)

    # Zone principale
    st.title("💬 Assistant DataExplorer")

    # Message de bienvenue initial
    if 'welcomed' not in st.session_state:
        st.markdown('<div class="chat-message">', unsafe_allow_html=True)
        st.markdown("""
        👋 Bonjour ! Je suis votre assistant DataExplorer.
        
        Pour commencer, veuillez télécharger votre fichier de données au format CSV.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        st.session_state.welcomed = True

    # Zone d'upload de fichier
    uploaded_file = st.file_uploader("Choisissez votre fichier CSV", type=['csv'])

    # Avertissements et instructions
    st.markdown('<div class="warning-box">', unsafe_allow_html=True)
    st.markdown("""
    ⚠️ **Important** :
    - Assurez-vous que votre fichier est au format CSV
    - Vérifiez que vos données sont bien structurées en colonnes
    - Les en-têtes de colonnes doivent être clairs et uniques
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # Si un fichier est uploadé
    if uploaded_file is not None:
        st.success("✅ Fichier reçu ! Je suis prêt à analyser vos données.")
        
        # Zone de chat
        st.markdown("### 💭 Posez vos questions sur les données")
        user_question = st.text_input("Votre question :")
        
        if user_question:
            with st.spinner('Analyse en cours...'):
                # Ici viendra la logique de traitement avec le LLM choisi
                time.sleep(1.5)  # Simulation de traitement
                st.markdown("*Cette partie sera connectée au LLM choisi (Claude ou GPT)*")

def main():
    if 'page' not in st.session_state:
        st.session_state.page = "home"
        
    if st.session_state.page == "upload":
        create_chat_interface()

if __name__ == "__main__":
    main()