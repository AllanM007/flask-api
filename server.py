from flask import Flask, render_template
import connexion
import config

# Create the application instance
connex_app = config.connex_app

# Read the swagger.yml file to configure the endpoints
connex_app.add_api("swagger.yml")

@connex_app.route('/')
def home():
    
    return render_template('home.html')

@connex_app.route('/error')
def error():
	return render_template('errors.html')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    connex_app.run(host='0.0.0.0', port=5000, debug=True)