from dash import Dash, html
import dash_ag_grid as dag
from utils import get_reservations_data

data = []

reservations = get_reservations_data("test.db")

app = Dash(__name__)

columnDefs = [
    { 'field': 'ID' },
    { 'field': 'Booking Date' },
    { 'field': 'Booking Time'},
    { 'field': 'Booking Name' },
    { 'field': 'Phone Number' },
    { 'field': 'People Number' }
]

grid = dag.AgGrid(
    id='reservation-table',
    rowData=reservations,
    columnDefs=columnDefs,
    style={
        "height": "100%",
        "width": "100%",  
    },
    className="ag-theme-alpine-dark"
)

app.layout = html.Div(
    [grid],
    style={
        "height": "100vh",
        "width": "100%",
        "margin": "0",
        "padding": "0"
    }
    )

if __name__ == "__main__":
    app.run(debug=True)