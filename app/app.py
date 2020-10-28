from flask import Flask, request
from waitress import serve
import sys
import optparse
import os

app = Flask(__name__)


@app.route("/")
def calculate_exponential():
    # Get all query parameters required to generate keywords
    number = request.args.get('number')

    # Validate if all required parameters are provided
    if not number:
        return {"ValidationError": {"number": "required"}}, 422

    # Attempt to get the keywords, throw exception in case things break
    try:
        return f"the exponential of {number} equals: {int(number)**4}"
    except Exception as ExceptionError:
        return {"ExceptionThrown": str(ExceptionError)}, 500


if __name__ == '__main__':

    # Run Flask or Waitress web-server
    parser = optparse.OptionParser(usage="python run.py -p ")
    parser.add_option('-p', '--port', action='store', dest='port', help='The port to listen on.')
    parser.add_option('-d', '--dev', action='store_true', dest='dev', help='Run Flask built-in server.')
    (args, _) = parser.parse_args()

    port = os.getenv("PORT", args.port)
    dev = os.getenv("DEV", args.dev)

    if port == None:
        print("Missing required argument: -p/--port")
        sys.exit(1)

    if dev:
        app.run(host='0.0.0.0', port=int(port), debug=True)
    else:
        serve(app, host='0.0.0.0', port=int(port))
