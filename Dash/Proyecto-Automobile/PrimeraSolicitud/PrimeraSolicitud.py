import dash
from dash import html, dcc, Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go   
from Metrica_Inversion_Individual import generar_grafico_metrica, inversiones   

app = dash.Dash(__name__)

# Leer el CSV con los datos
csv_file = r"C:\Users\josep\OneDrive\Escritorio\Proyectos-Junior\Dash\Proyecto-Automobile\PrimeraSolicitud\csv\PrimeraSolicitud.csv"
df = pd.read_csv(csv_file)

# Figura original sin filtro
figura_grafica_principal_PriceMake = px.bar(df, x="make", y="price", title="Precio por Marca",
              color="make", template="plotly_white", opacity=0.9)

figura_grafica_principal_PriceMake.update_layout(
    showlegend=False,
    margin=dict(l=20, r=20, t=40, b=20),
    height=500,
    width=1000
)

# Dropdown para seleccionar una marca
dropdown_makes = dcc.Dropdown(
    id="dropdown-make",
    options=[{"label": make, "value": make} for make in df["make"].unique()],
    placeholder="Seleccione una marca",
    multi=False,
    style={"width": "100%", "margin-bottom": "10px"}
)

@app.callback(
    [Output("price-make", "figure"), Output("grafico-metrica", "figure"),
     Output("suma-total", "children"), Output("unidades-total", "children"),
     Output("venta-mayor", "children"), Output("venta-menor", "children"),
     Output("grafico-metria-inversion", "figure"),
     Output("ganancia-perdida-porcentaje", "children")],
    [Input("dropdown-make", "value")]
)

def actualizar_graficos(selected_make):
    grafico_inversion = generar_grafico_metrica(df, selected_make)

    if selected_make:
        filtered_df = df[df["make"] == selected_make]
        total_price = filtered_df["price"].sum()
        total_unidades = filtered_df["make"].count()
        venta_mayor = filtered_df["price"].max()
        venta_menor = filtered_df["price"].min()

        # Obtener la inversión de la marca seleccionada
        inversion_marca = inversiones.get(selected_make.lower(), 0)

        # Calcular ganancia o pérdida
        ganancia_perdida = total_price - inversion_marca
        porcentaje_ganancia = (ganancia_perdida / inversion_marca * 100) if inversion_marca > 0 else 0

        # Crear gráficos
        figura_metrica = go.Figure()
        df_agrupado = df.groupby("make")["price"].sum().reset_index()

        figura_metrica.add_trace(go.Scatter(
            x=df_agrupado["make"],
            y=df_agrupado["price"],
            mode="lines+markers",
            line=dict(color="black", width=2),
            marker=dict(size=8)
        ))
        figura_metrica.update_layout(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            showlegend=False,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=0, r=0, t=0, b=0)
        )

        figura_grafica_filtro_MarcaPrice = px.bar(
            filtered_df, x=filtered_df.index, y="price",
            title=f"Precios de vehículos {selected_make.upper()}",
            color_discrete_sequence=["blue"],
            template="plotly_white",
            opacity=0.9
        )

        return (
            figura_grafica_filtro_MarcaPrice, figura_metrica,
            f"Venta Total: ${total_price:,}", f"Unidades Vendidas: {total_unidades:,}",
            f"Venta Mayor: ${venta_mayor:,}", f"Venta Menor: ${venta_menor:,}",
            grafico_inversion, f"%: {porcentaje_ganancia:.2f}%"
        )
    
    # **Caso General (todas las marcas)**
    total_general = df["price"].sum()
    total_general_unidades = df["make"].count()
    total_mayor = df["price"].max()
    total_menor = df["price"].min()

    # Inversión total
    inversion_total = sum(inversiones.values())
    ganancia_total = total_general - inversion_total
    porcentaje_ganancia_total = (ganancia_total / inversion_total * 100) if inversion_total > 0 else 0

    figura_metrica = go.Figure()
    df_agrupado = df.groupby("make")["price"].sum().reset_index()

    figura_metrica.add_trace(go.Scatter(
        x=df_agrupado["make"],
        y=df_agrupado["price"],
        mode="lines+markers",
        line=dict(color="black", width=2),
        marker=dict(size=8)
    ))
    figura_metrica.update_layout(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        showlegend=False,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=0, r=0, t=0, b=0)
    )

    return (
        figura_grafica_principal_PriceMake, figura_metrica,
        f"Venta Total: ${total_general:,}", f"Unidades Vendidas: {total_general_unidades:,}",
        f"Venta Mayor: ${total_mayor:,}", f"Venta Menor: ${total_menor:,}",
        grafico_inversion, f"%: {porcentaje_ganancia_total:.2f}%"
    )


# Definir el diseño de la aplicación
app.layout = html.Div([
    html.Link(),
    html.Div(className="grid-container", children=[
        html.Div(className="cuadro price-make", children=[dcc.Graph(id="price-make", figure=figura_grafica_principal_PriceMake)]),
        html.Div(className="cuadro filtro", children=[dropdown_makes]),
        html.Div(id="suma-total", className="cuadro sumatotal", children=["Suma Total: $0"]),
        html.Div(className="cuadro metrica", children=[dcc.Graph(id="grafico-metrica")]),
        html.Div(className="cuadro metriaInversion", children=[dcc.Graph(id="grafico-metria-inversion", figure={})]),
        html.Div(id="unidades-total", className="cuadro unidadestotal", children=["Suma Total: $0"]),
        html.Div(id="ganancia-perdida-porcentaje", className="cuadro ganancia_perdida_porcentaje", children=["%: 0%"]),
        html.Div(id="venta-mayor", className="cuadro ventamayor", children=["Suma Total: $0"]),
        html.Div(id="venta-menor", className="cuadro ventamenor", children=["Suma Total: $0"]),
    ])
], className="container")

if __name__ == "__main__":
    app.run(debug=True)
