# form
from flask import Flask, request, redirect




app = Flask(__name__)
app.config['DEBUG']=True

form="""
<!DOCTYPE html>
<html>
    <head>
        <style>
            .error {{
                color: red;
            }}
        </style>
    </head>
    <body>
    <h1>Signup</h1>
        <form method="post">
            <label>Username
                    <input name="username" type="text" value="{username_valid}">
                    </label>
                    <p class="error">{invalid}</p>    
                    
                
                
                    <label>Password
                
                        <input name="password" type="password">
                        </label>
                        <p class="error">{invalid_password}</p>
                    
                    <label>Verify Password
                    
                        <input name="verify" type="password">
                        </label>
                        <p class="error">{no_match}</p>
                    
                    <label> Email (optional)
                    
                        <input name="email" value="{entered_email}">
                        </label>
                        <p  class="error">{email_error}</p>
                    
            <input type="submit">
        </form>

        
        
    </body>
</html> 


"""

@app.route("/")
def index():
    return form.format(username_valid='', invalid='', invalid_password= '', entered_email='', email_error='', no_match='')


@app.route("/", methods=['POST'])
def enter_username():
    need_username= request.form['username']
    init_password= request.form['password']    
    verify_password= request.form['verify']
    what_email= request.form['email']
    
    #username verification
    if len(need_username) == 0:
        return form.format(username_valid= need_username, invalid="Please enter a username", invalid_password = "", entered_email= what_email, email_error='', no_match='')
    elif ' ' in need_username:
        return form.format(username_valid= need_username, invalid="Please try again without a space", invalid_password ="", entered_email= what_email, email_error='', no_match='')    
    elif len(need_username) > 20:
        return form.format(username_valid= need_username, invalid="That password is too long", invalid_password ="", entered_email=  what_email, email_error='', no_match='')
    elif len(need_username) < 4:
        return form.format(username_valid= need_username, invalid="That password is too short", invalid_password ="", entered_email= what_email, email_error='', no_match='')
    
    #password verification
    if ' ' in init_password:
        return form.format( invalid_password = "Please try again without a space", username_valid=need_username, invalid="", entered_email=what_email, email_error='', no_match='')
    elif len(init_password)==0:      
        return form.format( invalid_password ="Please enter a password", username_valid=need_username, invalid="", entered_email= what_email, email_error='', no_match='')  
    elif len(init_password) > 20:
        return form.format( invalid_password ="That password is too long", username_valid=need_username, invalid="", entered_email=what_email, email_error='', no_match='')
    elif len(init_password) < 4:
        return form.format( invalid_password ="That password is too short", username_valid=need_username, invalid="", entered_email=what_email, email_error='', no_match='')
    #password and confirm password are same
    if verify_password != init_password:
        return form.format( invalid_password ="", username_valid=need_username, invalid="", entered_email=what_email, email_error='', no_match="Passwords do not match" )
        
    #email verification
    symbol=0

    for i in what_email:
        if i == "@":
            symbol +=1
    if symbol==0 and len(what_email)>0:
        return form.format(invalid_password = " ", username_valid=need_username, invalid="", entered_email=what_email, email_error="That is not a valid email", no_match='')
    
    else:
        return (signup.html)


        


    




        

    
        


    
    






app.run()






#The user's password and password-confirmation do not match.
#The user provides an email, but it's not a valid email. Note: the email field may be left empty, but if there is content in it, then it must be validated. The criteria for a valid email address in this assignment are that it has a single @, a single ., contains no spaces, and is between 3 and 20 characters long.
#Each feedback message should be next to the field that it refers to.

#For the username and email fields, you should preserve what the user typed, so they don't have to retype it. With the password fields, you should clear them, for security reasons.

#If all the input is valid, then you should show the user a welcome page that uses the username input to display a welcome message of: "Welcome, [username]!"

#Use templates (one for the index/home page and one for the welcome page) to render the HTML for your web app.