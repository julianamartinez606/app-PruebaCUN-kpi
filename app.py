import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("📊 Dashboard COVID - Cundinamarca y Boyacá")

@st.cache_data
def load_data():
    municipio = pd.read_csv("kpi_municipio.csv")
    genero = pd.read_csv("kpi_genero.csv")
    contagio = pd.read_csv("kpi_contagios.csv")
    cases= pd.read ("cases.csv")
    return municipio, genero, contagio, cases

kpi_municipio, kpi_genero, kpi_contagios, df_cases = load_data()

# KPIs principales
total_casos = kpi_contagios["num_casos"].sum()
total_recuperados = df_cases["date_recovery"].notna().sum()
total_fallecidos = df_cases["date_death"].notna().sum()

# Cálculo de días promedio de recuperación
df_cases["date_symptom"] = pd.to_datetime(df_cases["date_symptom"], errors="coerce")
df_cases["date_recovery"] = pd.to_datetime(df_cases["date_recovery"], errors="coerce")
df_cases["dias_recuperacion"] = (df_cases["date_recovery"] - df_cases["date_symptom"]).dt.days
promedio_dias = int(df_cases["dias_recuperacion"].mean(skipna=True))

# Visualización en columnas
col1, col2, col3, col4 = st.columns(4)
col1.metric("🦠 Contagios", f"{total_casos:,}")
col2.metric("💚 Recuperados", f"{total_recuperados:,}")
col3.metric("🖤 Fallecidos", f"{total_fallecidos:,}")
col4.metric("🕒 Promedio días recuperación", f"{promedio_dias} días")






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
