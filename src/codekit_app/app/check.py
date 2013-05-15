from ideone import Ideone
import time

def checkSolution(taskd , code):
	i = Ideone('antonsemenov', 'abc123123')
	currSubmission = i.create_submission(code, language_name='python', std_input='6')
	while (i.submission_status(currSubmission['link'])['status'] != 0):
		time.sleep(3)
	return i.submission_details(currSubmission['link'])
