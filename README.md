# Cloud Computing Path

Creating **RESTful APIs** and deploying to [Google Cloud Platform](https://cloud.google.com)
by using [Google App Engine](https://cloud.google.com/appengine) and [Google Compute Engine](https://cloud.google.com/compute) for communication between **Machine Learning Recommendation System Model** and **Mobile Development**. Using [Cloud Function](https://cloud.google.com/functions) to solve the Travelling Salesman Problem(TSP). Creating database in [Cloud SQL](https://cloud.google.com/sql). 

# RESTful APIs

In making the **RESTful APIs** we use [Python](https://github.com/python) using the [Flask Framework](https://flask.palletsprojects.com/en/2.0.x/) and for responses using **JSON** format. For each URL that can be used will be explained below.

## List Destination

In this section there is a list of all destinations that can be filtered by name, city or place ID. Response from each URL using **JSON** format.

**Base URL :**

> https://getloc-314510.et.r.appspot.com/

**Path :**

> /wisata

**Method :**

> `GET`

- **Show List Destination**
  > https://getloc-314510.et.r.appspot.com/wisata

```json
{
  "category": "Taman Hiburan",
  "city": "Semarang",
  "deskripsi": "Kampoeng Kopi Banaran, sebuah agro wisata perkebunan kopi di Kabupaten Semarang. Tempat wisata ini memiliki luas 462 hektar yang sebagian dijadikan resort dan tempat wisata. Lokasinya berada di Areal Perkebunan Kopi Kebun Getas Afdeling Assinan tepatnya Jl. Raya Semarang ? Solo Km. 35. Lokasi Kampoeng Kopi Banaran yang berada di ketinggian 480 ? 600m dpl membuat suhu udara disana sejuk antara 23?C ? 27?C. Jadi cocok banget buat pelesir mencari udara dingin dan segar dengan pemandangan indah. Menghilangkan penat kesibukan Kota besar, di tengah perkebunan yang asri.",
  "name": "Kampoeng Kopi Banaran",
  "place_id": "ChIJ-9JlAnxwei4R0SmxRv26nXM",
  "price": "200000",
  "rating": "4.3",
  "spend_time": "90"
}
```

<br>

- **Show list destination filtering by place_id**

  > https://getloc-314510.et.r.appspot.com/wisata/{place_id}

  **Required**

  > place_id = [string]

  **Example request**

  > https://getloc-314510.et.r.appspot.com/wisata/ChIJ1RIjvSXmaC4Rn7u8rwSSLPw

```json
{
  "data": [
    {
      "category": "Tempat Ibadah",
      "city": "Bandung",
      "deskripsi": "Masjid Raya Bandung Provinsi Jawa Barat, yang dulu dikenal dengan nama Masjid Agung Bandung adalah masjid yang berada di Kota Bandung, Jawa Barat, Indonesia. Status masjid ini adalah sebagai masjid provinsi bagi Jawa Barat. ",
      "name": "Masjid Raya Bandung",
      "place_id": "ChIJ1RIjvSXmaC4Rn7u8rwSSLPw",
      "price": "0",
      "rating": "4.7",
      "spend_time": ""
    }
  ],
  "message": "success"
}
```

<br>

- **Show list destination search by name**

  > https://getloc-314510.et.r.appspot.com/wisata/search/name?nama={nama}

  **Required**

  > nama = [string]

  **Example request**

  > https://getloc-314510.et.r.appspot.com/wisata/search/name?nama=Borobudur

```json
{
  "data": [
    {
      "category": "Budaya",
      "city": "Yogyakarta",
      "deskripsi": "Borobudur adalah sebuah candi Buddha yang terletak di Borobudur, Magelang, Jawa Tengah, Indonesia. Candi ini terletak kurang lebih 100 km di sebelah barat daya Semarang, 86 km di sebelah barat Surakarta, dan 40 km di sebelah barat laut Yogyakarta.",
      "name": "Candi Borobudur",
      "place_id": "ChIJl9anCfCMei4Ry8NNdDRD0w0",
      "price": "50000",
      "rating": "4.7",
      "spend_time": "120"
    }
  ],
  "message": "success"
}
```

<br>
