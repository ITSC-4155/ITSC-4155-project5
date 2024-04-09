from flask import Blueprint, request, render_template

playlist_blueprint = Blueprint('search', __name__)


@playlist_blueprint("/playlists")
def show_all_playlists():
    """Return a list of playlists."""

    playlists = Playlist.query.all()
    return render_template("playlists.html", playlists=playlists)


@playlist_blueprint("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    """Show detail on specific playlist."""

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
    playlist = Playlist.query.get_or_404(playlist_id)
    return render_template("playlist.html", playlist=playlist)


@playlist_blueprint("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    """Handle add-playlist form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-playlists
    """

    # # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
    # form = PlaylistForm()
    # if form.validate_on_submit():
    #     name = form.name.data
    #     description = form.description.data

    #     new_playlist = Playlist(name=name, description=description)
    #     db.session.add(new_playlist)
    #     db.session.commit()
    #     return redirect("/playlists")

    # return render_template("new_playlist.html", form=form)
