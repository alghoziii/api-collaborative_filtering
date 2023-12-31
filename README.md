# Cloud Computing Path

blablaaa

# RESTful APIs

In making the **RESTful APIs** we use [Python](https://github.com/python) using the [Flask Framework](https://flask.palletsprojects.com/en/2.0.x/) and for responses using **JSON** format. For each URL that can be used will be explained below.

## List Destination

In this section there is a list of all destinations that can be filtered by name, city or place ID. Response from each URL using **JSON** format.

**Base URL :**

> http://localhost:5000

**Path :**

> /resto

**Method :**

> `GET`

- **Show List Destination**
  > http://localhost:5000/resto

```json
{
    "data": [
        {
            "Address": "Cicendo, Kota Bandung",
            "Category": "Seafood",
            "Coordinate": "{'lat': -6.907839576390254, 'lng':107.596398032071",
            "Culinary_Ratings": "4.5",
            "Description": "Menyajikan menu buffet dengan hidangan seafood, sushi, sop buntut dan pilihan menu internasional lainnya.",
            "Lat": "-6.907839576",
            "Long": "107.596398",
            "Place_Id": "1",
            "Place_Name": "Purnawarman Restaurant"
        },
}
```

<br>

- **Show list destination filtering by place_id**
  > http://localhost:5000/resto/place_id

  > place_id = [string]

  **Example request**

  > http://localhost:5000/resto/10

```json
{
    "data": [
        {
            "Address": "Cimenyan, Kabupaten Bandung",
            "Category": "Western",
            "Coordinate": "}'lat':-6.859342816769343, 'lng':107.6281670716133",
            "Culinary_Ratings": "4.4",
            "Description": "Restoran kasual terbuka yang menyajikan masakan internasional di bangunan bertingkat tiga & berpanorama indah.",
            "Lat": "-6.859342817",
            "Long": "107.6281671",
            "Place_Id": "10",
            "Place_Name": "The Stone Cafe"
        }
    ],
    "message": "success"
}
```

<br>

- **Show list destination search by place_name**

  > http://localhost:5000/resto/search/place_name

  **Required**

  > place_nama = [string]

  **Example request**

  > http://localhost:5000/resto/search/place_name?place_name=The Stone Cafe

```json
{
    "data": [
        {
            "Address": "Cimenyan, Kabupaten Bandung",
            "Category": "Western",
            "Coordinate": "}'lat':-6.859342816769343, 'lng':107.6281670716133",
            "Culinary_Ratings": "4.4",
            "Description": "Restoran kasual terbuka yang menyajikan masakan internasional di bangunan bertingkat tiga & berpanorama indah.",
            "Lat": "-6.859342817",
            "Long": "107.6281671",
            "Place_Id": "10",
            "Place_Name": "The Stone Cafe"
        }
    ],
    "message": "success"
}
```

<br>
