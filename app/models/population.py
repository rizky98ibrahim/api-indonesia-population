from app import db
from datetime import datetime

# Table Name
table_name = 'population'

class Population(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama_lengkap = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    telepon = db.Column(db.String(20), nullable=True)
    nik = db.Column(db.String(16), unique=True, nullable=True)
    nomor_kk = db.Column(db.String(16), unique=True, nullable=True)
    tempat_lahir = db.Column(db.String(255), nullable=True)
    tanggal_lahir = db.Column(db.Date, nullable=True)
    agama = db.Column(db.String(255), nullable=True)
    alamat = db.Column(db.Text, nullable=True)
    golongan_darah = db.Column(db.String(2), nullable=True)
    jenis_kelamin = db.Column(db.String(1), nullable=True)
    kewarganegaraan = db.Column(db.String(3), nullable=True)
    pekerjaan = db.Column(db.String(255), nullable=True)
    pendidikan_terakhir = db.Column(db.String(255), nullable=True)
    status_pernikahan = db.Column(db.String(255), nullable=True)
    pasport = db.Column(db.String(8), nullable=True)
    sim = db.Column(db.String(10), nullable=True)
    status = db.Column(db.String(255), default='Aktif')
    created_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.TIMESTAMP, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)


    def to_dict(self):
        return {
            'id': self.id,
            'nik': self.nik,
            'nomor_kk': self.nomor_kk,
            'nama_lengkap': self.nama_lengkap,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'telepon': self.telepon,
            'tempat_lahir': self.tempat_lahir,
            'tanggal_lahir': self.tanggal_lahir.strftime('%Y-%m-%d'),
            'agama': self.agama,
            'alamat': self.alamat,
            'golongan_darah': self.golongan_darah,
            'jenis_kelamin': self.jenis_kelamin,
            'kewarganegaraan': self.kewarganegaraan,
            'pekerjaan': self.pekerjaan,
            'pendidikan_terakhir': self.pendidikan_terakhir,
            'status_pernikahan': self.status_pernikahan,
            'pasport': self.pasport,
            'sim': self.sim,
            'status': self.status,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S') if self.created_at else None,
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S') if self.updated_at else None
        }
        
        return data