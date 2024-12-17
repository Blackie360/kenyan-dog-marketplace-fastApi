
```markdown
# Kenyan Dog Marketplace API

## Overview

The **Kenyan Dog Marketplace API** is an API designed to connect dog buyers and sellers in Kenya, providing a platform to search and create dog listings based on various criteria. The API includes geolocation support to ensure that all data is relevant to Kenyan users and regions.

This API allows users to create, read, and search for dog listings, with detailed information on each dog, including breed, age, price, and location. It also supports user registration and management.

## Features

- **Create Dog Listings**: Users can create new dog listings with details such as breed, price, age, and location.
- **Search Dogs**: Search for available dogs based on parameters like breed, location, price range, and distance from a specific point.
- **User Management**: Create and manage user profiles.
- **Geolocation Support**: Ensures that all data is within the boundaries of Kenya, with support for location-based searches.
- **Data Validation**: Strong data validation ensures that users only submit valid data (e.g., valid Kenyan counties, dog breeds).
- **Security**: Password hashing using bcrypt for secure password storage.
- **Search Capabilities**: Ability to filter listings by breed, price, and location, with support for combined filters.

## Installation

### Prerequisites

- **Python 3.7 or higher**
- **pip** (Python package manager)

### Local Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Blackie360/kenyan-dog-marketplace-fastApi.git
   cd kenyan-dog-marketplace-fastApi
   ```

2. **Create and activate the virtual environment**:

   For Linux/MacOS:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   For Windows:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Start the server**:

   ```bash
   uvicorn app.main:app --reload
   ```

   The API will be available at `http://127.0.0.1:8000`.

## API Documentation

Once the server is running, you can access the interactive API documentation at:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc UI**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Main Endpoints

### Users API

- **Create User**: `POST /api/v1/users/`
- **Get User**: `GET /api/v1/users/{user_id}`

### Dogs API

- **Create Dog**: `POST /api/v1/dogs/`
- **Search Dogs**: `GET /api/v1/dogs/`  
  Supports filtering by:
  - **Location**: Search for dogs within a specified distance from a location.
  - **Breed**: Filter by specific dog breed.
  - **Price Range**: Filter by price range.

## Models

### User Model

```json
{
  "name": "str",          // 2-50 characters
  "email": "str",         // Valid email format
  "phone": "str",         // Valid Kenyan phone number
  "password": "str",      // Min 8 characters (for creation only)
  "location": {
    "latitude": "float",  // Valid Kenya coordinates
    "longitude": "float", // Valid Kenya coordinates
    "city": "str",
    "county": "str"       // Must be valid Kenyan county
  }
}
```

### Dog Model

```json
{
  "name": "str",          
  "breed": "str",        
  "age_months": "int",    
  "price": "float",       
  "description": "str",   
  "location": {
    "latitude": "float", 
    "longitude": "float", 
    "city": "str",
    "county": "str"       
  }
}
```

## Database

- **Uses SQLite** (dogs.db).
- **Created automatically** on the first run.
- **Tables**:
  - **users**: Stores user information.
  - **dogs**: Stores dog listings.
  - **Relationships**: One-to-many between users and dogs.

## Features

- **Geolocation**:
  - Validates coordinates within Kenya.
  - Supports distance-based search for dogs.
  - County validation against official Kenyan counties.

- **Data Validation**:
  - Validates Kenyan phone numbers.
  - Checks for valid email addresses.
  - Ensures valid county names for location.
  - Validates dog breeds from a predefined list.
  - Ensures price and age ranges for dogs are valid.

- **Search Capabilities**:
  - Search by **location radius**.
  - Filter by **breed**.
  - Filter by **price range**.
  - Support for **combined filters** (location, breed, price).

## Security Features

- **Password hashing** using bcrypt for secure password storage.
- **Input validation and sanitization** to protect against malicious inputs.
- **Error handling** for invalid requests to ensure robust API responses.

## Contribution

We welcome contributions! Feel free to fork the repository, create a new branch, and submit a pull request with any changes you'd like to propose.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

