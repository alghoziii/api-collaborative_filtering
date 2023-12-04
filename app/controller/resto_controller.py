from app import db
from app.model.resto import Resto
from app import response


def index():
    try:
        resto = Resto.query.all()
        data = formatarray(resto)
        return response.success(data, "success")
    except Exception as e:
        print(e)
        return response.error("Internal Server Error", 500)

def listById(id):
    try:
        resto = db.session.query(Resto).filter_by(Place_Id=id)
        data = formatarray(resto)
        return response.success(data, "success")
    except Exception as e:
        print(e)

# Add other functions...
def searchPlaceName(place_name):
    param = f"%{place_name}%"
    try:
        resto = Resto.query.filter(Resto.Place_Name.like(param)).all()
        data = formatarray(resto)
        return response.success(data, "success")
    except Exception as e:
        print(e)



def formatarray(datas=[]):
    array = []

    for i in datas:
        array.append(singleObject(i))

    return array

def singleObject(data):
    data = {
        'Place_Id': data.Place_Id,
        'Place_Name': data.Place_Name,
        'Culinary_Ratings': data.Culinary_Ratings,
        'Category': data.Category,
        'Address': data.Address,
        'Description': data.Description,
        'Coordinate': data.Coordinate,
        'Lat': data.Lat,
        'Long': data.Long,
      
    }

    return data
