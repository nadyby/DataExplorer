import streamlit as st
import time

def create_homepage():
    # Configuration de la page
    st.set_page_config(
        page_title="DataExplorer",
        page_icon="📊",
        layout="centered"
    )

    # Custom CSS pour le style
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
        /* Style amélioré pour l'expander de Streamlit */
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

    # Titre principal
    st.markdown('<h1 class="title">DataExplorer</h1>', unsafe_allow_html=True)

    # Description dans un cadre
    with st.container():
        st.markdown('<div class="description-box">', unsafe_allow_html=True)
        st.markdown('<p class="welcome-text">Bienvenue sur DataExplorer, votre assistant intelligent d\'analyse de données. Notre plateforme vous permet d\'explorer et de comprendre vos données tabulaires de manière intuitive grâce à l\'intelligence artificielle.</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Bouton expandable pour les caractéristiques (maintenant plus grand et plus visible)
    with st.expander("✨ Pourquoi utiliser notre produit ? ✨"):
        features = [
            "🔍 Chargez n'importe quel jeu de données tabulaire",
            "💬 Posez vos questions en langage naturel",
            "📊 Obtenez des visualisations pertinentes et des interprétations claires"
        ]
        
        for feature in features:
            st.markdown(f'<p class="feature-item">{feature}</p>', unsafe_allow_html=True)

    # Espacement
    st.markdown("<br>", unsafe_allow_html=True)

    # Bouton de démarrage
    st.markdown('<div class="start-button">', unsafe_allow_html=True)
    if st.button("Commencez votre exploration", type="primary", use_container_width=True):
        with st.spinner('Préparation de votre espace de travail...'):
            time.sleep(1.5)
            st.session_state.page = "upload"
    st.markdown('</div>', unsafe_allow_html=True)

    # Section de licence
    st.markdown('<div class="license">', unsafe_allow_html=True)
    st.markdown('<p>© 2025 DataExplorer. Tous droits réservés.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    create_homepage()
