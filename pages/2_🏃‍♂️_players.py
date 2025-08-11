import streamlit as st
import time

st.set_page_config(
    page_title="Players",
    page_icon="🏃‍♂️",
    layout="wide"
)

time.sleep(0.5)

df_data = st.session_state["data"]

#1. Seleciona o Clube
clubes = df_data["Club"].unique()
club = st.sidebar.selectbox("Clube", clubes)

#2. Filtra Jogadores do Clube Selecionado
df_players_do_clube = df_data[(df_data["Club"] == club)]
players_do_clube = df_players_do_clube["Name"].unique()

#3. Seleciona o Jogador usando a lista filtrada
player = st.sidebar.selectbox("Jogador", players_do_clube)

#4. Encontra os Status do Jogador Selecionado
player_stats = df_data[df_data["Name"] == player].iloc[0]

#5. Exibe Imagem do Jogador
st.image(player_stats["Photo"])
st.title(player_stats["Name"])

st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)'] / 100}")
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)'] * 0.453:.2f}")

st.divider()

st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats["Overall"]))

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor de Mercado", value=f"£ {player_stats['Value(£)']:,}")
col2.metric(label="Remuneração Semanal", value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label="Cláusula de Recisão", value=f"£ {player_stats['Release Clause(£)']:,}")





