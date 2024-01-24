from flask import Flask, render_template, request

app = Flask(__name__)

# This is a dummy data set for demonstration purposes
data = [
    {"name": "Item 1", "description": "Description of Item 1"},
    {"name": "Item 2", "description": "Description of Item 2"},
    # Add more items as needed
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if query:
        results = [item for item in data if query.lower() in item['name'].lower()]
    else:
        results = []
    return render_template('search_results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)