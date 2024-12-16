

```markdown
# Kenyan Dog Marketplace API

## Overview

The **Kenyan Dog Marketplace API** is an API designed to connect dog buyers and sellers in Kenya, providing a platform to search and create dog listings based on various criteria. The API includes geolocation support to ensure that all data is relevant to Kenyan users and regions.

This API allows users to create, read, and search for dog listings, with detailed information on each dog, including breed, age, price, and location. It also supports user registration and management.

## Features

- **Create Dog Listings**: Users can create new dog listings with details such as breed, price, age, and location.
- **Search Dogs**: Search for available dogs based on parameters like breed, location, price range, and distance from a specific point.
- **User Management**: Create and manage user profiles.
- **Geolocation Support**: Ensure that all data is within the boundaries of Kenya, with support for location-based searches.
- **Data Validation**: Strong data validation ensures that users only submit valid data (e.g., valid Kenyan counties, dog breeds).

## Installation

To run the API locally, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Blackie360/kenyan-dog-marketplace-fastApi.git
   cd kenyan-dog-marketplace-fastApi
   ```

2. **Create a virtual environment**:

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

4. **Set up the database**:

   This API uses SQLite for local development. The database will be automatically created when you run the API.

5. **Run the API**:

   ```bash
   uvicorn app.main:app --reload
   ```

   The API will be available at `http://127.0.0.1:8000`.

## API Documentation

Once the server is running, you can access the interactive API documentation at:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc UI**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Endpoints

### Dogs Endpoints

- **POST /api/v1/dogs/**: Create a new dog listing.
- **GET /api/v1/dogs/**: Search for dogs. You can filter by breed, price range, location, and distance.

### Users Endpoints

- **POST /api/v1/users/**: Create a new user profile.
- **GET /api/v1/users/{user_id}**: Get a specific user profile by user ID.

## Models

### Dog Model

- **name**: The name of the dog.
- **breed**: The breed of the dog.
- **age_months**: The age of the dog in months.
- **price**: The price of the dog in Kenyan Shillings.
- **description**: Optional description of the dog.
- **location**: Geolocation data (latitude, longitude, city, and county).

### User Model

- **id**: A unique identifier for the user.
- **name**: Name of the user.
- **email**: User's email.
- **phone**: User's phone number (Kenyan format).
- **location**: Geolocation data (latitude, longitude, city, and county).

## Configuration

The API settings are stored in `app/config/settings.py`, including:

- **APP_NAME**: The name of the application.
- **APP_VERSION**: The version of the application.
- **APP_DESCRIPTION**: A brief description of the API.
- **Kenya's geographic boundaries**: Ensures that only locations within Kenya are used in the API.

## Database

The API uses SQLAlchemy with SQLite as the database. The database schema includes tables for **users** and **dogs**, and it is automatically created when you start the application.

## Contribution

We welcome contributions! Feel free to fork the repository, create a new branch, and submit a pull request with any changes you'd like to propose.

```

### Key Details:

- **Installation**: Provides step-by-step instructions on setting up the project locally.
- **API Documentation**: Direct links to Swagger and ReDoc for interactive API exploration.
- **Endpoints**: Lists the main API endpoints for dogs and users.
- **Models**: Describes the Dog and User models, including all necessary fields.
- **Database**: Mention of SQLite as the backend and automatic database creation on startup.

This should serve as a comprehensive guide for users to get started with the API, interact with the endpoints, and contribute to the project.
