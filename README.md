# inventory-backend
# 📦 Inventory Management App - Backend (Flask API)

## 🔧 Overview

This is the **Flask API backend** for the Inventory Management Application. It supports a full-stack inventory tracking system with users, items, and warehouses. The API includes:

* Full CRUD for Items
* Read/Create for Users and Warehouses
* One-to-many and many-to-many relationships
* User-submittable attributes in the many-to-many association
* Data validation and proper serialization

The frontend is built using React and integrates with this backend via `fetch()`.

---

## 🧱 Models & Relationships

### 1. **User**

* `id` (PK)
* `username` (string, required, unique)
* `email` (string, required, format-validated)

### 2. **Warehouse**

* `id` (PK)
* `name` (string, required)
* `location` (string, required)

### 3. **Item**

* `id` (PK)
* `name` (string, required)
* `quantity` (integer, required)
* `warehouse_id` (FK to Warehouse)

### 4. **UserItem** *(Association Model)*

* `id` (PK)
* `user_id` (FK)
* `item_id` (FK)
* `notes` (string - submittable attribute)

#### ✅ Relationships:

* **User** `has_many` UserItems
* **Item** `has_many` UserItems
* **Warehouse** `has_many` Items
* **User <--> Item**: Many-to-many through `UserItem`

---

## 🔄 API Endpoints

### 📍 Users

* `GET /users` - List all users
* `POST /users` - Create a user

### 🏬 Warehouses

* `GET /warehouses` - List all warehouses
* `POST /warehouses` - Create a warehouse

### 📦 Items

* `GET /items` - List all items
* `GET /items/<id>` - Retrieve single item
* `POST /items` - Create an item
* `PATCH /items/<id>` - Update an item
* `DELETE /items/<id>` - Delete an item

### 🤝 UserItem (many-to-many with notes)

* `POST /user_items` - Link user to item with a note
* `GET /user_items` - View all user-item links

---

## ✅ Validations

* Email format validation (`email@domain.com`)
* Quantity must be a positive integer
* Name and username fields must be strings and non-empty

---

## 🧪 Technologies Used

* Python 3.11+
* Flask
* Flask SQLAlchemy
* Marshmallow for serialization/validation
* SQLite (development)

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/kareeeeeey/inventory-backend.git
cd inventory-backend
```

### 2. Set up a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations and seed the database

```bash
flask db init
flask db migrate
flask db upgrade
python seed.py
```

### 5. Start the server

```bash
flask run
```

---

## 🌐 API URL

```
http://localhost:5001
```

---

## 🧪 Testing

You can use Postman or cURL to test the endpoints, or interact directly via the connected React frontend.

---

## 📁 File Structure

```
backend/
├── app.py
├── config.py
├── models.py
├── routes.py
├── seed.py
├── migrations/
└── requirements.txt
```

---

## ✨ MVP Features Recap

* Users can create an account
* Users can submit inventory items with quantities
* Items belong to warehouses
* Users can associate notes with items via a many-to-many table
* Forms in frontend are validated via Formik (email format, quantity type, required fields)

---

## 🚀 Future Improvements

* Authentication system
* Pagination for item lists
* Item status (in stock, out of stock)
* Warehouse capacity limit

---

## 🔗 Frontend Integration

This backend is connected to a React frontend using `fetch()` calls to the endpoints above. All data is rendered in React components routed using `react-router-dom`, with forms managed and validated via Formik.

Frontend routes include:

* `/` - Dashboard (Items overview)
* `/users` - User list and user-item associations
* `/warehouses` - Warehouse list and item breakdown per location

---


## 👨‍💻 Author

Cynthia 
