from flask import jsonify, request, render_template, Blueprint

from request_handler import RequestHandler

view = Blueprint('view', __name__, url_prefix='')


@view.route('/')
def splash_page():
    return 'hii'


@view.route('/timeout-check')
def timeout_check():
    return jsonify({'STATUS': 'AVAILABLE'})


@view.route('/runScript', methods=['POST'])
def run_scripts():
    try:
        return jsonify(RequestHandler.process_request(request))
    except Exception as e:
        return jsonify({'ERROR': str(e)})
