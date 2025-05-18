import pandas as pd
from sqlalchemy import create_engine

# 🔌 Conexión a MySQL en GCP por socket
user = 'root'
password = '1234'
database = 'covid_db'
socket_path = '/cloudsql/prueba-cun-460113:us-central1:myinstance'

# Crear motor de conexión
engine = create_engine(
    f'mysql+pymysql://{user}:{password}@localhost/{database}?unix_socket={socket_path}'
)

# 📥 Extraer tablas
tables = {}
for tbl in ['cases', 'municipality', 'gender', 'type_contagion']:
    df = pd.read_sql(f'SELECT * FROM {tbl}', con=engine)
    # Corregir nombres de columnas: quitar espacios, puntos y puntos y coma
    df.columns = [c.strip().replace(';', '').replace(' ', '_').lower() for c in df.columns]
    tables[tbl] = df

# Renombrar para facilitar
cases = tables['cases']
municipality = tables['municipality']
gender = tables['gender']
type_contagion = tables['type_contagion']

# 🔍 Verifica los nombres para asegurar que existen
print("✅ Columnas en 'cases':", cases.columns.tolist())

# 📊 KPIs
kpi_municipio = cases.groupby('id_municipality').size().reset_index(name='num_casos')
kpi_genero = cases.groupby('id_gender').size().reset_index(name='num_casos')
kpi_contagios = cases.groupby('id_type').size().reset_index(name='num_casos')


# 🧩 Merge para nombres legibles
kpi_municipio = kpi_municipio.merge(municipality, on='id_municipality', how='left')
kpi_genero = kpi_genero.merge(gender, on='id_gender', how='left')
kpi_contagios = kpi_contagios.merge(type_contagion, on='id_type', how='left')

# 💾 Exportar
kpi_municipio.to_csv('kpi_municipio.csv', index=False)
kpi_genero.to_csv('kpi_genero.csv', index=False)
kpi_contagios.to_csv('kpi_contagios.csv', index=False)

print("🎉 ¡Transformaciones y archivos KPI generados con éxito!")


