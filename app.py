import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("📊 Dashboard COVID - Cundinamarca y Boyacá")

@st.cache_data
def load_data():
    municipio = pd.read_csv("kpi_municipio.csv")
    genero = pd.read_csv("kpi_genero.csv")
    contagio = pd.read_csv("kpi_contagios.csv")
    return municipio, genero, contagio

kpi_municipio, kpi_genero, kpi_contagios = load_data()

# 📍 KPI: Casos por Municipio
st.subheader("🏘️ Casos por Municipio")
st.dataframe(kpi_municipio.sort_values("num_casos", ascending=False))
fig1, ax1 = plt.subplots()
ax1.barh(kpi_municipio["name_municipality"], kpi_municipio["num_casos"])  # ✅ columna corregida
ax1.set_xlabel("Número de Casos")
ax1.set_ylabel("Municipio")
ax1.invert_yaxis()
st.pyplot(fig1)

# 📍 KPI: Casos por Género
st.subheader("👩‍🦰 Casos por Género")
st.dataframe(kpi_genero)
fig2, ax2 = plt.subplots()
ax2.pie(kpi_genero["num_casos"], labels=kpi_genero["name"], autopct="%1.1f%%", startangle=90)
ax2.axis("equal")
st.pyplot(fig2)

# 📍 KPI: Casos por Tipo de Contagio
st.subheader("🦠 Casos por Tipo de Contagio")
st.dataframe(kpi_contagios)
fig3, ax3 = plt.subplots()
ax3.bar(kpi_contagios["name"], kpi_contagios["num_casos"])
ax3.set_ylabel("Número de Casos")
ax3.set_xticks(range(len(kpi_contagios)))  # ✅ Añade ticks explícitamente
ax3.set_xticklabels(kpi_contagios["name"], rotation=45)
st.pyplot(fig3)

# 📍 Pie de página
st.markdown("---")
st.markdown("App creada por **Sarii** para la prueba técnica BI ✨")
