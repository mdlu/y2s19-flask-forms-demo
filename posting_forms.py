from flask import Flask, request, render_template
from databases import add_survey_info, get_all_survey_info

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        # Make some variables so we type less later
        firstname = request.form['firstname']
        animalvote = request.form['animal']

        # Save form information to database
        add_survey_info(firstname, animalvote)

        # Display response
        return render_template('response.html',
               n=firstname,
               s=animalvote)

@app.route('/results')
def all_results():
    all_info = get_all_survey_info()
    return render_template('all.html', all_responses=all_info)

app.run(debug=True)
