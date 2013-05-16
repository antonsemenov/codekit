from ideone import Ideone
import time
i = Ideone('antonsemenov', 'abc123123')	

def checkSolution(taskd , code, checkers):
	p = {}
	p['result'] = 'Success'	
	for e in checkers:
		currSubmission = i.create_submission(code, language_name='python', std_input=e.input_value)
		while (i.submission_status(currSubmission['link'])['status'] != 0):
			time.sleep(1)
		if (i.submission_details(currSubmission['link'])['result'] != 15):
			p['result'] = 'Fail'
			break
	return p
