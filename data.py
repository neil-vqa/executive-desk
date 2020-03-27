import pandas as pd

	
def data_parse_home():
	app_vol = pd.read_csv('https://query.data.world/s/4ajgkqusikphkx4wopxcunnmyzrs5r')
	comm_perm_df = pd.read_csv('https://query.data.world/s/dsvzxfib7obokh44zshmnpp5fjhx6i')
	resi_perm = pd.read_csv('https://query.data.world/s/mfwqnpjsz34xzooerc3mxm2pomjonm')
	perm_iss = pd.read_csv('https://query.data.world/s/q3n43xk4ksewnwy23pj4aibrahf5gu')
	insp_trade_df = pd.read_csv('https://query.data.world/s/mcnhcsx2mzwzjn2xktyhgngvqemtav')
	
	return app_vol,comm_perm_df,resi_perm,perm_iss,insp_trade_df

def data_parse_ops():
	insp_trade_df = pd.read_csv('https://query.data.world/s/mcnhcsx2mzwzjn2xktyhgngvqemtav')
	insp_trade_res = pd.read_csv('https://query.data.world/s/bclvcjcpiw72z6tgpebahmx6h2sc32')
	insp_type = pd.read_csv('https://query.data.world/s/ibrafxfjgtgj4nedfdphcm3hrczw7t')
	
	return insp_trade_df,insp_trade_res,insp_type
	
def data_parse_reps():
	perm_iss = pd.read_csv('https://query.data.world/s/q3n43xk4ksewnwy23pj4aibrahf5gu')
	inspector_df = pd.read_csv('https://query.data.world/s/hnqck2hhadqfvbghhjycwmscoivva7')
	comm_perm_df = pd.read_csv('https://query.data.world/s/dsvzxfib7obokh44zshmnpp5fjhx6i')
	resi_perm = pd.read_csv('https://query.data.world/s/mfwqnpjsz34xzooerc3mxm2pomjonm')
	juris_df = pd.read_csv('https://query.data.world/s/hzetm3kxbgid7k7s5gg35e4n5s4fxl')
	
	return perm_iss,inspector_df,comm_perm_df,resi_perm,juris_df
