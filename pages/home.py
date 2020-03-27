import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as do
from app import app
from datetime import datetime
from data import data_parse_home
from flask_login import current_user

textSize = 21
numberSize = 65

jumbotron = dbc.Jumbotron(
	[
		html.H1(id='display-user',className="display-3"),
		html.P(id='time', className="lead"),
		html.Hr(className="my-2"),
		html.P(
            "Konoha City Administration - Planning & Development Department"
		),
		html.Div(id='dummy',style={'display':'none'})
	]
)

body = dcc.Loading(dbc.Container([
	dbc.Row([
		dbc.Row(html.H2("Summary", className='ml-3'),
		no_gutters=True,
		style={'backgroundColor':'#f7f3e7','width':'100%'}),
		dbc.Row([
			dbc.Col(
				dbc.Col(
					dbc.Row(
						dcc.Graph(id='chart-1',config={'displayModeBar': False},style={'height':'100%','width':'100%'})
					)
				)
			,lg=3),
			dbc.Col(
				dbc.Col(
					dbc.Row(
						dcc.Graph(id='chart-2',config={'displayModeBar': False},style={'height':'100%','width':'100%'})
					)
				)
			,lg=3),
			dbc.Col(
				dbc.Col(
					dbc.Row(
						dcc.Graph(id='chart-3',config={'displayModeBar': False},style={'height':'100%','width':'100%'})
					)
				)
			,lg=3),
			dbc.Col(
				dbc.Col(
					dbc.Row(
						dcc.Graph(id='chart-4',config={'displayModeBar': False},style={'height':'100%','width':'100%'})
					)
				)
			,lg=3),
		],
		id='chart-rows',
		no_gutters=True,
		style={'width':'100%'}),
		dbc.Row([
			dbc.Col(
				dbc.Col(
					dbc.Row(
						dcc.Graph(id='chart-5',config={'displayModeBar': False},style={'height':'100%','width':'100%'})
					)
				)
			,md=6),
			dbc.Col(
				dbc.Col(
					dbc.Row(
						dcc.Graph(id='chart-6',config={'displayModeBar': False},style={'height':'100%','width':'100%'})
					)
				)
			,md=6),
		],
		#id='chart-rows',
		className='mb-5 mt-2',
		no_gutters=True,
		style={'width':'100%'}),
		dbc.Row(html.H5("Inspections by Trade", className='ml-3 mt-1'),
		no_gutters=True,
		style={'backgroundColor':'#f7f3e7','width':'50%'}),
		dbc.Row([
			dbc.Col(
				dbc.Col(
					dbc.Row(
						dcc.Graph(id='chart-7',config={'displayModeBar': False},style={'height':'100%','width':'100%'})
					)
				)
			,lg=3),
			dbc.Col(
				dbc.Col(
					dbc.Row(
						dcc.Graph(id='chart-8',config={'displayModeBar': False},style={'height':'100%','width':'100%'})
					)
				)
			,lg=3),
			dbc.Col(
				dbc.Col(
					dbc.Row(
						dcc.Graph(id='chart-9',config={'displayModeBar': False},style={'height':'100%','width':'100%'})
					)
				)
			,lg=3),
			dbc.Col(
				dbc.Col(
					dbc.Row(
						dcc.Graph(id='chart-10',config={'displayModeBar': False},style={'height':'100%','width':'100%'})
					)
				)
			,lg=3),
		],
		#id='chart-rows',
		className='mb-4 mt-5',
		no_gutters=True,
		style={'width':'100%'})
		
		
	],id='layout-content')
],
className='shadow',
style={'backgroundColor':'#ffffff',}), type='dot', color='#536391')

layout = [jumbotron,body]

@app.callback(
	[Output('display-user','children'),
	Output('time','children')],
	[Input('dummy','children')]
)
def update_time(child):
	name = str(current_user.username)
	user = "Welcome, {}.".format(name)

	now = datetime.now()
	day = datetime.today().strftime('%A')
	today = now.strftime("%Y-%m-%d | Current time is %H:%M")
	time = "Today is {}, {}".format(day, today)
	
	return user,time

@app.callback(
	[Output('chart-1','figure'),
	Output('chart-2','figure'),
	Output('chart-3','figure'),
	Output('chart-4','figure'),
	Output('chart-5','figure'),
	Output('chart-6','figure'),
	Output('chart-7','figure'),
	Output('chart-8','figure'),
	Output('chart-9','figure'),
	Output('chart-10','figure')],
	[Input('dummy','children')]
)
def update_charts(child):
	app_vol,comm_perm_df,resi_perm,perm_iss,insp_trade_df = data_parse_home()
	
	df_comm = comm_perm_df.tail(6)
	df_res = resi_perm.tail(6)
	df_insp = insp_trade_df.tail(4)
	df_trade = list(df_insp['trade'].unique())
	df_percent = list(df_insp['percent'])
	colored = ['#6c5391','#f7f3e7']
	
	plot1 = do.Figure(do.Indicator(
			mode= 'number',
			value= app_vol.tail(1)['totalcount'].values[0],
			title = {'text':'Permit Application Volume','font':{'size':textSize,'family':'Source Sans Pro'}},
			number={'font':{'size':numberSize}}))
	
	plot2 = do.Figure(do.Indicator(
			mode= 'number',
			value= comm_perm_df.tail(1)['totalcount'].values[0],
			title = {'text':'Total Commercial Permits','font':{'size':textSize,'family':'Source Sans Pro'}},
			number={'font':{'size':numberSize}}))

	plot3 = do.Figure(do.Indicator(
			mode= 'number',
			value= resi_perm.tail(1)['totalcount'].values[0],
			title = {'text':'Total Residential Permits','font':{'size':textSize,'family':'Source Sans Pro'}},
			number={'font':{'size':numberSize}}))
			
	plot4 = do.Figure(do.Indicator(
			mode= 'number',
			value= perm_iss.tail(1)['avgdays'].values[0],
			title = {'text':'Average Issuance Days','font':{'size':textSize,'family':'Source Sans Pro'}},
			number={'font':{'size':numberSize}}))

	plot1.update_layout(margin= do.layout.Margin(t=0,b=0),height=200)
	plot2.update_layout(margin= do.layout.Margin(t=0,b=0),height=200)
	plot3.update_layout(margin= do.layout.Margin(t=0,b=0),height=200)
	plot4.update_layout(margin= do.layout.Margin(t=0,b=0),height=200)

	plot5 = do.Figure(do.Bar(
			x= df_comm['PERMITISSUEDATE'],
			y= df_comm['totalcount'],
			name='Total Count',
			marker_color='#d39951'))
			
	plot5.update_layout(margin= do.layout.Margin(t=40,b=15,r=0,l=0),
					title={'text':'Total Commercial Permits by Month','font':{'size':textSize,'family':'Source Sans Pro'}},
					showlegend=False, plot_bgcolor='#ffffff', hovermode='x', height=225,
					xaxis={'showgrid':False,'showticklabels':True},
					yaxis={'showgrid':False,'showticklabels':False})
					
	plot6 = do.Figure(do.Bar(
			x= df_res['PERMITISSUEDATE'],
			y= df_res['totalcount'],
			name='Total Count',
			marker_color='#c05e4a'))
			
	plot6.update_layout(margin= do.layout.Margin(t=40,b=20,r=0,l=0),
					title={'text':'Total Residential Permits by Month','font':{'size':textSize,'family':'Source Sans Pro'}},
					showlegend=False, plot_bgcolor='#ffffff', hovermode='x', height=225,
					xaxis={'showgrid':False,'showticklabels':True},
					yaxis={'showgrid':False,'showticklabels':False})

	plot7 = do.Figure(do.Pie(
			labels=[df_trade[0],'Rest of trades'],
			values=[df_percent[0],100-df_percent[0]],
			hole=0.8))
	
	plot7.update_traces(hoverinfo='label+percent', textinfo='none', marker={'colors':colored})	
	plot7.update_layout(margin= do.layout.Margin(t=40,b=0,r=0,l=0),
					title={'text':'Building','font':{'size':textSize,'family':'Source Sans Pro'}},
					showlegend=False, plot_bgcolor='#ffffff', height=225,
					annotations=[{'text':str(df_percent[0])+'%','x':0.5,'y':0.5,'font':{'size':40},'showarrow':False}])
	
	plot8 = do.Figure(do.Pie(
			labels=[df_trade[1],'Rest of trades'],
			values=[df_percent[1],100-df_percent[1]],
			hole=0.8))
	
	plot8.update_traces(hoverinfo='label+percent', textinfo='none', marker={'colors':colored})		
	plot8.update_layout(margin= do.layout.Margin(t=40,b=0,r=0,l=0),
					title={'text':'Electrical','font':{'size':textSize,'family':'Source Sans Pro'}},
					showlegend=False, plot_bgcolor='#ffffff', height=225,
					annotations=[{'text':str(df_percent[1])+'%','x':0.5,'y':0.5,'font':{'size':40},'showarrow':False}])
	
	plot9 = do.Figure(do.Pie(
			labels=[df_trade[2],'Rest of trades'],
			values=[df_percent[2],100-df_percent[2]],
			hole=0.8))
	
	plot9.update_traces(hoverinfo='label+percent', textinfo='none', marker={'colors':colored})		
	plot9.update_layout(margin= do.layout.Margin(t=40,b=0,r=0,l=0),
					title={'text':'Other Trades','font':{'size':textSize,'family':'Source Sans Pro'}},
					showlegend=False, plot_bgcolor='#ffffff', height=225,
					annotations=[{'text':str(df_percent[2])+'%','x':0.5,'y':0.5,'font':{'size':40},'showarrow':False}])
	
	plot10 = do.Figure(do.Pie(
			labels=[df_trade[3],'Rest of trades'],
			values=[df_percent[3],100-df_percent[3]],
			hole=0.8))
	
	plot10.update_traces(hoverinfo='label+percent', textinfo='none', marker={'colors':colored})	
	plot10.update_layout(margin= do.layout.Margin(t=40,b=0,r=0,l=0),
					title={'text':'Plumbing/Mechanical/Gas','font':{'size':textSize,'family':'Source Sans Pro'}},
					showlegend=False, plot_bgcolor='#ffffff', height=225,
					annotations=[{'text':str(df_percent[3])+'%','x':0.5,'y':0.5,'font':{'size':40},'showarrow':False}])
	
	return plot1,plot2,plot3,plot4,plot5,plot6,plot7,plot8,plot9,plot10

