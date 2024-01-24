# Pricing-Module-v2
The Pricing Module is designed for storing and managing product/service prices. It also holds the logic that calculates the final invoice amount based on the time and the distance traveled.
Clone the Repository
----------------------------
git clone https://github.com/AmitPaltankar/Pricing-Module-v2/

Navigate to the Project Directory
------------------------------------------
cd django-pricing-module

Install Dependencies
-----------------------------------------
pip install -r requirements.txt


Database Setup
----------------------
Run Migrations
------------------------------
python manage.py makemigrations
python manage.py migrate

Create a Superuser
-----------------------------
python manage.py createsuperuser

Django Admin
---------------------
Start the Development Server
------------------------------
python manage.py runserver


Access the Django Admin Interface
---------------------------------------------
Open your browser and go to http://127.0.0.1:8000/admin/

Log in
-----------------------------------
Use the superuser credentials created earlier to log in.

Manage Pricing Configurations
----------------------------------------------
Navigate to the "Pricing Config" section to add, modify, or remove pricing configurations.
Customize Distance Base Price, Distance Additional Price, Time Multiplier Factor, and Waiting Charges.

