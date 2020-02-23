import os
import sys

# add app to system path
parent_directory = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(parent_directory)
sys.path.append(os.getcwd())

from app.server import create_app

app = create_app()

app.run(debug=True, threaded=True, host='127.0.0.1', port=5000)
