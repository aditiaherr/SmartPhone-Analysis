
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Load dataset using pandas
df = pd.read_csv("smartphones.csv")

# Function to integrate Dash into Flask
def add_dashboard(server):
    # Create a Dash app attached to the Flask app
    dash_app = dash.Dash(__name__, server=server, routes_pathname_prefix='/dashboard/')

    # Layout of the dashboard
    dash_app.layout = html.Div([
        html.H1("Smartphones Price Prediction Analysis", style={'textAlign': 'center', 'color': '#4B0082', 'fontSize': 40}),
        
        html.Div([
            dcc.Dropdown(
                id='brand-filter',
                options=[{'label': brand, 'value': brand} for brand in df['Brand me'].unique()],
                value=None,
                placeholder="Select a Brand",
                multi=True
            )
        ], style={'width': '50%', 'margin': '0 auto'}),

        html.Div([
            dcc.Graph(id='price-by-brand', style={'display': 'inline-block', 'width': '48%'}),
            dcc.Graph(id='rating-by-brand', style={'display': 'inline-block', 'width': '48%'}),
        ]),

        html.Div([
            dcc.Graph(id='price-by-ram', style={'display': 'inline-block', 'width': '48%'}),
            dcc.Graph(id='price-by-rom', style={'display': 'inline-block', 'width': '48%'}),
        ]),

        html.Div([
            dcc.Graph(id='price-by-screen-size', style={'display': 'inline-block', 'width': '48%'}),
            dcc.Graph(id='battery-power-chart', style={'display': 'inline-block', 'width': '48%'}),
        ]),

        html.Div([
            dcc.Graph(id='selfie-vs-primary-camera', style={'display': 'inline-block', 'width': '48%'}),
        ]),
    ], style={'backgroundColor': '#f0f0f0', 'padding': '20px'})

    # Callbacks to update charts dynamically
    @dash_app.callback(
        [
            Output('price-by-brand', 'figure'),
            Output('rating-by-brand', 'figure'),
            Output('price-by-ram', 'figure'),
            Output('price-by-rom', 'figure'),
            Output('price-by-screen-size', 'figure'),
            Output('battery-power-chart', 'figure'),
            Output('selfie-vs-primary-camera', 'figure')
        ],
        [Input('brand-filter', 'value')]
    )
    def update_charts(selected_brands):
        filtered_df = df if not selected_brands else df[df['Brand me'].isin(selected_brands)]

        # Bar chart for Avg. Price by Brand
        price_by_brand_fig = px.bar(
            filtered_df, x='Brand me', y='Price', title="Avg. price of brand",
            labels={'Price': 'Avg. Price'}, color='Brand me'
        )

        price_by_brand_fig.update_layout(showlegend=False, template='plotly_dark')

        # Scatter plot for Ratings by Brand
        rating_by_brand_fig = px.scatter(
            filtered_df, x='Ratings', y='Price', color='Brand me', title="Ratings vs Price by Brand",
            labels={'Ratings': 'Avg. Ratings'}, size='Price', hover_name='Brand me'
        )
        rating_by_brand_fig.update_layout(showlegend=False, template='plotly_dark')

        # Line chart for Avg. Price by RAM
        price_by_ram_fig = px.line(
            filtered_df, x='RAM', y='Price', title="Avg. price by RAM",
            labels={'RAM': 'RAM (GB)', 'Price': 'Avg. Price (₹)'}, markers=True
        )
        price_by_ram_fig.update_layout(template='plotly_dark')

        # Bar chart for Price by ROM
        price_by_rom_fig = px.bar(
            filtered_df, x='ROM', y='Price', title="Price vs ROM (Internal Memory)",
            labels={'ROM': 'Internal Memory (GB)', 'Price': 'Price (₹)'}, color='Brand me'
        )
        price_by_rom_fig.update_layout(template='plotly_dark')

        # Scatter plot for Price vs Screen Size
        price_by_screen_size_fig = px.scatter(
            filtered_df, x='Mobile_Size', y='Price', title="Price vs Mobile Size",
            labels={'Mobile_Size': 'Screen Size (inches)', 'Price': 'Price (₹)'}, size='Price', color='Brand me'
        )
        price_by_screen_size_fig.update_layout(template='plotly_dark')

        # Pie chart for Battery Power distribution
        battery_power_chart_fig = px.pie(
            filtered_df, names='Brand me', values='Battery_Power', title="Battery Power Distribution by Brand"
        )
        battery_power_chart_fig.update_traces(textinfo='percent+label')
        battery_power_chart_fig.update_layout(template='plotly_dark')

        # Scatter plot for Primary Camera vs Selfie Camera
        selfie_vs_primary_camera_fig = px.scatter(
            filtered_df, x='Primary_Cam', y='Selfi_Cam', size='Price', color='Brand me',
            title="Primary Camera vs Selfie Camera with Price",
            labels={'Primary_Cam': 'Primary Camera (MP)', 'Selfi_Cam': 'Selfie Camera (MP)'}
        )
        selfie_vs_primary_camera_fig.update_layout(template='plotly_dark')

        return (price_by_brand_fig, rating_by_brand_fig, price_by_ram_fig, price_by_rom_fig,
                price_by_screen_size_fig, battery_power_chart_fig, selfie_vs_primary_camera_fig)

    return dash_app
