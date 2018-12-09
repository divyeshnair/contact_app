from flask import Flask, render_template,request,url_for,redirect
import sqlite3
from flask_httpauth import HTTPBasicAuth
from scripts import Modules
from flask_caching import Cache


app=Flask(__name__)
auth = HTTPBasicAuth()
cache = Cache(app, config={'CACHE_TYPE': 'redis'})




users = {
    "admin": "plivo",
    "john": "plivo"
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


search_data=[]
main_data=[]


@app.route('/add_contact_page' , methods=['GET'])
@auth.login_required

def add_contact_page():
    
    return render_template('add_contact.html')



@app.route('/add_contact' , methods=['POST'])
def add_contact():

    name = request.form['name']
    email = request.form['email_add']
    phone = request.form['phone']

    if not name or not email or not phone:
        var="Please fill all the blanks"
        return render_template("add_contact.html",msg= var)
    
    else:
        check_email = Modules.check_email_exist(email)
        check_number = Modules.valid_number(phone)
        valid_email = Modules.valid_email(email)
        if check_email:
            var="Email_address already exists"
            return render_template("add_contact.html",msg= var)
        elif(check_number == "False"):
            var="Please make sure the contact has only numbers in it"
            return render_template("add_contact.html",msg= var)
        elif(valid_email.split("-")[0] == "name"):
            var="Not a valid email address"
            return render_template("add_contact.html",msg= var)
        
        else:    
            data = Modules.add_contact([name,email,phone])
            return redirect(url_for('home_page'))

        
            
  

@app.route('/delete_contact',methods=['POST'])
@auth.login_required
def delete_page():
    email_add = request.form['val1']
    data = Modules.delete_contact(email_add)
    return redirect(url_for('home_page'))
    


@app.route('/edit_contact_page',methods=['GET'])
def edit_page_page():

    param = request.args.get('add')
    data = Modules.edit_contact_page(param)

    return render_template('edit_contact.html',people=data,val=data[0][0])




@app.route('/edit_contact',methods=['POST'])
def edit_page():

    id_no = request.form['id']
    name = request.form['name']
    email = request.form['email_add']
    phone = request.form['phone']
    data = Modules.edit_contact([id_no,name,email,phone])
        
    return redirect(url_for('home_page'))
        



@app.route('/search_it',methods=['POST'])
@cache.cached(timeout=2)
def result():
    

    global search_data
 
    search_text=request.form["search_val"]
    if not search_text: 
        return redirect(url_for('home_page'))
    
    else:
        data = Modules.search_text(search_text)
        search_data = data[2]
        pages=data[1]
        people=data[0]
        
        return render_template("search_results.html",people=people,pages=pages)

@app.route('/change_page_search',methods=['POST'])
def result1():
    global search_data
    var1=int(request.form['val1'])
    change_data = Modules.pagination(search_data,var1)
    data1=change_data[0]
    pages=change_data[1]    
    return render_template("search_results.html",people=data1,pages=pages)

    
@app.route('/')
@auth.login_required
@cache.cached(timeout=2)
def home_page():

    global main_data
 
    full_data=Modules.get_whole_db()
    data=Modules.pages(full_data)
    main_data= data[2]
    pages=data[1]
    people=data[0]
    
    return render_template('contact_page.html',people=people,pages=pages)




@app.route('/change_page_contact',methods=['POST'])
def result2():
  
    global main_data
        
    var1=int(request.form['val1'])
    change_data = Modules.pagination(main_data,var1)
    data1=change_data[0]
    pages=change_data[1]    
    return render_template("contact_page.html",people=data1,pages=pages)





app.debug=True

app.run(host="0.0.0.0",threaded=True)




