# Non-Communicable Diseases Charity Backend API

![API Status](https://img.shields.io/badge/status-active-brightgreen)
![Version](https://img.shields.io/badge/version-1.0.0-blue)

A RESTful API backend for managing non-communicable disease charity operations, including user authentication, case management, disease tracking, and donation processing.

## Table of Contents

* [Features](#features)
* [Project Structure](#project-structure)
* [API Endpoints](#api-endpoints)
* [Authentication](#authentication)
* [Environment Setup](#environment-setup)
* [Running the Server](#running-the-server)
* [Testing](#testing)
* [Postman Collection](#postman-collection)
* [Database Schema](#database-schema)
* [Deployment](#deployment)
* [Contributing](#contributing)
* [License](#license)

## Features

* **User Management**: Registration, authentication, and role-based access control
* **Disease Tracking**: Maintain database of non-communicable diseases
* **Case Management**: Create and track fundraising cases
* **Geospatial Data**: Track affected areas with latitude/longitude coordinates
* **Donation System**: Process and record charitable donations
* **Resource Library**: Store educational materials and resources

## Project Structure

```
non-communicable-diseases-charity-backend/
│
├── .venv/                     # Python virtual environment
├── __pycache__/               # Python bytecode cache
│
├── app/                       # Main application package
│   ├── __init__.py            # Package initialization
│   ├── __pycache__/           # Bytecode cache
│   │
│   ├── models/                # Database models
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   ├── area.py            # Area model
│   │   ├── association.py     # Association tables
│   │   ├── case.py            # Case model
│   │   ├── disease.py         # Disease model
│   │   ├── donation.py        # Donation model
│   │   ├── resource.py        # Resource model
│   │   ├── review.py          # Review model
│   │   └── user.py            # User model
│   │
│   ├── routes/                # API route handlers
│   │   ├── __init__.py
│   │   ├── __pycache__/
│   │   ├── admin_routes.py     # Admin-specific routes
│   │   ├── area_routes.py      # Area-related routes
│   │   ├── auth_routes.py      # Authentication routes
│   │   ├── case_routes.py      # Case-related routes
│   │   ├── disease_routes.py   # Disease-related routes
│   │   ├── donation_routes.py  # Donation-related routes
│   │   ├── resource_routes.py  # Resource-related routes
│   │   ├── review_routes.py    # Review-related routes
│   │   └── user_routes.py      # User-related routes
│   │
│   ├── core/                  # Core application components
│   │   ├── __init__.py
│   │   ├── config.py          # Configuration settings
│   │   ├── extensions.py      # Flask extensions
│   │   ├── int_helpers.py     # Helper functions
│   │   ├── schemas.py         # Marshmallow schemas
│   │   └── validations.py     # Data validations
│   │
│   └── instance/              # Instance-specific files
│       └── config.py          # Instance configuration
│
├── migrations/                # Database migration scripts
│
├── .env                       # Environment variables
├── .flaskenv                  # Flask environment settings
├── .python-version            # Python version specification
│
├── app.py                     # Main application entry point
├── docker-compose.yml         # Docker compose configuration
├── Dockerfile                 # Docker configuration
├── Pipfile                    # Pipenv dependencies
├── Pipfile.lock               # Locked dependencies
├── Procfile                   # Process file for deployment
├── README.md                  # Project documentation
├── render.yaml                # Render deployment config
├── requirements.txt           # Python requirements
├── seed.py                    # Database seeding script
└── wsgi.py                    # WSGI entry point
```

## API Endpoints

### Authentication

| Method | Endpoint         | Description             |
| ------ | ---------------- | ----------------------- |
| POST   | `/auth/register` | Register new user       |
| POST   | `/auth/login`    | Login and get JWT token |

### Users

| Method | Endpoint           | Description                   |
| ------ | ------------------ | ----------------------------- |
| GET    | `/users/me`        | Get current user profile      |
| PATCH  | `/users/{id}/role` | Update user role (Admin only) |

### Cases

| Method | Endpoint  | Description                  |
| ------ | --------- | ---------------------------- |
| GET    | `/cases/` | Get all fundraising cases    |
| POST   | `/cases/` | Create new case (Admin only) |

### Diseases

| Method | Endpoint     | Description                   |
| ------ | ------------ | ----------------------------- |
| GET    | `/diseases/` | Get all disease records       |
| POST   | `/diseases/` | Create disease record (Admin) |

### Areas

| Method | Endpoint      | Description                     |
| ------ | ------------- | ------------------------------- |
| GET    | `/areas/`     | Get all geographic areas        |
| GET    | `/areas/{id}` | Get specific area by ID         |
| GET    | `/areas/map`  | Get geospatial data for mapping |
| POST   | `/areas/`     | Create new area (Admin)         |
| PUT    | `/areas/{id}` | Update area (Admin)             |
| DELETE | `/areas/{id}` | Delete area (Admin)             |

### Reviews

| Method | Endpoint    | Description       |
| ------ | ----------- | ----------------- |
| GET    | `/reviews/` | Get all reviews   |
| POST   | `/reviews/` | Create new review |

### Donations

| Method | Endpoint      | Description         |
| ------ | ------------- | ------------------- |
| GET    | `/donations/` | Get all donations   |
| POST   | `/donations/` | Record new donation |

### Resources

| Method | Endpoint      | Description                   |
| ------ | ------------- | ----------------------------- |
| GET    | `/resources/` | Get all educational resources |
| POST   | `/resources/` | Add new resource (Admin)      |

## Authentication

The API uses JWT (JSON Web Tokens) for authentication. Include the token in the `Authorization` header:

```http
Authorization: Bearer your.jwt.token.here
```

## Environment Setup

Clone the repository:

```bash
git clone https://github.com/your-repo/ncd-charity-backend.git
cd ncd-charity-backend
```

Install dependencies:

```bash
npm install
```

Create `.env` file based on `.env.example`:

```env
PORT=10000
DATABASE_URL=your_database_connection_string
JWT_SECRET=your_jwt_secret_key
ADMIN_USERNAME=admin
ADMIN_PASSWORD=secure_admin_password
```

## Running the Server

Start the development server:

```bash
npm run dev
```

Production build:

```bash
npm run build
npm start
```

## Testing

Run unit tests:

```bash
npm test
```

## Postman Collection

A complete Postman collection is available in the repository (`Non-Communicable-Diseases-Charity-Backend-API-collection.json`).

Import this collection to:

* Test all API endpoints
* View example requests and responses
* Automate API testing

## Database Schema

![Schema](https://docs/db-schema.png)

Key tables:

* `users` - User accounts and authentication
* `diseases` - Non-communicable disease information
* `cases` - Fundraising campaigns
* `areas` - Geographic locations with disease prevalence
* `donations` - Donation records
* `resources` - Educational materials

## Deployment

The API can be deployed to:

* Heroku
* AWS Elastic Beanstalk
* Docker containers

Example Docker deployment:

```bash
docker build -t ncd-charity-api .
docker run -p 10000:10000 -d ncd-charity-api
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.
