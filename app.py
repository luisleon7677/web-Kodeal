from flask import Flask, render_template

app = Flask(__name__,template_folder='.')

@app.route('/')
def home():
    return render_template('/templates/home.html')

@app.route('/about')
def about():
    return render_template('templates/about.html')

@app.route('/services')
def services():
    return render_template('templates/services.html')


        


if __name__ == '__main__':
    app.run(debug=True)
