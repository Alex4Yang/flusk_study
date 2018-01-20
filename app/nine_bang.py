from flask import render_template

from . import routes


@routes.route('/entryticket')
def entry_ticket():
    return render_template('entryticket.html')
