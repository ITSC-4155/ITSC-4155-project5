from flask import Blueprint, request, render_template, flash
from deezer import Client

# Initialize the Deezer Client
deezer_client = Client()

# Create a Blueprint for the search functionality
search_blueprint = Blueprint('search', __name__, url_prefix='/search')

@search_blueprint.route('/', methods=['GET'])
def search():
    query = request.args.get('query', '')

    if results is None:
        flash('Please enter a song to search.')
        return render_template('search.html', query=query, results=[])
    if not results:
        flash('No results found. Please check for typos or try different search terms.', 'info')
        return render_template('search.html', query=query, results=[])
    

    results = deezer_client.search(query) 

    
    return render_template('search.html', query=query, results=results)
