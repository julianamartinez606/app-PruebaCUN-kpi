import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(layout="centered")
st.title("📊 Dashboard COVID - Cundinamarca y Boyacá")

# 📥 Cargar KPIs
@st.cache_data
def load_data():
    municipio = pd.read_csv("kpi_municipio.csv")
    genero = pd.read_csv("kpi_genero.csv")
    contagio = pd.read_csv("kpi_contagios.csv")
    resumen = pd.read_csv("kpi_resumen.csv")
    return municipio, genero, contagio, resumen

kpi_municipio, kpi_genero, kpi_contagios, kpi_resumen = load_data()

# 🔹 Indicadores generales
st.subheader("📌 Indicadores Generales")
col1, col2 = st.columns(2)
col1.metric("🧪 Total Contagios", int(kpi_resumen.loc[0, "valor"]))
col2.metric("💀 Total Fallecidos", int(kpi_resumen.loc[2, "valor"]))
col1.metric("💚 Total Recuperados", int(kpi_resumen.loc[1, "valor"]))
col2.metric("🕒 Promedio días recuperación", f'{kpi_resumen.loc[3, "valor"]:.2f} días')

# 🏘️ Casos por Municipio
st.subheader("🏘️ Casos por Municipio")
st.dataframe(kpi_municipio.sort_values("num_casos", ascending=False))
fig1, ax1 = plt.subplots()
ax1.barh(kpi_municipio["name_municipality"], kpi_municipio["num_casos"])
ax1.set_xlabel("Número de Casos")
ax1.set_ylabel("Municipio")
ax1.invert_yaxis()
st.pyplot(fig1)

# 👩‍🦰 Casos por Género
st.subheader("👩‍🦰 Casos por Género")
st.dataframe(kpi_genero)
fig2, ax2 = plt.subplots()
ax2.pie(kpi_genero["num_casos"], labels=kpi_genero["name"], autopct="%1.1f%%", startangle=90)
ax2.axis("equal")
st.pyplot(fig2)

# 🦠 Casos por Tipo de Contagio
st.subheader("🦠 Casos por Tipo de Contagio")
st.dataframe(kpi_contagios)
fig3, ax3 = plt.subplots()
ax3.bar(kpi_contagios["name"], kpi_contagios["num_casos"])
ax3.set_ylabel("Número de Casos")
ax3.set_xticks(range(len(kpi_contagios)))
ax3.set_xticklabels(kpi_contagios["name"], rotation=45)
st.pyplot(fig3)

# Footer
st.markdown("---")
st.markdown("Prueba Técnica BI - Universidad CUN")

