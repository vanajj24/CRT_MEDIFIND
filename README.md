**Nearby Medical Shop Medicine Finder**

**Project Content**
This project is a web-based system designed to help users locate nearby medical stores that stock specific medicines. It includes:
User and admin registration/login system with JWT-based authentication
Admin dashboard for managing stores and medicine inventory
Users can search for medicines using live location or manual location input
Medicine stock is displayed with distance from user
Secure and responsive interface built with HTML, CSS, and JavaScript
Backend API using Flask and MySQL with role-based access control

**Project Code**
This project consists of multiple HTML templates and a Python backend. The core files include:
app.py: Flask server managing authentication, medicine and store management, and search API.
scrt.sql: MySQL schema for users, stores, medicines, and inventory.

HTML pages:
index.html: Combined registration and login UI
dashboard.html: Dashboard view with user profile and navigation
add_store.html: Admin interface to add a new medical store
add_medicine.html: Admin interface to add new medicines to a store
search.html: UI for users to search for medicines by name and location
register.html and login.html: Separate pages for registration and login (optional use)

**Key Technologies**
Frontend:
HTML5
CSS3
JavaScript
Google Maps Places API (for location autocomplete)

Backend:
Python 3
Flask Web Framework
Flask-JWT-Extended for token-based authentication
Flask-CORS for cross-origin requests
MySQL database using PyMySQL connector

Database:
MySQL with relational schema consisting of users, stores, medicines, and inventory tables

**Descriptions**
User Roles:
Users can register, log in, and search for medicines based on location.
Admins can manage stores and add medicines.

Authentication:
Login system uses JWT tokens. Only logged-in users can access protected endpoints like profile and inventory addition.

Medicine Search:
Search uses live geolocation or manual location entry.
Distance is calculated using the Haversine formula.
Results are filtered to show stores within a 50 km radius.

Admin Features:
Add new medical stores with optional latitude and longitude
Add medicines and link them to stores
Populate inventory and set alerts for stock levels

**Output**
When the user logs in:
A dashboard is shown with user profile and navigation options
Admin sees additional links to manage store and medicine data
Search results display:
Name of medicine
Store name and address
Stock level
Distance from user

Example output for a search:
Medicine: Paracetamol
Store: Apollo Pharmacy
Address: Hitech City, Hyderabad
Stock: 25
Distance: 3.42 km

**Further Research**
To expand the scope of this project, the following features can be researched and added:
Live GPS Tracking: Integrate phone-based GPS for accurate current location detection.
Push Notifications: Notify users when a medicine they searched for becomes available nearby.
User Feedback & Ratings: Allow users to rate pharmacies and provide feedback.
E-Prescription Upload: Add a feature to upload and validate prescriptions.
Online Ordering Integration: Collaborate with delivery partners for doorstep delivery.
Admin Analytics Dashboard: Show most searched medicines, stock movement, etc.
Map View: Display search results on an interactive map using Google Maps API.
ML-based Suggestions: Recommend medicines or alternatives using past search patterns.
Inventory Forecasting: Use historical stock usage to predict and alert about low stock.
Multi-language Support: Add translations for regional languages for better accessibility.
Run Instructions
Install Python and MySQL.

Setup the database:
mysql -u root -p < scrt.sql

Install dependencies:
pip install flask flask-cors flask-jwt-extended pymysql

Run the server:
python app.py
Open index.html or login.html in a browser to begin using the application.

Folder Structure
project-root/
│
├── app.py
├── scrt.sql
│
├── index.html
├── login.html
├── register.html
├── dashboard.html
├── add_store.html
├── add_medicine.html
├── search.html
