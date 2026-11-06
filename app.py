
import streamlit as st
from pathlib import Path

# ============================================================
# CONFIGURAÇÕES
# ============================================================
st.set_page_config(
    page_title="Uma surpresa para você ❤️",
    page_icon="🎄",
    layout="centered",
    initial_sidebar_state="collapsed"
)

BASE_DIR = Path(__file__).resolve().parent
GIF_PATH = BASE_DIR / "gatinho_amor_natal.gif"

# ============================================================
# ESTILO
# ============================================================
st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(
                180deg,
                #FFF0F5 0%,
                #FFE4EC 55%,
                #FFF7FA 100%
            );
        }

        header[data-testid="stHeader"] {
            background: transparent;
        }

        [data-testid="stMainBlockContainer"] {
            max-width: 740px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        h1 {
            text-align: center;
            color: #D6336C !important;
            font-family: Georgia, serif;
            font-size: clamp(1.7rem, 5vw, 2.6rem) !important;
        }

        .subtitle {
            text-align: center;
            color: #B85C7A;
            font-size: 1.1rem;
            margin-bottom: 1.5rem;
        }

        .message {
            text-align: center;
            color: #A83D68;
            font-family: Georgia, serif;
            font-size: 1.4rem;
            margin-top: 1.3rem;
        }

        .footer {
            text-align: center;
            color: #BC8299;
            font-size: 0.85rem;
            margin-top: 3rem;
        }

        [data-testid="stImage"] img {
            border-radius: 18px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# PÁGINA
# ============================================================
st.title("Uma surpresa para você! 🎄❤️")

st.markdown(
    '<div class="subtitle">'
    'Um pouquinho de carinho em forma de animação ✨'
    '</div>',
    unsafe_allow_html=True
)

# GIF: reprodução automática quando a página carregar
if GIF_PATH.exists():
    st.image(str(GIF_PATH), width="stretch")
else:
    st.error("Arquivo da animação não encontrado.")

st.markdown(
    '<div class="message">'
    'Que seu dia seja tão especial quanto seu sorriso! ❤️'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="footer">'
    'Feito com carinho ✨'
    '</div>',
    unsafe_allow_html=True
)
