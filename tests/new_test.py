import requests


class UnitTestClass:

    def email(self,data):
    	url = "http://127.0.0.1:5000/add_contact"
    	passed=0
    	failed=0  	 
  
    	for i in range(len(data)):
    	    r =  requests.post(url = url, data = data[i])
    	    if r.status_code == 200:
    	    	passed = passed+1
    	    else:
    	        failed = failed+1
    	    remark = r.text

    	return("Ran %d test,passed %d tests and failed %d tests for validation of email"%(len(data),passed,failed))        	
    	

    def number(self,data):
    	url = "http://127.0.0.1:5000/add_contact"
    	passed=0
    	failed=0  	 
  
    	for i in range(len(data)):
    	    r =  requests.post(url = url, data = data[i])
    	    if r.status_code == 200:
    	    	passed = passed+1
    	    else:
    	        failed = failed+1
    	    print(r.text)

    	return("Ran %d test,passed %d tests and failed %d tests for validation of email"%(len(data),passed,failed))        	
    	


    def __init__(self):
    	data=[{'name':'abc','email_add':'ads@gmail.com','phone':'324ds'},{'name':'abc','email_add':'adscom','phone':''}]
    	test_email=self.email(data)
    	test_number  = self.number(data)
    	print(test_number)















c = UnitTestClass()