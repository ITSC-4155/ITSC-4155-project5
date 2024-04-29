from flask import Blueprint, request, render_template, flash, redirect
from deezer import Client

# Initialize the Deezer Client
deezer_client = Client()

# Create a Blueprint for the search functionality
search_blueprint = Blueprint('search', __name__, url_prefix='/search')

@search_blueprint.route('/', methods=['GET'])
def search():
    query = request.args.get('query', '')


    if query != '':
        results = deezer_client.search(query) 
        return render_template('search.html', query=query, results=results)
    
    else:    
        flash('No results found. Please check for typos or try different search terms.', 'info')
        return redirect('/')


