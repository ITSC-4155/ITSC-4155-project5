from flask import (
    Blueprint, g, render_template
)
from ..managers.playlist_manager import playlist_manager_class

playlist_blueprint = Blueprint('playlist', __name__, template_folder="templates", url_prefix='/playlists')

@playlist_blueprint.route('/all')
def show_all_playlists():
    if not g.current_user.is_authenticated:
        # Redirect to login or handle it appropriately if user is not authenticated
        pass
    playlists = playlist_manager_class.get_playlists_by_user(g.current_user.id)
    return render_template('playlist.html', playlists=playlists)

@playlist_blueprint.app_context_processor
def inject_user_playlists():
    if hasattr(g, 'current_user') and g.current_user.is_authenticated:
        user_playlists = playlist_manager_class.get_playlists_by_user(g.current_user.id)
        return {'user_playlists': user_playlists}
    return {'user_playlists': []}



# @playlist_blueprint.route("/playlists/<int:playlist_id>")
# def show_playlist(playlist_id):
#     # Show detail on specific playlist.#

#     # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
#     playlist = Playlist.query.get_or_404(playlist_id)
#     return render_template("playlist.html", playlist=playlist)


# @playlist_blueprint.route("/playlists/add", methods=["GET", "POST"])
# def add_playlist():
#     """Handle add-playlist form:

#     - if form not filled out or invalid: show form
#     - if valid: add playlist to SQLA and redirect to list-of-playlists
#     """

#     # # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
#     # form = PlaylistForm()
#     # if form.validate_on_submit():
#     #     name = form.name.data
#     #     description = form.description.data

#     #     new_playlist = Playlist(name=name, description=description)
#     #     db.session.add(new_playlist)
#     #     db.session.commit()
#     #     return redirect("/playlists")

#     # return render_template("new_playlist.html", form=form)
