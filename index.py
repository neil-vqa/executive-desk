import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app, server
from pages import home, operations, reports, login
from flask_login import logout_user, current_user


navbar = dbc.NavbarSimple([
	dbc.NavItem(dbc.NavLink("Home", href="/home", id="page-1-link")),
	dbc.NavItem(dbc.NavLink("Operations", href="/operations", id="page-2-link")),
	dbc.NavItem(dbc.NavLink("Reports", href="/reports", id="page-3-link")),
	dbc.NavItem(dbc.NavLink("Logout", href="/logout", id="page-4-link")),
],
id='navs',
brand="Executive Desk",
color="dark",
dark=True)


content = html.Div(id="page-content")


def serve_layout():
	return html.Div([dcc.Location(id="url"), navbar, content])

app.layout = serve_layout
    

@app.callback(
	[Output("navs",component_property='style'),
	Output("page-content", "children")],
	[Input("url", "pathname")]
)
def render_content(pathname):
	if current_user.is_authenticated:
		if pathname in ["/home","/"]:
			return {'backgroundColor':'#343758'},home.layout
		elif pathname in ["/operations"]:
			return {'backgroundColor':'#343758'},operations.layout
		elif pathname in ["/reports"]:
			return {'backgroundColor':'#343758'},reports.layout
		elif pathname in ["/logout"]:
			logout_user()
			return {'transform':'scale(0)'},login.layout
	else:
		return {'transform':'scale(0)'},login.layout

if __name__ == "__main__":
    app.run_server(debug=False)
