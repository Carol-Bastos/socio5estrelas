import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Sócio 5 Estrelas", page_icon="🦊", layout="wide")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(to bottom, #00122e 0%, #005BA3 50%, #4facfe 100%);
    background-attachment: fixed;
}
.stButton>button {
    background-color: rgba(255,255,255,0.1);
    color: white;
    border: 1px solid white;
    border-radius: 15px;
}
h1, h2, h3, p, span, label { color: white !important; }

.fall, .joker {
    position: fixed;
    top: -50px;
    font-size: 30px;
    animation: fall linear infinite;
    z-index: 9999;
}
@keyframes fall {
    0% { transform: translateY(-50px); opacity: 1; }
    100% { transform: translateY(100vh); opacity: 0; }
}
</style>
""", unsafe_allow_html=True)

def carregar_imagem(nome_base):
    for ext in [".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG"]:
        caminho = f"{nome_base}{ext}"
        if os.path.exists(caminho):
            return caminho
    return None

with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/bc/Cruzeiro_Esporte_Clube_logo.svg", width=80)
    st.title("Painel do Sócio")
    st.subheader("🗓️ Próximo Jogo")
    data_jogo = datetime(2026, 2, 8, 16, 0)
    dias_restantes = (data_jogo - datetime.now()).days
    st.metric(label="Dias para o Clássico", value=f"{max(0, dias_restantes)}")

st.markdown("<h1 style='text-align:center;'>Sócio 5 estrelas by Carol Bastos</h1>", unsafe_allow_html=True)

st.markdown("### 🎵 Solta o Hino, Torcedor!")
st.video("https://www.youtube.com/watch?v=aeJzEJ8pcXg")

st.divider()

st.header("🏆 Planos 5 estrelas")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Estrelas do Povo")
    img = carregar_imagem("gerson")
    if img: st.image(img, use_container_width=True)
    st.write("💰 R$ 21,00/mês")
    if st.button("Assinar Estrelas do Povo", key="povo", use_container_width=True):
        st.toast("🃏 Modo Coringa ativado!")
        st.markdown("""
        <div class="joker" style="left:10%; animation-duration:3s;">🃏</div>
        <div class="joker" style="left:20%; animation-duration:4s;">🃏</div>
        <div class="joker" style="left:30%; animation-duration:5s;">🃏</div>
        <div class="joker" style="left:40%; animation-duration:3.5s;">🃏</div>
        <div class="joker" style="left:50%; animation-duration:4.5s;">🃏</div>
        <div class="joker" style="left:60%; animation-duration:5s;">🃏</div>
        <div class="joker" style="left:70%; animation-duration:3.2s;">🃏</div>
        <div class="joker" style="left:80%; animation-duration:4.8s;">🃏</div>
        <div class="joker" style="left:90%; animation-duration:3.7s;">🃏</div>
        """, unsafe_allow_html=True)

with col2:
    st.subheader("Cruzeiro Sempre")
    img = carregar_imagem("comemoracao")
    if img: st.image(img, use_container_width=True)
    st.write("💰 R$ 62,00/mês")
    if st.button("Assinar Cruzeiro Sempre", key="sempre", use_container_width=True):
        st.snow()

with col3:
    st.subheader("K-abuloso Max")
    img = carregar_imagem("kaio")
    if img: st.image(img, use_container_width=True)
    st.write("💰 R$ 150,00/mês")
    if st.button("Assinar K-abuloso Max", key="max", use_container_width=True):
        st.toast("⚽ GOOOOOL DO CABULOSO!")
        st.markdown("""
        <div class="fall" style="left:5%; animation-duration:3s;">⚽</div>
        <div class="fall" style="left:15%; animation-duration:4s;">GOL</div>
        <div class="fall" style="left:25%; animation-duration:5s;">⚽</div>
        <div class="fall" style="left:35%; animation-duration:3.5s;">GOL</div>
        <div class="fall" style="left:45%; animation-duration:4.5s;">⚽</div>
        <div class="fall" style="left:55%; animation-duration:5s;">GOL</div>
        <div class="fall" style="left:65%; animation-duration:3.2s;">⚽</div>
        <div class="fall" style="left:75%; animation-duration:4.8s;">GOL</div>
        <div class="fall" style="left:85%; animation-duration:3.7s;">⚽</div>
        """, unsafe_allow_html=True)

st.divider()

col_esq, col_dir = st.columns([2,1])

with col_esq:
    st.header("📊 Crescimento de Sócios")
    dados = pd.DataFrame({'Mês':['Jan','Fev','Mar','Abr','Mai','Jun'],'Novos Sócios':[4500,5200,6100,5800,7500,9000]})
    st.bar_chart(dados.set_index('Mês'))

    st.header("📖 Nossa História")
    with st.expander("⭐ 1921 - Fundação"):
        st.write("""
A história do Cruzeiro Esporte Clube começa em 2 de janeiro de 1921, em Belo Horizonte, fundado pela colônia italiana como Societá Sportiva Palestra Itália, usando as cores verde e vermelho.  
Em 1942, forçado pelo governo devido à Segunda Guerra Mundial, mudou para Cruzeiro Esporte Clube, adotando o azul e branco e o Cruzeiro do Sul como símbolos.  
Tornou-se um dos grandes do Brasil, conquistando títulos como Libertadores, Copa do Brasil e Campeonato Brasileiro, sendo reconhecido como Melhor Clube Brasileiro do Século XX pela IFFHS.

**Principais Marcos:**
- Fundação: 2 de janeiro de 1921, como Palestra Itália  
- Mudança de Nome: 1942, para Cruzeiro Esporte Clube  
- Cores: Verde, vermelho e branco (inicial) → Azul e branco (atual)  
- Primeiras Glórias: Tricampeonato Mineiro (1928–1930) e abertura para jogadores não italianos (1925)  
- Era de Ouro: Décadas de 90 e 2000, com títulos como Libertadores (1997), Supercopa (1991, 1992) e a Tríplice Coroa em 2003  
- Reconhecimento: Melhor Clube Brasileiro do Século XX (IFFHS, 2009)  
- Ídolos: Ronaldo, Maicon, Gomes, Luisão, entre outros  
- Símbolo: A Raposa, criada pelo cartunista Mangabeira  

**Títulos de Destaque:**
- Libertadores: 1976, 1997  
- Brasileirão: 1966 (Taça Brasil), 2003, 2013, 2014  
- Copa do Brasil: 1993, 1996, 2000, 2003, 2017, 2018  
- Outros: Supercopa Libertadores (1991, 1992), Recopa Sul-Americana (1999)
""")

img = carregar_imagem("raposao")
if img:
    st.image(img, width=500)

with st.expander("⭐ 2003 - Tríplice Coroa"):
    st.write("""
A Tríplice Coroa do Cruzeiro refere-se ao feito histórico de 2003, quando o clube venceu o Campeonato Mineiro, a Copa do Brasil e o Campeonato Brasileiro no mesmo ano — algo inédito no futebol brasileiro.

A equipe, comandada por Vanderlei Luxemburgo, tinha jogadores como Alex, Deivid e Aristizábal, marcando um dos anos mais vitoriosos da história do clube.

**Os Títulos da Tríplice Coroa (2003):**
- Campeonato Mineiro: Invicto, com goleada de 4x0 sobre o Tupi  
- Copa do Brasil: Vitória por 3x1 sobre o Flamengo no Mineirão  
- Campeonato Brasileiro: 100 pontos, título confirmado contra o Paysandu  

**Características da Conquista:**
- Futebol ofensivo e envolvente  
- Quarteto decisivo: Alex, Deivid, Aristizábal e Mota  
- Primeiro clube brasileiro a conquistar Estadual + Copa do Brasil + Brasileirão no mesmo ano
""")

img = carregar_imagem("fotodatacatrofeu")
if img:
    st.image(img, width=500)


    st.header("📍 Nossa Casa")
    st.map(pd.DataFrame({'lat':[-19.8659],'lon':[-43.9711]}))

with col_dir:
    st.header("🏟️ Check-in")
    with st.form("check"):
        setor = st.selectbox("Setor do Estádio", ["Amarelo","Laranja","Vermelho","Roxo"])
        if st.form_submit_button("Confirmar Presença"):
            st.toast("Check-in feito!")

    st.header("💬 Mural Azul")
    with st.form("mural"):
        nome = st.text_input("Seu Nome")
        msg = st.text_area("Mensagem")
        if st.form_submit_button("Postar"):
            st.success("Mensagem postada!")

st.markdown("---")
st.write("© 2026 - Desenvolvido com 💙 por Carol Bastos")

