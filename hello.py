from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        user = request.form['name']
        if user != '':
            return redirect(url_for('greet', name=user))
        else:
            return f'''
            <p>Name cannot be empty!</p><br>
            <form action="/">
            <input type="submit" value="Go Home">
        </form>
        '''
            
    return '''
        <form method="POST">
            Name: <input type="text" name="name"><br>
            <input type="submit" value="Submit"><br>
        </form>
    '''

@app.route("/greet/<name>")
def greet(name):
    return f'''
        <p>Hello, {name}!</p>
        <form action="/">
            <input type="submit" value="Go Home">
        </form>
    '''