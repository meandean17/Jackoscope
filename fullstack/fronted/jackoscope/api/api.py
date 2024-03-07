from flask import Flask, Response
import CardDetector as cd
import json

app = Flask(__name__)

# cd.detectCards()

from flask import Flask, Response
import json

app = Flask(__name__)

@app.route('/api/detect')
def get_json():
    try:
        # Open the JSON file in read mode
        with open('cards.json', 'r') as json_file:
            # Read the contents of the file
            json_data = json_file.read()
        # Return the JSON data as a response
        return Response(json_data, mimetype='application/json')
    except FileNotFoundError:
        # Return a 404 error if the file does not exist
        return "File not found", 404
    except Exception as e:
        # Return an error message for other exceptions
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)

