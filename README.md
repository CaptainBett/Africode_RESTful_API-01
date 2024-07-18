---

# Flask RESTful API with SQLAlchemy

This is a simple Flask RESTful API project using SQLAlchemy for database management. It includes basic CRUD operations for a `UserModel` with `username` and `email` fields.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Running the Application](#running-the-application)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv env
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source env/bin/activate
     ```

4. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Set up the database:**
   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

2. **Run the application:**
   ```bash
   python app.py
   ```

3. **Access the application:**
   Open your browser and navigate to `http://127.0.0.1:5000/`

## API Endpoints

### List All Users

- **URL:** `/api/users/`
- **Method:** `GET`
- **Response:**
  ```json
  [
    {
      "id": 1,
      "username": "user1",
      "email": "user1@example.com"
    },
    ...
  ]
  ```

### Create a New User

- **URL:** `/api/users/`
- **Method:** `POST`
- **Payload:**
  ```json
  {
    "username": "newuser",
    "email": "newuser@example.com"
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "username": "newuser",
    "email": "newuser@example.com"
  }
  ```

### Get a Specific User

- **URL:** `/api/users/<int:id>`
- **Method:** `GET`
- **Response:**
  ```json
  {
    "id": 1,
    "username": "user1",
    "email": "user1@example.com"
  }
  ```

### Update a User

- **URL:** `/api/users/<int:id>`
- **Method:** `PATCH`
- **Payload:**
  ```json
  {
    "username": "updateduser",
    "email": "updateduser@example.com"
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "username": "updateduser",
    "email": "updateduser@example.com"
  }
  ```

### Delete a User

- **URL:** `/api/users/<int:id>`
- **Method:** `DELETE`
- **Response:**
  ```json
  [
    {
      "id": 2,
      "username": "user2",
      "email": "user2@example.com"
    },
    ...
  ]
  ```

## Running the Application

1. **Run the Flask development server:**
   ```bash
   python app.py
   ```

2. **Access the application:**
   Open your browser and navigate to `http://127.0.0.1:5000/`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
