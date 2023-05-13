# weatherapp
The Weather API is a Django-based RESTful API that provides weather data for a specific location. This API allows authorized users to access weather data via GET requests to a specified endpoint.
To start the API locally, follow these steps:
1. Clone the repository: git clone https://github.com/amnonih/weatherapp.git
2. Create and activate a virtual environment:
         python -m venv venv
         venv\Scripts\activate  # for Windows
         
3. Install the required dependencies: pip install -r requirements.txt
4. Apply database migrations: python manage.py migrate
5. Create a superuser account (to access the Django admin panel): python manage.py createsuperuser
6. Run the development server: python manage.py runserver
The API should now be accessible at http://127.0.0.1:8000/. You can view the API documentation at https://editor.swagger.io/.

API AUTHENTICATION
To ensure that only authorized users can access the API, the API requires basic authentication. Users and their passwords are stored in the database.

API ENDPOINTS
The following endpoints are available: 
  1. /api/weather/ - This endpoint returns the current weather data for a specified location.
  2. /api/weather/past/ - This endpoint returns the past weather data for a specified location and date range.
  3. /api/weather/forecast/ - This endpoint returns the weather forecast data for a specified location and date range.

TECHNOLOGIES USED:
Python
Django
Django REST framework
Postman
OpenAPI
Swagger UI


