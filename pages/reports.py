import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as do
import plotly.express as px
import dash_table
from app import app
from data import data_parse_reps


layout = dcc.Loading(dbc.Container([
	dbc.Row([
		html.Div(id='dummy-reps',style={'display':'none'}),
		dbc.Row(html.H2("Reports", className='ml-3'),
		no_gutters=True,
		style={'backgroundColor':'#f7f3e7','width':'100%'}),
		dbc.Row(html.H5("Total Commercial & Residential Permits", className='ml-3 mt-1'),
		no_gutters=True,
		className='mt-2',
		style={'backgroundColor':'#f7f3e7','width':'70%'}),
		dbc.Row([
			dbc.Col(
				dbc.Col(
					dbc.Row(
						dcc.Graph(id='column-1',config={'displayModeBar': False},style={'height':'100%','width':'100%'})
					)
				)
			,md=12)
		],
		id='chart-rows',
		no_gutters=True,
		style={'width':'100%'}),
		dbc.Row(html.H5("Permits Issued by Jurisdiction", className='ml-3 mt-1'),
		no_gutters=True,
		className='mt-2',
		style={'backgroundColor':'#f7f3e7','width':'70%'}),
		dbc.Row([
			dbc.Col(
				dbc.Col(
					dbc.Row([
						dbc.Col(html.Div(id='table-div')),
						dbc.Col(html.Div(id='table-div2'))
					],justify='center')
				)
			)
		],
		id='chart-rows',
		no_gutters=True,
		style={'width':'100%'}),
		dbc.Row(html.H5("Average Permit Issuance Time", className='ml-3 mt-1'),
		no_gutters=True,
		className='mt-4',
		style={'backgroundColor':'#f7f3e7','width':'70%'}),
		dbc.Row([
			dbc.Col(
				dbc.Col(
					dbc.Row(
						dcc.Graph(id='day-line',config={'displayModeBar': False},style={'height':'100%','width':'100%'})
					)
				)
			,md=12)
		],
		id='chart-rows',
		no_gutters=True,
		style={'width':'100%'}),
		dbc.Row(html.H5("Inspections by Inspectors", className='ml-3 mt-1'),
		no_gutters=True,
		className='mt-4',
		style={'backgroundColor':'#f7f3e7','width':'70%'}),
		dbc.Row([
			dbc.Col(
				dbc.Col(
					dbc.Row(
						dcc.Graph(id='bar-hor1',config={'displayModeBar': False},style={'height':'100%','width':'100%'})
					)
				)
			,md=12)
		],
		id='chart-rows',
		no_gutters=True,
		style={'width':'100%'}),
		
	],id='layout-content')
],
className='shadow',
style={'backgroundColor':'#ffffff'}), type='dot', color='#536391')


@app.callback(
	[Output('column-1','figure'),
	Output('day-line','figure'),
	Output('bar-hor1','figure'),
	Output('table-div','children'),
	Output('table-div2','children')],
	[Input('dummy-reps','children')]
)
def update_charts(child):
	perm_iss,inspector_df,comm_perm_df,resi_perm,juris_df = data_parse_reps()
	
	inspector_trace = inspector_df.tail(50)
	juris_data = juris_df.head(8)
	juris_data.columns = ['Date','Jurisdiction','Count']
	juris_data2 = juris_df.tail(8)
	juris_data2.columns = ['Date','Jurisdiction','Count']
	
	plot1 = do.Figure(
		do.Bar(
			x= comm_perm_df['PERMITISSUEDATE'],
			y= comm_perm_df['totalcount'],
			name='Commercial',
			marker_color='#d39951'
		)
	)
	
	plot1.add_trace(
		do.Bar(
			x= resi_perm['PERMITISSUEDATE'],
			y= resi_perm['totalcount'],
			name='Residential',
			marker_color='#c05e4a'
		)
	)
	
	plot1.update_layout(margin= do.layout.Margin(t=0,b=0),showlegend=True, plot_bgcolor='#ffffff',
					hovermode='x', height=300, barmode='group',
					xaxis={'showgrid':False,'showticklabels':True,'title':{'text':''}},
					yaxis={'showgrid':False,'showticklabels':True,'title':{'text':'Count'}})
					
	plot2 = px.line(perm_iss, x='PERMITISSUEDATE', y='avgdays', template='seaborn',
				labels={'PERMITISSUEDATE':'For the Month', 'avgdays':'Average Number of Days'})
				
	plot2.update_layout(margin= do.layout.Margin(t=0,b=0),showlegend=True, plot_bgcolor='#ffffff', hovermode='x', height=300,
					xaxis={'showgrid':False,'showticklabels':True,'title':{'text':''}},
					yaxis={'showgrid':False,'showticklabels':True})
					
	plot3 = px.bar(inspector_trace, x='totalcount', y='RESULTDATE', color='INSPECTORNAME', template='seaborn', orientation='h',
				labels={'RESULTDATE':'Date','totalcount':'Inspections Done', 'INSPECTORNAME':'Name'})
				
	plot3.update_layout(margin= do.layout.Margin(t=0,b=0),showlegend=True, plot_bgcolor='#ffffff',
					barmode='group', height=1000,
					xaxis={'showgrid':False,'showticklabels':True,'title':{'text':''}},
					yaxis={'showgrid':False,'showticklabels':True,'title':{'text':''}})
	
	table1 = dash_table.DataTable(
		id='table',
		columns=[{'name': i, 'id': i} for i in list(juris_data.columns)],
		data = juris_data.to_dict('rows'),
		style_header={'backgroundColor':'#343a40','color':'#ffffff'},
		style_cell_conditional = [
			{
				'if':{'column_id':'Jurisdiction'},
				'textAlign': 'left'
			}
		],
		style_cell={'color':'#000000','padding':'5px'},
		style_as_list_view=True,
		css = [{'selector':'.row', 'rule':'margin: 0'}],
	)
	
	table2 = dash_table.DataTable(
		id='table',
		columns=[{'name': i, 'id': i} for i in list(juris_data2.columns)],
		data = juris_data2.to_dict('rows'),
		style_header={'backgroundColor':'#343a40','color':'#ffffff'},
		style_cell_conditional = [
			{
				'if':{'column_id':'Jurisdiction'},
				'textAlign': 'left'
			}
		],
		style_cell={'color':'#000000','padding':'5px'},
		style_as_list_view=True,
		css = [{'selector':'.row', 'rule':'margin: 0'}],
	)
	
	return plot1,plot2,plot3,table1,table2

