from dash import Dash, htmls
import dash_ag_grid as dag
from utils import get_reservations_data

data = []

reservations = get_reservations_data("test.db")

app = Dash()

if __name__ == "__main__":
    app.run(debug=True)