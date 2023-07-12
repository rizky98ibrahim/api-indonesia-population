# API Endpoints

## Get All Population Data

### Request

- Method: GET
- URL: <http://127.0.0.1:5000/api/population>

### Response

```json
{
    "status": "success",
    "message": "Population data retrieved successfully",
    "data": [
        {
            "id": 1,
            "nik": "1234567890123456",
            "nomor_kk": "1234567890123456",
            "nama_lengkap": "Jhon Doe",
            "username": "jhondoe@example.com",
            "email": "jhondoe@example.com",
            "password": "p@sSw0rd",
            "telepon": "08XX-XXXX-XXX",
            "tempat_lahir": "Jakarta",
            "tanggal_lahir": "1998-06-06",
            "agama": "Hindu",
            "alamat": "Komplek ABC, Jl. BCD No.123, Kota Bekasi, Jawa Barat, 17426",
            "golongan_darah": "AB",
            "jenis_kelamin": "L",
            "kewarganegaraan": "WNA",
            "pekerjaan": "Web Developer",
            "pendidikan_terakhir": "S2",
            "status_pernikahan": "Belum Menikah",
            "pasport": "1234567890",
            "sim": null,
            "status": "Aktif",
            "created_at": "2023-05-19 11:31:41",
            "updated_at": "2023-02-06 17:43:05"
        },
        {

        },
        {

        }
    ],
    "limit": 10,
    "current_page": 1,
    "total_pages": 11,
    "links": {
        "next": "http://localhost:5000/api/population?page=2&limit=10",
        "previous": null
    }
}
```

## Get Population Data by ID

### Request

- Method: GET
- URL: <http://127.0.0.1:5000/api/population/{id}>

### Response

```json
{
    "status": "success",
    "message": "Population data retrieved successfully",
    "data": {
        "id": 1,
        "nik": "1234567890123456",
        "nomor_kk": "3481045759733855",
        "nama_lengkap": "Jhon Doe",
        "username": "jhondoe@example.com",
        "email": "jhondoe@example.com",
        "password": "p@sSw0rd",
        "telepon": "08XX-XXXX-XXX",
        "tempat_lahir": "Jakarta",
        "tanggal_lahir": "1998-06-06",
        "agama": "Hindu",
        "alamat": "Komplek ABC, Jl. BCD No.123, Kota Bekasi, Jawa Barat, 17426",
        "golongan_darah": "AB",
        "jenis_kelamin": "L",
        "kewarganegaraan": "WNA",
        "pekerjaan": "Web Developer",
        "pendidikan_terakhir": "S2",
        "status_pernikahan": "Belum Menikah",
        "pasport": "42368962",
        "sim": null,
        "status": "Aktif",
        "created_at": "2023-05-19 11:31:41",
        "updated_at": "2023-02-06 17:43:05"
    }
}
```

## Create New Population Data

### Request

- Method: POST
- URL: <http://127.0.0.1:5000/api/population>
- Body:

  ```json
  {
    "nama_lengkap": "Jhon Doe",
    "username": "jhondoe@example.com",
    "email": "jhondoe@example.com",
    "password": "p@sSw0rd"
  }
  ```

### Response

```json
{
    "status": "success",
    "message": "Population data created successfully",
    "data": {
        "id": 2,
        "nama_lengkap": "Jhon Doe",
        "username": "jhondoe@example.com",
        "email": "jhondoe@example.com",
        "password": "p@sSw0rd",
        "status": "Aktif",
        "created_at": "2023-07-12 16:46:37",
        "updated_at": "2023-07-12 16:46:37"
    }
}
```

## Update Population Data by ID

### Request

- Method: PUT
- URL: <http://127.0.0.1:5000/api/population/{id}>
- Body:

  ```json
  {
      "nik": "1234567890123456",
      "nomor_kk": "3481045759733855",
      "nama_lengkap": "Jhon Doe",
      "username": "jhondoe@example.com",
      "email": "jhondoe@example.com",
      "password": "p@sSw0rd",
      "telepon": "08XX-XXXX-XXX",
      "tempat_lahir": "Jakarta",
      "tanggal_lahir": "1998-06-06",
      "agama": "Hindu",
      "alamat": "Komplek ABC, Jl. BCD No.123, Kota Bekasi, Jawa Barat, 17426",
      "golongan_darah": "AB",
      "jenis_kelamin": "L",
      "kewarganegaraan": "WNA",
      "pekerjaan": "Web Developer",
      "pendidikan_terakhir": "S2",
      "status_pernikahan": "Belum Menikah",
      "pasport": "42368962",
      "sim": null,
  }

  ```

### Response

```json
{
    "status": "success",
    "message": "Population data updated successfully",
    "data": {
        "id": 2,
        "nik": "1234567890123456",
        "nomor_kk": "3481045759733855",
        "nama_lengkap": "Jhon Doe",
        "username": "jhondoe@example.com",
        "email": "jhondoe@example.com",
        "password": "p@sSw0rd",
        "telepon": "08XX-XXXX-XXX",
        "tempat_lahir": "Jakarta",
        "tanggal_lahir": "1998-06-06",
        "agama": "Hindu",
        "alamat": "Komplek ABC, Jl. BCD No.123, Kota Bekasi, Jawa Barat, 17426",
        "golongan_darah": "AB",
        "jenis_kelamin": "L",
        "kewarganegaraan": "WNA",
        "pekerjaan": "Web Developer",
        "pendidikan_terakhir": "S2",
        "status_pernikahan": "Belum Menikah",
        "pasport": "42368962",
        "sim": null,
        "created_at": "2023-07-12 16:46:37",
        "updated_at": "2023-07-12 16:48:20"
    }
}
```

## Delete Population Data by ID

### Request

- Method: DELETE
- URL: <http://127.0.0.1:5000/api/population/{id}>

### Response

```json
{
    "status": "success",
    "message": "Population data deleted successfully",
    "data": null
}
```
