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
    { 'field': 'People Number' },
]

grid = dag.AgGrid(
    id='reservation-table',
    rowData=reservations,
    columnDefs=columnDefs,
    defaultColDef={
        "sortable": True,
        "filter": True,
        "resizable": True,
        "flex": 1
    },
    style={
        "height": "100%",
        "width": "100%",  
    },
    className="ag-theme-alpine-dark"
)

app.layout = html.Div(
    [
        grid,

        # Fixed Button for adding a new reservation
        html.Button(
            "+",
            id='open-modal-btn',
            style={
                "position": "fixed",
                "top": "50%",
                "right": "20px",
                "transform": "translateY(-50%)",
                "fontSize": "24px",
                "padding": "15px 25px",
                "backgroundColor": "#4CAF50",
                "color": "white",
                "border": "none",
                "borderRadius": "100%",
                "cursor": "pointer",
            }
        )
    ],
    style={
        "height": "100vh",
        "width": "100%",
        "margin": "0",
        "padding": "0"
    }
    )

if __name__ == "__main__":
    app.run(debug=True)