from ideone import Ideone
import time
i = Ideone('antonsemenov', 'abc123123')	

def checkSolution(code, checkers, langId):
	p = {}
	p['result'] = 'This is win!'
	for e in checkers:
		currSubmission = i.create_submission(code, language_id = langId, std_input=e.input_value)
		while (i.submission_status(currSubmission['link'])['status'] != 0):
			time.sleep(1)
		if (i.submission_details(currSubmission['link'])['result'] != 15):
			p['result'] = 'Fail, sorry'
			break
	return p
