from dash import Dash, html, page_container, page_registry
import dash_bootstrap_components as dbc

app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.layout = dbc.Container([
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink(page["name"], href=page["relative_path"]))
            for page in sorted(
                page_registry.values(), # Hämtar alla registrerade sidor i pages mappen
                key=lambda page: (
                    0 if page["name"] == "Home"
                    else int(page["name"].replace("Question", ""))
                )
            )
        ],
        brand="Group 7 Dataset Visualization",
        color="dark", # Gör navbaren mörk
        dark=True # Gör texterna anpasat för mörk bakgrund
    ),
    page_container  # Visar inehållet på den valda sidan
], fluid=True) # Använder hela sidbredden

if __name__ == "__main__":
    app.run(debug=True)