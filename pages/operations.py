import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as do
import plotly.express as px
from app import app
from data import data_parse_ops


layout = dcc.Loading(dbc.Container([
	dbc.Row([
		html.Div(id='dummy-ops',style={'display':'none'}),
		dbc.Row(html.H2("Operations", className='ml-3'),
		no_gutters=True,
		style={'backgroundColor':'#f7f3e7','width':'100%'}),
		dbc.Row(html.H5("Inspections by Trade (Total Count)", className='ml-3 mt-1'),
		no_gutters=True,
		className='mt-2',
		style={'backgroundColor':'#f7f3e7','width':'70%'}),
		dbc.Row([
			dbc.Col(
				dbc.Col(
					dbc.Row(
						dcc.Graph(id='line-1',config={'displayModeBar': False},style={'height':'100%','width':'100%'})
					)
				)
			,md=12)
		],
		id='chart-rows',
		no_gutters=True,
		style={'width':'100%'}),
		dbc.Row(html.H5("Inspections by Trade (Percent)", className='ml-3 mt-1'),
		no_gutters=True,
		className='mt-4',
		style={'backgroundColor':'#f7f3e7','width':'70%'}),
		dbc.Row([
			dbc.Col(
				dbc.Col(
					dbc.Row(
						dcc.Graph(id='bar-1',config={'displayModeBar': False},style={'height':'100%','width':'100%'})
					)
				)
			,md=12)
		],
		id='chart-rows',
		no_gutters=True,
		style={'width':'100%'}),
		dbc.Row(html.H5("Inspection Results (Percent)", className='ml-3 mt-1'),
		no_gutters=True,
		className='mt-4',
		style={'backgroundColor':'#f7f3e7','width':'70%'}),
		dbc.Row(html.H5("Building", className='ml-3 mt-1'),
		no_gutters=True,
		className='mt-2',
		style={'backgroundColor':'#f7f3e7','width':'50%'}),
		dbc.Row([
			dbc.Col(
				dbc.Col(
					dbc.Row(
						dcc.Graph(id='bar-res-1',config={'displayModeBar': False},style={'height':'100%','width':'100%'})
					)
				)
			,md=12)
		],
		id='chart-rows',
		no_gutters=True,
		style={'width':'100%'}),
		dbc.Row(html.H5("Electrical", className='ml-3 mt-1'),
		no_gutters=True,
		className='mt-2',
		style={'backgroundColor':'#f7f3e7','width':'50%'}),
		dbc.Row([
			dbc.Col(
				dbc.Col(
					dbc.Row(
						dcc.Graph(id='bar-res-2',config={'displayModeBar': False},style={'height':'100%','width':'100%'})
					)
				)
			,md=12)
		],
		id='chart-rows',
		no_gutters=True,
		style={'width':'100%'}),
		dbc.Row(html.H5("Other Trades", className='ml-3 mt-1'),
		no_gutters=True,
		className='mt-2',
		style={'backgroundColor':'#f7f3e7','width':'50%'}),
		dbc.Row([
			dbc.Col(
				dbc.Col(
					dbc.Row(
						dcc.Graph(id='bar-res-3',config={'displayModeBar': False},style={'height':'100%','width':'100%'})
					)
				)
			,md=12)
		],
		id='chart-rows',
		no_gutters=True,
		style={'width':'100%'}),
		dbc.Row(html.H5("Plumbing/Mechanical/Gas", className='ml-3 mt-1'),
		no_gutters=True,
		className='mt-2',
		style={'backgroundColor':'#f7f3e7','width':'50%'}),
		dbc.Row([
			dbc.Col(
				dbc.Col(
					dbc.Row(
						dcc.Graph(id='bar-res-4',config={'displayModeBar': False},style={'height':'100%','width':'100%'})
					)
				)
			,md=12)
		],
		id='chart-rows',
		no_gutters=True,
		style={'width':'100%'}),
		dbc.Row(html.H5("Total Inspections by Type", className='ml-3 mt-1'),
		no_gutters=True,
		className='mt-4',
		style={'backgroundColor':'#f7f3e7','width':'70%'}),
		dbc.Row([
			dbc.Col(
				dbc.Col(
					dbc.Row(
						dcc.Graph(id='line-2',config={'displayModeBar': False},style={'height':'100%','width':'100%'})
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
	[Output('line-1','figure'),
	Output('bar-1','figure'),
	Output('bar-res-1','figure'),
	Output('bar-res-2','figure'),
	Output('bar-res-3','figure'),
	Output('bar-res-4','figure'),
	Output('line-2','figure'),],
	[Input('dummy-ops','children')]
)
def update_charts(child):
	insp_trade_df,insp_trade_res,insp_type = data_parse_ops()
	
	build_df = insp_trade_res.loc[insp_trade_res['trade']=='Building']
	elect_df = insp_trade_res.loc[insp_trade_res['trade']=='Electrical']
	other_df = insp_trade_res.loc[insp_trade_res['trade']=='Other']
	mech_df = insp_trade_res.loc[insp_trade_res['trade']=='Plumbing/Mechanical/Gas']
	
	plot1 = px.line(insp_trade_df, x='RESULTDATE', y='totalcount', color='trade',
				labels={'RESULTDATE':'Date','totalcount': 'Count','trade':'Trade'},
				template='seaborn')
				
	plot1.update_layout(margin= do.layout.Margin(t=0,b=0),showlegend=True, plot_bgcolor='#ffffff', hovermode='x', height=300,
					xaxis={'showgrid':False,'showticklabels':True,'title':{'text':''}},
					yaxis={'showgrid':False,'showticklabels':True})
	
	plot2 = px.bar(insp_trade_df, x='RESULTDATE', y='percent', color='trade',
				labels={'RESULTDATE':'Date','percent': 'Percent','trade':'Trade'},
				template='seaborn')
	
	plot2.update_layout(margin= do.layout.Margin(t=0,b=0),showlegend=True, plot_bgcolor='#ffffff', hovermode='x', height=300,
					xaxis={'showgrid':False,'showticklabels':True,'title':{'text':''}},
					yaxis={'showgrid':False,'showticklabels':True})
	
	plot3 = px.bar(build_df, x='RESULTDATE', y='percent', color='INSPECTIONRESULT',
				labels={'RESULTDATE':'Date','percent': 'Percent','INSPECTIONRESULT':'Result'},
				template='seaborn')
				
	plot3.update_layout(margin= do.layout.Margin(t=0,b=0),showlegend=True, plot_bgcolor='#ffffff', hovermode='x', height=300,
					xaxis={'showgrid':False,'showticklabels':True,'title':{'text':''}},
					yaxis={'showgrid':False,'showticklabels':True})
	
	plot4 = px.bar(elect_df, x='RESULTDATE', y='percent', color='INSPECTIONRESULT',
				labels={'RESULTDATE':'Date','percent': 'Percent','INSPECTIONRESULT':'Result'},
				template='seaborn')
				
	plot4.update_layout(margin= do.layout.Margin(t=0,b=0),showlegend=True, plot_bgcolor='#ffffff', hovermode='x', height=300,
					xaxis={'showgrid':False,'showticklabels':True,'title':{'text':''}},
					yaxis={'showgrid':False,'showticklabels':True})
					
	plot5 = px.bar(other_df, x='RESULTDATE', y='percent', color='INSPECTIONRESULT',
				labels={'RESULTDATE':'Date','percent': 'Percent','INSPECTIONRESULT':'Result'},
				template='seaborn')
				
	plot5.update_layout(margin= do.layout.Margin(t=0,b=0),showlegend=True, plot_bgcolor='#ffffff', hovermode='x', height=300,
					xaxis={'showgrid':False,'showticklabels':True,'title':{'text':''}},
					yaxis={'showgrid':False,'showticklabels':True})
	
	plot6 = px.bar(mech_df, x='RESULTDATE', y='percent', color='INSPECTIONRESULT',
				labels={'RESULTDATE':'Date','percent': 'Percent','INSPECTIONRESULT':'Result'},
				template='seaborn')
				
	plot6.update_layout(margin= do.layout.Margin(t=0,b=0),showlegend=True, plot_bgcolor='#ffffff', hovermode='x', height=300,
					xaxis={'showgrid':False,'showticklabels':True,'title':{'text':''}},
					yaxis={'showgrid':False,'showticklabels':True})
	
	plot7 = px.line(insp_type, x='RESULTDATE', y='totalcount', color='INSPECTION_DESC',
				labels={'RESULTDATE':'Date','totalcount': 'Count','INSPECTION_DESC':'Inspection Type/Description'},
				template='seaborn')
				
	plot7.update_layout(margin= do.layout.Margin(t=0,b=0),showlegend=True, plot_bgcolor='#ffffff', hovermode='x', height=300,
					xaxis={'showgrid':False,'showticklabels':True,'title':{'text':''}},
					yaxis={'showgrid':False,'showticklabels':True})
	
	return plot1,plot2,plot3,plot4,plot5,plot6,plot7

