import numpy as np 

def churn_data_process(**data):
	clfs = data['clfs']
	form_data = data['form_data']
	status = data['status']

	if form_data['internet_service'] == 0:
	    form_data['internet_service'] = [1,0,0]
	elif form_data['internet_service'] == 1:
	    form_data['internet_service'] = [0,1,0]
	elif form_data['internet_service'] == 2:
	    form_data['internet_service'] = [0,0,1]
    
	query = np.array([[form_data['tenure'], 
	                   form_data['internet_service'][0],form_data['internet_service'][1],
	                   form_data['internet_service'][2],
	                   form_data['payment_method']]])
	query = clfs['minmax_scaler'].transform(query)
	query = query.reshape(1,-1)

	results = {'svc_clf':{'status':status['svc_clf_status'],'predicted_result':'NULL', 'predicted_proba':0.0},
	            'knn_clf':{'status':status['knn_clf_status'], 'predicted_result':'NULL', 'predicted_proba':0.0}, 
	            'rand_clf':{'status':status['rand_clf_status'], 'predicted_result':'NULL', 'predicted_proba':0.0},
	            'ada_clf':{'status':status['ada_clf_status'], 'predicted_result':'NULL', 'predicted_proba':0.0}, 
	            'result':True}

	if status['svc_clf_status'] or status['knn_clf_status'] or status['rand_clf_status'] or status['ada_clf_status']:
		if status['svc_clf_status']:
			results['svc_clf']['predicted_result'] = clfs['svc_clf'].predict(query)[0]
			index = results['svc_clf']['predicted_result']
			results['svc_clf']['predicted_proba'] = clfs['svc_clf'].predict_proba(query)[0][index]
			results['svc_clf']['predicted_proba'] = np.round_(results['svc_clf']['predicted_proba'], decimals=4)

			if results['svc_clf']['predicted_result'] == 0:
			    results['svc_clf']['predicted_result'] = 'No Churn'
			elif results['svc_clf']['predicted_result'] == 1:
			    results['svc_clf']['predicted_result'] = 'Churn'

		if status['knn_clf_status']:
		    results['knn_clf']['predicted_result'] = clfs['knn_clf'].predict(query)[0]
		    index = results['knn_clf']['predicted_result']
		    results['knn_clf']['predicted_proba'] = clfs['knn_clf'].predict_proba(query)[0][index]
		    results['knn_clf']['predicted_proba'] = np.round_(results['knn_clf']['predicted_proba'], decimals=4)

		    if results['knn_clf']['predicted_result'] == 0:
		    	results['knn_clf']['predicted_result'] = 'No Churn'
		    elif results['knn_clf']['predicted_result'] == 1:
		    	results['knn_clf']['predicted_result'] = 'Churn'

		if status['rand_clf_status']:
		    results['rand_clf']['predicted_result'] = clfs['rand_clf'].predict(query)[0]
		    index = results['rand_clf']['predicted_result']
		    results['rand_clf']['predicted_proba'] = clfs['rand_clf'].predict_proba(query)[0][index]
		    results['rand_clf']['predicted_proba'] = np.round_(results['rand_clf']['predicted_proba'], decimals=4)

		    if results['rand_clf']['predicted_result'] == 0:
		    	results['rand_clf']['predicted_result'] = 'No Churn'
		    elif results['rand_clf']['predicted_result'] == 1:
		    	results['rand_clf']['predicted_result'] = 'Churn'

		if status['ada_clf_status']:
		    results['ada_clf']['predicted_result'] = clfs['ada_clf'].predict(query)[0]
		    index = results['ada_clf']['predicted_result']
		    results['ada_clf']['predicted_proba'] = clfs['ada_clf'].predict_proba(query)[0][index]
		    results['ada_clf']['predicted_proba'] = np.round_(results['ada_clf']['predicted_proba'], decimals=4)

		    if results['ada_clf']['predicted_result'] == 0:
		    	results['ada_clf']['predicted_result'] = 'No Churn'
		    elif results['ada_clf']['predicted_result'] == 1:
		    	results['ada_clf']['predicted_result'] = 'Churn'
	else:
		results['result'] = False

	return results
