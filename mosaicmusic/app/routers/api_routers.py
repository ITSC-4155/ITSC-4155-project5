
from flask import (
    Blueprint, flash, redirect, render_template, request
)
import deezer

client = deezer.Client(app_id='foo', app_secret='bar')

api_pages = Blueprint('api', __name__, template_folder="templates", url_prefix='/api')


# These routers will be used for viewing and managing  Api - specific information


## Get an album page by ID
@api_pages.get('/album/<int:id>')
def showAlbum(id):

    album = client.get_album(id)
    return render_template('album.html', album=album)