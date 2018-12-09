import sqlite3


#-----------------------------------------------Function to add contact---------------------------------------------------------------------------
def add_contact(lis):
	conn=sqlite3.connect("database/plivo.db")
	cursor=conn.cursor()
	cursor.execute("insert into contact(Name,Email_add,COntact_No) values(?,?,?)",(lis[0],lis[1],lis[2]))
	conn.commit()
	conn.close()
	return("hello") 

#-----------------------------------------------Function to find the contact to be edited---------------------------------------------------------------------------

def edit_contact_page(add):
	conn=sqlite3.connect("database/plivo.db")
	cursor=conn.cursor()
	cursor.execute("select * from contact where Email_add='"+add+"'")
	data=cursor.fetchall()
	conn.close()
	return(data)
	

#-----------------------------------------------Function to edit the details of contact selected---------------------------------------------------------------------------

def edit_contact(lis):
	conn=sqlite3.connect("database/plivo.db")
	cursor=conn.cursor()
	cursor.execute("update contact set Name='"+lis[1]+"',Email_add='"+lis[2]+"',COntact_No='"+lis[3]+"' where id='"+lis[0]+"'")
	conn.commit()
	conn.close()
	return("done")

#-----------------------------------------------Function to delete particular contact ---------------------------------------------------------------------------

def delete_contact(email_add):
	conn=sqlite3.connect("database/plivo.db")
	cursor=conn.cursor()
	cursor.execute("Delete from contact where Email_add='"+email_add+"'")
	conn.commit()
	conn.close()
	return("The record has been deleted successfully")

#-----------------------------------------------Function to get the details from the database---------------------------------------------------------------------------

def get_whole_db():
    conn=sqlite3.connect("database/plivo.db")
    cursor=conn.cursor()
    cursor.execute("select * from contact order by Name COLLATE NOCASE ASC")
    data=cursor.fetchall()
    values=len(data)
    
    return(data)   


def valid_number(num):
    if num.isdigit():
    	return("True")
    else:
        return("False")	
	


#-----------------------------------------------Function for pagination---------------------------------------------------------------------------
    

def pagination(data,n):
	
	last=n*10
	start=last-10
	data1=data[start:last]
	values=len(data)
	final_val=0
	if(values!=0):
	    quo,rem=int(values/10),int(values%10)
	    if(rem!=0):
	    	final_val=quo+1
	    else:
	    	final_val=quo
	return([data1,final_val])    	
   

#-----------------------------------------------Function to return the values to main contact book---------------------------------------------------------------------------
	
def pages(data):
	last=1*10
	start=last-10
	data1=data[start:last]
	values=len(data)

	final_val=0
	if(values!=0):
	    quo,rem=int(values/10),int(values%10)
	    if(rem!=0):
	    	final_val=quo+1
	    else:
	    	final_val=quo
	return([data1,final_val,data])    	
    
#-----------------------------------------------Function to check whether the search string is an email or name---------------------------------------------------------------------------


def get_search_text(string):
	conn=sqlite3.connect("database/plivo.db")
	cursor=conn.cursor()
	data=[]
	if(string.split("-")[0]  == "name"):

		cursor.execute("select * from contact where Name like '%"+string.split("-")[1]+"%' Order By Name ASC")
		data=cursor.fetchall()
		
	elif(string.split("-")[0]  == "email"):
		print(string.split("-")[1])
		cursor.execute("select * from contact where Email_add like '%"+string.split("-")[1]+"%' Order By Name ASC")
		data=cursor.fetchall()
		
	conn.close()
	return(data)

#-----------------------------------------------Function to check if the email is valid---------------------------------------------------------------------------


def valid_email(string):
    
    try:
    	if '@' in string:
    		val1 = string.split('@')[1]
    		val2 = val1.split('.')[1]
    		if '.' in val1 and val2 == 'com':
    			return('email-%s'%string.split('@')[0])
    		else:
    			return('name-%s'%string)
    	else:
    		return('name-%s'%string)        	
    except:
    	return('name-%s'%string)
#-----------------------------------------------Function to process the string queried by the user---------------------------------------------------------------------------


def search_text(string):

    check_valid=valid_email(string)
    string_result = get_search_text(check_valid)
    get_exact_result = pages(string_result)
    
    return(get_exact_result)

#-----------------------------------------------Function to check whther the email already existed---------------------------------------------------------------------------


def check_email_exist(email):
	conn=sqlite3.connect("database/plivo.db")
	cursor=conn.cursor()
	cursor.execute("select * from contact where Email_Add ='"+email+"'")
	data=cursor.fetchall()
	conn.close()
	return(data)


