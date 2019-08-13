import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Set up the chart
beers=['Maibock', 'Troeginator', 'Vienna Lager', 'Pear Lager']
ibu_values=[35, 60, 85, 75]
abv_values=[6.4, 8.4, 6.2, 5.3]
color1='darkgrey'
color2='lightred'

bitterness = go.Bar(
    x=beers,
    y=ibu_values,
    name='IBU',
    marker={'color':color1}
)
alcohol = go.Bar(
    x=beers,
    y=abv_values,
    name='ABV',
    marker={'color':color2}
)

beer_data = [bitterness, alcohol]
beer_layout = go.Layout(
    barmode='group',
    title = 'Beer Comparison'
)

beer_fig = go.Figure(data=beer_data, layout=beer_layout)

########### Display the chart

app = dash.Dash()
server = app.server

app.layout = html.Div(children=[
    html.H1('Flying Dog Beers'),
    dcc.Graph(
        id='flyingdog',
        figure=beer_fig
    ),
    html.A('Code on Github', href='https://github.com/austinlasseter/flying-dog-beers'),
    html.Br(),
    html.A('Data Source', href='https://www.flyingdog.com/beers/'),
    ]
)

if __name__ == '__main__':
    app.run_server()
