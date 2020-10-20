from flask import Blueprint, jsonify
from flask_restplus import Api, Resource, reqparse

api_v0_blueprint = Blueprint('api', __name__)
api = Api(api_v0_blueprint, doc='/', version='v0')

@api.route('/test')
class Test(Resource):
    def get(self):
        message = {'service': 'processor', 'api_version': 'v0_test'}
        return jsonify(message)


process_parser = reqparse.RequestParser()
process_parser.add_argument('image_data', type=str)
process_parser.add_argument('image_type', type=str)

@api.route('/process')
@api.doc(params={
    'image_type': 'the mime type of the image "image/jpeg" or "image/png"',
    'image_data': 'The data of the image in base64 format'})
class process(Resource):
    @api.expect(process_parser)
    def post(self):
        args = process_parser.parse_args()
        image = args['image_data']
        print(f'Payload: {image}')
        message = {'payload': '12345'}
        return jsonify(message)
