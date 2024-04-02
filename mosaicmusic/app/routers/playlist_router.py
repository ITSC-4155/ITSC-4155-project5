from flask import (
    Blueprint, flash, redirect, render_template, request
)

playlist_pages = Blueprint('auth', __name__, template_folder="templates", url_prefix='/playlist')