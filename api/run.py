import os
from app import app

port = 5000
app.run(debug = True, host = '0.0.0.0', port = port)

# To Run:
# python run.py
# or
# python -m flask run
