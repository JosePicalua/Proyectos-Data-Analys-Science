import plotly.graph_objects as go
import pandas as pd

# Diccionario de inversión por marca
inversiones = {'toyota': 10000, 'bmw': 20000, 'ford': 30000}

def generar_grafico_metrica(df, selected_make):
    filtered_df = df[df["make"] == selected_make] if selected_make else df

    if selected_make in inversiones:
        y2_value = inversiones[selected_make]
    else:
        y2_value = 0  # Si no hay inversión definida
    
    fig = go.Figure()
    
    # Área de pérdida (rojo)
    fig.add_trace(go.Scatter(
        x=filtered_df.index,
        y=[y2_value] * len(filtered_df),
        fill=None,
        mode='lines',
        line=dict(color='rgba(255, 0, 0, 0)')
    ))
    fig.add_trace(go.Scatter(
        x=filtered_df.index,
        y=filtered_df['price'],
        fill='tonexty',
        mode='lines',
        line=dict(color='red', width=4),
        fillcolor='rgba(63, 245, 93, 0.8)',  # Verde (ganancia)
        showlegend=False
    ))
    
    # Área de ganancia (verde)
    fig.add_trace(go.Scatter(
        x=filtered_df.index,
        y=[max(p, y2_value) for p in filtered_df['price']],
        fill='tonexty',
        mode='lines',
        line=dict(color='green', width=4),
        fillcolor='rgba(246, 36, 36, 0.8)',  # Rojo (pérdida)
        showlegend=False
    ))
    
    # Línea de inversión
    fig.add_trace(go.Scatter(
        x=filtered_df.index,
        y=[y2_value] * len(filtered_df),
        mode='lines',
        line=dict(color='white', dash='dash'),
        showlegend=False
    ))
    
    fig.update_layout(
        title=f'Métrica de Inversión - {selected_make.upper() if selected_make else "General"}',
        xaxis=dict(showticklabels=False, showgrid=False, zeroline=False),
        yaxis=dict(showticklabels=False, showgrid=False, zeroline=False),
        plot_bgcolor='white',
        showlegend=False
    )
    
    return fig
