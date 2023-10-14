import datetime
# Import the os package, used to set env variables and check paths
import os
# import the dotenv package for client keys in .env file
from dotenv import load_dotenv


# for random UUID keys
# https://docs.python.org/3/library/uuid.html
import uuid
# Import square 
from square.client import Client

# import pandas so we can create a table to
# display JSON results from SQ
import pandas as pd

# for JSON
import json


from flask import Flask, render_template



# Get the current working directory
cwd = os.getcwd()

# Construct the .env file path
env_path = os.path.join(cwd, '.env')

# Load the .env file
load_dotenv(dotenv_path=env_path)





app = Flask(__name__)




@app.route("/")
def root():




    # SQUARE API
    # init the square API
    # using generic os environment this fails.
    # However, when using the dotenv package it works
    sq_client = Client(
        access_token=os.environ['SQUARE_ACCESS_TOKEN'],
        environment='production'  
    )

    result = sq_client.invoices.list_invoices(
        location_id = "LZBNSDTSHAMM8"
    )

    if result.is_success():
        print(result.body)
    elif result.is_error():
        print(result.errors)

    result_txt = result.body




    # read our JSON result into a pandas dataframe
    aDF = pd.DataFrame(result.body)

    # Flatten business data into a dataframe, replace separator
    invoices_DF = pd.json_normalize(result.body['invoices'])
    # Just show three columns
    table = invoices_DF[['id', 'order_id', 'invoice_number']].to_html(index=False)
    
    return render_template("index.html", mytable=table)



if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host="127.0.0.1", port=8080, debug=True)
    