from faker import Faker
from app import create_app, db
from app.models.population import Population

def seed_data(num_records):
    app = create_app()
    with app.app_context():
        for _ in range(num_records):
            fake = Faker('id_ID')
            population = Population(
                nama_lengkap=fake.name(),
                username=fake.user_name(),
                email=f"{fake.user_name()}@gmail.com",
                password=fake.password(),
                nik=fake.unique.random_number(digits=16),
                nomor_kk=fake.unique.random_number(digits=16),
                telepon=f"08{fake.random_int(min=10, max=99)}-{fake.random_int(min=1000, max=9999)}-{fake.random_int(min=1000, max=9999)}",
                tempat_lahir=fake.city(),
                tanggal_lahir=fake.date_of_birth(minimum_age=17, maximum_age=45).strftime('%Y-%m-%d'),
                agama=fake.random_element(elements=('Islam', 'Kristen', 'Katolik', 'Hindu', 'Buddha', 'Konghucu')),
                alamat=fake.address(),
                golongan_darah=fake.random_element(elements=('A', 'B', 'AB', 'O')),
                jenis_kelamin=fake.random_element(elements=('L', 'P')),
                kewarganegaraan=fake.random_element(elements=('Indonesia', 'Asing')),
                pekerjaan=fake.job(),
                pendidikan_terakhir=fake.random_element(elements=('SD', 'SMP', 'SMA', 'D3', 'S1', 'S2', 'S3')),
                status_pernikahan=fake.random_element(elements=('Belum Menikah', 'Menikah', 'Cerai', 'Cerai Mati')),
                pasport=fake.random_element(elements=(None, fake.unique.random_number(digits=8))),
                sim=fake.random_element(elements=(None, fake.random_number(digits=10))),
                status=fake.random_element(elements=('Aktif', 'Tidak Aktif')),
                created_at=fake.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
                updated_at=fake.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S')
            )
            try:
                db.session.add(population)
                db.session.commit()
                print('Population data seeded successfully.')
            except Exception as e:
                db.session.rollback()
                print(f"Error seeding population data: {str(e)}")
    
if __name__ == '__main__':
    # Seed 100 population records
    seed_data(100)
