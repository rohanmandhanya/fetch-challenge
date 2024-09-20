# fetch-challenge (Receipt Points Calculator)

This application calculates points from a receipt based on custom rules.


## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed on your machine.
- [Docker Compose](https://docs.docker.com/compose/install/) installed (usually included with Docker Desktop).

## Steps to Run the Application

### 1. Clone the Repository

```
git clone https://github.com/rohanmandhanya/fetch-challenge.git
cd fetch-challenge
```

### 2. Run the Application Using Docker Compose
```
docker-compose up
```
The web app will be exposed on port 8000, and the endpoints will be accessible at http://localhost:8000


### 3. Close the application
press ```Ctrl+C```


## Endpoints

### 1. Process a Receipt
- **URL**: `/receipts/process`
- **Method**: `POST`
- **Description**: Processes a receipt and returns an `id` for the receipt.

### 2. Get Points for a Receipt
- **URL**: `/receipts/{id}/points`
- **Method**: `GET`
- **Description**: Retrieves the points awarded for a specific receipt.