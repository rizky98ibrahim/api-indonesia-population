# Usage

## Running the Application

To run the application, execute the following command:

```bash
python run.py
```

By default, the application runs on `http://127.0.0.1:5000`.

## Migration

Migrations are used to manage database schema changes. The project includes a `migrations` folder for this purpose. To run migrations, follow these steps:

1. Generate a migration script:

   ```bash
   flask db migrate -m "Migration message"
   ```

2. Apply the migrations to the database:

   ```bash
   flask db upgrade
   ```

## Seeder

The `seeder.py` file provides functionality to seed the database with sample population data. To run the seeder, use the following command:

```bash
python seeder.py
```
