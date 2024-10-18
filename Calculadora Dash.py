import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc

# Inicializa o aplicativo Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout do aplicativo
app.layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(html.H1("Calculadora", className='text-center mb-4'), width=12)
        ),
        dbc.Row(
            dbc.Col(
                dcc.Dropdown(
                    id='operacao',
                    options=[
                        {'label': 'Multiplicação', 'value': '1'},
                        {'label': 'Divisão', 'value': '2'},
                        {'label': 'Soma', 'value': '3'},
                        {'label': 'Subtração', 'value': '4'},
                    ],
                    placeholder="Escolha uma operação",
                    value='1',
                    className='mb-3',
                    style={
                        'border': '2px solid #007bff',
                        'borderRadius': '5px',
                        'backgroundColor': '#ffffff'
                    }
                ),
                width=12
            ),
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Input(
                        id='num1',
                        type='text',
                        placeholder='Primeiro número',
                        value='',
                        className='mb-3',
                        style={
                            'border': '2px solid #007bff',
                            'borderRadius': '5px',
                            'backgroundColor': '#ffffff'
                        }
                    ),
                    width=6
                ),
                dbc.Col(
                    dcc.Input(
                        id='num2',
                        type='text',
                        placeholder='Segundo número',
                        value='',
                        className='mb-3',
                        style={
                            'border': '2px solid #007bff',
                            'borderRadius': '5px',
                            'backgroundColor': '#ffffff'
                        }
                    ),
                    width=6
                ),
            ],
            justify="center",
        ),
        dbc.Row(
            dbc.Col(
                html.Button(
                    'Calcular',
                    id='calcular',
                    n_clicks=0,
                    className='btn btn-primary btn-lg',
                    style={
                        'width': '100%',
                        'backgroundColor': '#007bff',
                        'border': 'none',
                        'borderRadius': '5px',
                        'transition': 'background-color 0.3s',
                        'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.2)'
                    }
                ),
                width=12
            )
        ),
        dbc.Row(
            dbc.Col(
                html.Div(
                    id='resultado',
                    style={
                        'margin-top': '20px',
                        'font-weight': 'bold',
                        'fontSize': '20px',
                        'textAlign': 'center',
                        'backgroundColor': '#f8f9fa',
                        'padding': '10px',
                        'borderRadius': '5px',
                        'boxShadow': '0 2px 5px rgba(0,0,0,0.1)'
                    }
                ),
                width=12
            )
        ),
    ],
    fluid=True,
    style={
        'backgroundColor': '#e9ecef',
        'padding': '40px',
        'borderRadius': '10px',
        'boxShadow': '0 4px 10px rgba(0,0,0,0.2)',
        'maxWidth': '600px',
        'margin': 'auto'
    }
)

# Callback para atualizar o resultado
@app.callback(
    Output('resultado', 'children'),
    Input('calcular', 'n_clicks'),
    Input('operacao', 'value'),
    Input('num1', 'value'),
    Input('num2', 'value')
)
def update_result(n_clicks, operacao, num1, num2):
    if n_clicks > 0:
        try:
            num1 = float(num1)
            num2 = float(num2)
            if operacao == '1':
                resultado = num1 * num2
                return f"Resultado da multiplicação: {resultado:.2f}"
            elif operacao == '2':
                if num2 == 0:
                    return "Erro: Divisão por zero não permitida."
                resultado = num1 / num2
                return f"Resultado da divisão: {resultado:.2f}"
            elif operacao == '3':
                resultado = num1 + num2
                return f"Resultado da soma: {resultado:.2f}"
            elif operacao == '4':
                resultado = num1 - num2
                return f"Resultado da subtração: {resultado:.2f}"
        except ValueError:
            return "Entrada inválida. Por favor, digite um número."
    return ""

# Executa o aplicativo
if __name__ == '__main__':
    app.run(debug=True)
