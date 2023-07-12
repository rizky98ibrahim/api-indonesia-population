# Indonesian Population Data API (Faker)

This project provides a public API for retrieving simulated population data of Indonesia. The data is generated using the Faker library. The API is built using Flask and PostgreSQL.

## Getting Started

To get started with the project, follow the instructions below.

### Prerequisites

- [Python](https://www.python.org/) (version 3.9.X)
- [Flask](https://flask.palletsprojects.com/) (version 2.3.X)
- [PostgreSQL](https://www.postgresql.org/) (version 13.X)
- [Faker](https://faker.readthedocs.io/) (version 8.12.X)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/rizky98ibrahim/api-indonesia-population.git
   ```

2. Create a virtual environment:

   ```bash
   # Windows
   py -3 -m venv venv
   # Linux/macOS
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   ```bash
    # Windows
    venv\Scripts\active
    
    # Linux
    source venv/bin/activate    
    ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Set up the envirotment variables by creating a `.env` filein the root directory of the project and add the following variables:

   ```bash
   FLASK_APP=app.py
   FLASK_ENV=development
   DATABASE_URL=postgresql://[username]:[password]@localhost:5432/[database_name]
   ```

6. Run the application:

   ```bash
   python run.py
   ```

7. The API will be accessible at `http://localhost:5000/api/population`.

## Usage

For detailed information on how to use the API and its endpoints, please refer to the [Usage Documentation](documentation/usage.md).

## API Endpoints

For a list of available API endpoints and their descriptions, please refer to the [API Endpoints Documentation](documentation/api-endpoints.md).

## Contributing

Contributions to the project are welcome. To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or comments about this repository, please feel free to contact me through the following channels:

[![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/6287808740020)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:rizky98ibrahim@gmail.com)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/rizky98ibrahim)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rizky98ibrahim/)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/rizky98ibrahim)
