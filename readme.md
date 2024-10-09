
## Installation

1. Clone dette repository:

```
   git clone https://github.com/NikoKiru/inventory_service
   cd inventory_service
   docker build -t inventory_service .
   docker run -it --rm -p 5000:5000 -v ${PWD}:/home/data inventory_service
```

## API Endpoints

### FIND Stock by product

- **URL:** `/stock/<int:product_id>`
- **Method:** `GET`
- **Request Body:** JSON

- **Response:**

  - **200 OK** Product stock was returned

### Search Product by Title

- **URL:** `/change/<int:product_id>/<int:new_value>`
- **Method:** `POST`

- **Response:**

  - **200 OK:** Changed stock