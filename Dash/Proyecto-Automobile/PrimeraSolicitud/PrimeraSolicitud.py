import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

# Cargar datos
csv_path = r"C:\Users\josep\OneDrive\Escritorio\Proyectos-Junior\Dash\Proyecto-Automobile\PrimeraSolicitud\PrimeraSolicitud.csv"  # Reemplaza con la ruta real
df = pd.read_csv(csv_path)

# Agrupar por 'make' y calcular el precio promedio
df_avg_price = df.groupby("make", as_index=False)["price"].mean()

# Crear la app Dash
app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1("Relación entre el precio del automóvil y sus especificaciones técnicas"),
    dcc.Graph(id="price-make-graph",
              figure=px.bar(df_avg_price, x="make", y="price",
                            labels={"make": "Automóviles", "price": "Precio Promedio"},
                            title="Precio Promedio de Autos por Marca"))
])

if __name__ == "__main__":
    app.run_server(debug=True)
