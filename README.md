# Project Title

Brief description of the project.

## Prerequisites

- Docker installed on your machine.

## Getting Started

1. Clone this repository to your local machine.
2. Navigate to the project directory in your terminal.

## Running the Application

### Update .env File

Open the existing `.env` file in the root directory of the project.

Add or update the following environment variables in the `.env` file:

```dotenv
TWILLIO_AUTH_TOKEN=YOUR_TWILIO_AUTH_TOKEN
TWILLIO_ACCOUNT_SID=YOUR_TWILIO_ACCOUNT_SID
TWILLIO_NUMBER=YOUR_TWILIO_NUMBER
```

Replace TWILLIO_AUTH_TOKEN, TWILLIO_ACCOUNT_SID, and TWILLIO_NUMBER with your actual Twilio credentials.

Save the .env file after making changes.

To run the Django application in a Docker container, use the following command:

```bash
docker build -t my-django-app . && docker run -p 8000:8000 -v "$(pwd)/logs.log:/web_django/logs.log" my-django-app

