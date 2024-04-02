from flask import Blueprint, request, render_template

search_blueprint = Blueprint('search', __name__,template_folder="templates", )

@search_blueprint.route('/', methods=['GET'])  
def search():
    query = request.args.get('query', '')
    results = Song.query.filter(Song.title.ilike(f"%{query}%")).all()
    return render_template('search.html', query=query, results=results)
