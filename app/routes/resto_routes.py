from app.routes import resto_bp
from app.controller import resto_controller 
from flask import request

from flask import Blueprint

resto_bp = Blueprint('resto_bp', __name__)


@resto_bp.route('/resto', methods=['GET'])
def restor():
    return resto_controller.index()

@resto_bp.route('/resto/<id>', methods=['GET'])
def restorById(id):
    return resto_controller.listById(id)

@resto_bp.route('/resto/search/place_name', methods=['GET'])
def searchByPlaceName():
    place_name = request.args.get("place_name")
    return resto_controller.searchPlaceName(place_name)



# @resto_bp.route('/resto/search/place_id', methods=['GET'])
# def searchByPlaceId():
#     args = request.args
#     filtered_args = {k: v for k, v in args.items() if v is not None}

#     array = []

#     for i in filtered_args:
#         array.append(" OR place_id = '" + filtered_args[i] + "'")

#     s = str(array)

#     del1 = s.replace('[', '')
#     del2 = del1.replace(']', '')
#     del3 = del2.replace('"', '')
#     result = del3.replace(',', '')

#     return resto_controller.multipleSearchId(result)
