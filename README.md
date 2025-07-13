# Product Review Management System

## Prerequisites

- Python 3.8 or higher

## Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd DjangoRestAssignment/product_review
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**For Windows:**
```bash
venv\Scripts\activate
```

**For macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

If requirements.txt doesn't exist, install the required packages manually:

```bash
pip install django==5.2.4
pip install djangorestframework
```

### 5. Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## API Endpoints

### Authentication Endpoints

#### 1. User Registration
- **URL**: `POST /api/register/`
- **Description**: Register a new user account

```bash
curl -X POST "${BASE_URL}/register/" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john",
    "password": "pass123",
    "is_admin": false
  }'
```
- **Response**:
```json
{
    "token": "sdfghhxcAlGkaGsdScndsfj...."
}
```

#### 2. User Login
- **URL**: `POST /api/login/`
- **Description**: Authenticate user and get access token

```bash
curl -X POST "${BASE_URL}/login/" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john",
    "password": "pass123"
  }'
```
- **Response**:
```json
{
    "token": "your-auth-token-here"
}
```

### Product Endpoints

#### 3. List All Products (Everyone)
- **URL**: `GET /api/products/`
- **Description**: Retrieve all available products
- **Authentication**: Not required (read-only)
```bash
curl -X GET "${BASE_URL}/products/" \
  -H "Content-Type: application/json"
```
- **Response**:
```json
[
    {
        "id": 1,
        "name": "Smartwatch X1",
        "description": "Water-resistant smartwatch with fitness tracking",
        "price": "249.99",
        "average_rating": 4.5"reviews": [
            {
                "id": 1,
                "product": 1,
                "user": "username",
                "rating": 5,
                "feedback": "Excellent product! Highly recommended.",
                "created_at": "2024-01-15T10:30:00Z"
            },
            {
                "id": 2,
                "product": 1,
                "user": "another_user",
                "rating": 4,
                "feedback": "Great product, but battery life could be better.",
                "created_at": "2024-01-16T12:00:00Z"
            }
        ]
    }
]
```


#### 4. Create Product (Admin Only)
- **URL**: `POST /api/products/`
- **Description**: Add a new product to the system
- **Authentication**: Required (Admin token)
- **Request Body**:
```bash
curl -X POST "${BASE_URL}/products/" \
  -H "Content-Type: application/json" \
  -H "Authorization: Token ${ADMIN_TOKEN}" \
  -d '{
    "name": "New Product",
    "description": "Product description here",
    "price": "99.99"
  }'
```

#### 5. Update Product (Admin Only)
- **URL**: `PUT /api/products/{id}/`
- **Description**: Update existing product information
- **Authentication**: Required (Admin token)
```bash
curl -X PUT "${BASE_URL}/products/${PRODUCT_ID}/" \
  -H "Content-Type: application/json" \
  -H "Authorization: Token ${ADMIN_TOKEN}" \
  -d '{
    "price": "99.99"
  }'
```

#### 6. Delete Product (Admin Only)
- **URL**: `DELETE /api/products/{id}/`
- **Description**: Remove a product from the system
- **Authentication**: Required (Admin token)
```bash
curl -X DELETE "${BASE_URL}/products/${PRODUCT_ID}/" \
  -H "Content-Type: application/json" \
  -H "Authorization: Token ${ADMIN_TOKEN}"
```
### Review Endpoints

#### 7. Create Review (Auth Only)
- **URL**: `POST /api/reviews/`
- **Description**: Submit a review for a product
- **Authentication**: Required (User token)
- **Request Body**:
```bash
curl -X POST "${BASE_URL}/reviews/" \
  -H "Content-Type: application/json" \
  -H "Authorization: Token ${TOKEN}" \
  -d '{
    "product": 1,
    "rating": 5,
    "feedback": "Excellent product! Highly recommended."
  }'
```



