import pathlib
import os
from dotenv import load_dotenv
from Airtable import AirTable
from flask import (Flask,
                   render_template,
                   request,
                   redirect)

TEMPLATES_DIR = pathlib.Path('templates/')
TEMPLATES_DIR.mkdir(parents=True, exist_ok=True)

STATIC_DIR = pathlib.Path('static/')
STATIC_DIR.mkdir(parents=True, exist_ok=True)
STATIC_DIR = str(STATIC_DIR)

app = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)

load_dotenv()

AIRTABLE_BASE_ID    = os.environ.get("AIRTABLE_BASE_ID")
AIRTABLE_API_KEY    = os.environ.get('AIRTABLE_API_KEY')
AIRTABLE_TABLE_NAME = os.environ.get('AIRTABLE_TABLE_NAME')

@app.route('/', methods=['GET', 'POST'])
def home_view():
    did_send = None
    if request.method == 'POST':
        email = request.form['email']
        airtable_client = AirTable(
            base_id= AIRTABLE_BASE_ID,
            api_key= AIRTABLE_API_KEY,
            table_name= AIRTABLE_TABLE_NAME
            )
        did_send = airtable_client.create_records(email=email)
        if did_send in range(200, 300):
            # print(f'did send {did_send}')
            return redirect('/success/')
            did_send = True
            # return redirect('/#footer/')
        else:
            # return redirect('/error/')
            did_send = False
    return render_template('index.html', did_send = did_send)

@app.route('/success/')
def success_view():
    return render_template('success.html')

@app.route('/<error>/')
def error_view(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)