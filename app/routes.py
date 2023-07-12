from flask import Blueprint, json, request, jsonify
from app import db
from math import ceil
from datetime import datetime
from app.models.population import Population

bp = Blueprint("api", __name__, url_prefix="/api")

@bp.route("/population", methods=["GET"])
def get_population():
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    offset = (page - 1) * limit

    populations = Population.query.offset(offset).limit(limit).all()
    total_count = Population.query.count()
    total_pages = ceil(total_count / limit)

    data = []
    for population in populations:
        data.append(population.to_dict())

    response = {
        'status': 'success',
        'message': 'Population data retrieved successfully',
        'data': data,
        'limit': limit,
        'current_page': page,
        'total_pages': total_pages,
        'links': {
            'next': f'http://localhost:5000/api/population?page={page + 1}&limit={limit}' if page < total_pages else None,
            'previous': f'http://localhost:5000/api/population?page={page - 1}&limit={limit}' if page > 1 else None
        }
    }
    if len(data) > 0:
        return json.dumps(response, sort_keys=False), 200, {'Content-Type': 'application/json'}
    else:
        response['status'] = 'failure'
        response['message'] = 'No population data found'
        return json.dumps(response, sort_keys=False), 404, {'Content-Type': 'application/json'}

@bp.route("/population/<int:id>", methods=["GET"])
def get_population_by_id(id):
    population = Population.query.get(id)
    if population:
        response = {
           'status': 'success',
           'message': 'Population data retrieved successfully',
           'data' : population.to_dict()
        }
        return json.dumps(response, sort_keys=False), 200, {'Content-Type': 'application/json'}
    else:
        response = {
            'status': 'failure',
            'message': 'Population data not found'
        }
        return json.dumps(response, sort_keys=False), 404, {'Content-Type': 'application/json'}


# POST /api/population
@bp.route("/population", methods=["POST"])
def create_population():
    data = request.get_json()
    population = Population(**data)
    db.session.add(population)
    db.session.commit()
    response = {
        'status': 'success',
        'message': 'Population data created successfully',
        'data': population.to_dict()
    }
    return json.dumps(response, sort_keys=False), 201, {'Content-Type': 'application/json'}

# PUT /api/population/<id>
@bp.route("/population/<int:id>", methods=["PUT"])
def update_population(id):
    data = request.get_json()
    population = Population.query.get(id)
    if population:
        population.nama_lengkap = data['nama_lengkap']
        population.username = data['username']
        population.email = data['email']
        population.password = data['password']
        population.telepon = data['telepon']
        population.nik = data['nik']
        population.nomor_kk = data['nomor_kk']
        population.tempat_lahir = data['tempat_lahir']
        population.tanggal_lahir = datetime.strptime(data['tanggal_lahir'], '%Y-%m-%d').date()
        population.agama = data['agama']
        population.alamat = data['alamat']
        population.golongan_darah = data['golongan_darah']
        population.jenis_kelamin = data['jenis_kelamin']
        population.kewarganegaraan = data['kewarganegaraan']
        population.pekerjaan = data['pekerjaan']
        population.pendidikan_terakhir = data['pendidikan_terakhir']
        population.status_pernikahan = data['status_pernikahan']
        population.pasport = data['pasport']
        population.sim = data['sim']
        population.updated_at = datetime.utcnow()
        db.session.commit()
        response = {
            'status': 'success',
            'message': 'Population data updated successfully',
            'data': population.to_dict()
        }
        return json.dumps(response, sort_keys=False), 200, {'Content-Type': 'application/json'}
    else:
        response = {
            'status': 'failure',
            'message': 'Population data not found'
        }
        return json.dumps(response, sort_keys=False), 404, {'Content-Type': 'application/json'}

@bp.route("/population/<int:id>", methods=["DELETE"])
def delete_population(id):
    population = Population.query.get(id)
    if population:
        db.session.delete(population)
        db.session.commit()
        response = {
            'status': 'success',
            'message': 'Population data deleted successfully'
        }
        return json.dumps(response, sort_keys=False), 200, {'Content-Type': 'application/json'}
    else:
        response = {
            'status': 'failure',
            'message': 'Population data not found'
        }
        return json.dumps(response, sort_keys=False), 404, {'Content-Type': 'application/json'}
