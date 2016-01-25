from flask import Flask, abort, request

app = Flask(__name__)

# Index view to the main URL
@app.route('/')
def index():
    return ('<h3>Hello world with Flask framework!!</h3>')

# View to send an specific name to be displayed on browser
@app.route('/hello/<name>')
@app.route('/hello/')
def hello(name=None):
    if name is None:
        # If no name is specified, it tries to obtain
        # from the URL string
        name = request.args.get('name')
        if name:
            return ('Hello ' + name)
        else:
            return ('Any name was found')

    else:
        # No name was specified in the URL or the query string
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
