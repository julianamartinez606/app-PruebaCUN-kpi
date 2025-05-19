import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# 🌐 Título
st.title("📊 Dashboard COVID - Cundinamarca y Boyacá")

# 📁 Cargar datos
@st.cache_data
def load_data():
    municipio = pd.read_csv("kpi_municipio.csv")
    genero = pd.read_csv("kpi_genero.csv")
    contagio = pd.read_csv("kpi_contagios.csv")
    resumen = pd.read_csv("kpi_resumen.csv")
    resumen["indicador"] = resumen["indicador"].str.strip()  # Limpia espacios
    return municipio, genero, contagio, resumen

kpi_municipio, kpi_genero, kpi_contagios, kpi_resumen = load_data()

# 🔹 Indicadores clave
st.markdown("### 🔹 Indicadores Clave")

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

col1.metric("🔢 Total Contagios", int(kpi_resumen.query("indicador == 'Contagios'")["valor"].values[0]))
col2.metric("🧵 Total Recuperados", int(kpi_resumen.query("indicador == 'Recuperados'")["valor"].values[0]))
col3.metric("☠️ Total Fallecidos", int(kpi_resumen.query("indicador == 'Fallecidos'")["valor"].values[0]))
prom_dias = kpi_resumen.query("indicador == 'Promedio días recuperación'")["valor"].values[0]
col4.metric("🕐 Promedio días recuperación", f"{prom_dias:.2f} días")

# 📊 KPI: Casos por Municipio
st.subheader("🏡 Casos por Municipio")
st.dataframe(kpi_municipio.sort_values("num_casos", ascending=False))
fig1, ax1 = plt.subplots()
ax1.barh(kpi_municipio["name_municipality"], kpi_municipio["num_casos"])
ax1.set_xlabel("Número de Casos")
ax1.set_ylabel("Municipio")
ax1.invert_yaxis()
st.pyplot(fig1)

# 📊 KPI: Casos por Género
st.subheader("👩‍🧐 Casos por Género")
st.dataframe(kpi_genero)
fig2, ax2 = plt.subplots()
ax2.pie(kpi_genero["num_casos"], labels=kpi_genero["name"], autopct="%1.1f%%", startangle=90)
ax2.axis("equal")
st.pyplot(fig2)

# 📊 KPI: Casos por Tipo de Contagio
st.subheader("🦠 Casos por Tipo de Contagio")
st.dataframe(kpi_contagios)
fig3, ax3 = plt.subplots()
ax3.bar(kpi_contagios["name"], kpi_contagios["num_casos"])
ax3.set_ylabel("Número de Casos")
ax3.set_xticks(range(len(kpi_contagios)))
ax3.set_xticklabels(kpi_contagios["name"], rotation=45)
st.pyplot(fig3)

# 📄 Pie de página
st.markdown("---")
st.markdown("App creada por **Sarii** para la prueba técnica BI ✨")

