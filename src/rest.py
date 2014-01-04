import json

from bottle import route, run, request, abort
from pymongo import Connection



connection = Connection('mongodb://oscar:s0304484@54.209.153.250', 27017)
db = connection.mydatabase


@route('/documents', method='PUT')
def put_document():
    data = request.body.readline()
    print(data)
    if not data:
        abort(400, 'No data received')
    entity = json.loads(data)
    if not entity.has_key('_id'):
        abort(400, 'No _id specified')
    try:
        db.documents.insert(entity)
    except ValidationError as ve:
        abort(400, str(ve))


@route('/documents/<_id>', method='GET')
def get_document(_id):
    entity = db.documents.find_one({'_id': _id})
    if not entity:
        abort(404, 'No document with id %s' % _id)
    return entity

run(host='localhost', port=8080)