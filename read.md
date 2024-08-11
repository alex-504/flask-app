# Flask Greeting App

This is a simple web application built with Flask, a Python web framework. The application has two main routes:

1. **Home route ("/")**: This route displays a form where users can enter their name. If a name is entered and the form is submitted, the user is redirected to the greet route. If the form is submitted with an empty name field, a message is displayed indicating that the name cannot be empty, along with a button to return to the home page.

2. **Greet route ("/greet/")**: This route displays a personalized greeting to the user based on the name entered in the form on the home page. It also includes a button to return to the home page.

This application demonstrates basic usage of Flask, including defining routes, handling GET and POST requests, using the request object to access form data, and using the redirect and url_for functions to redirect users to different routes.

3.**Next ("New features")**
As I explore the Flask doc, I will be adding more features, and perhaps use this app to learn deployment and orchestration tools"

-------------
-------------

# Flask Greeting App

This is a simple web application built with Flask, a Python web framework. The application has two main routes:

1. **Home route ("/")**: This route displays a form where users can enter their name. If a name is entered and the form is submitted, the user is redirected to the greet route. If the form is submitted with an empty name field, a message is displayed indicating that the name cannot be empty, along with a button to return to the home page.

2. **Greet route ("/greet/")**: This route displays a personalized greeting to the user based on the name entered in the form on the home page. It also includes a button to return to the home page.


This application demonstrates basic usage of Flask, including defining routes, handling GET and POST requests, using the request object to access form data, and using the redirect and url_for functions to redirect users to different routes.

3. **Next ("New features")**
As I explore the Flask doc, I will be adding more features, and perhaps use this app to learn deployment and orchestration tools"

4. **April, 14**
Add CRUD methods.


5. **Running app:**
- Create the environment: 
  ```
  $ mkdir myproject
  $ cd myproject
  $ python3 -m venv .venv
  ```
- Activate the Environment:
```
  $ . .venv/bin/activate
```
- Install Flask in the Environment:
```
  $ pip install Flask
```
- Run the app:
```
  $ flask --app hello run
  * Serving Flask app 'hello'
  * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```
