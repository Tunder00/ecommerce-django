# 🛍️ Django E-Commerce Website  

A full-stack **E-Commerce web application** built using **Django**, featuring secure user authentication, product browsing, cart, checkout, and an admin dashboard for managing products and orders.

---

## 🚀 Features  

### 👤 User Features
- Register, Login, and Logout  
- Browse available products  
- View detailed product pages  
- Add products to cart and checkout  
- View previous orders  

### 🧑‍💼 Admin Features
- Dedicated admin dashboard  
- Manage orders (view and update statuses)  
- Export orders as CSV  
- Add, edit, or delete products  

### 💡 Highlights
- Django’s built-in authentication  
- SQLite database (for local dev)  
- Clean, responsive design with custom CSS  
- Media upload for product images  

---

## ⚙️ Project Setup  

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/tunder00/ecommerce-django.git
cd ecommerce-django


python -m venv env
env\Scripts\activate     # On Windows
# OR
source env/bin/activate  # On macOS/Linux

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py collectstatic

python manage.py runserver


# admin login
Username: kalyan
Password: tiger

ecommerce/
│
├── accounts/          # Handles user authentication (login/register/logout)
├── products/          # Product listing and details
├── orders/            # Cart, checkout, and order management
├── ecommerce/         # Project settings and URLs
├── static/            # CSS, JS, and images
├── templates/         # Shared templates
├── media/             # Uploaded product images
├── manage.py
├── requirements.txt
└── README.md

SECRET_KEY=your-secret-key
DEBUG=True

pip install python-decouple

from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

👨‍💻 Developer

Kalyan BN
💼 Django Full Stack Developer
📧 [kalyanbn19@gmail.com
]
🌐 https://github.com/Tunder00