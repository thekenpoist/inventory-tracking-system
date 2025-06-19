# Tooling Inventory Tracking System

**NOTE:** This project is still under development. New features are being added as time permits.

This is a full-stack inventory management application built using **Python, Flask, SQLAlchemy, and MySQL**, styled with **Bootstrap 5**. It provides a clean, web-based interface for organizing, searching, and managing tooling inventory—ideal for shop floors, machine shops, or any environment with parts and category-based tracking needs.

---

## Features

- View items grouped by category with visual cards  
- Relational data models for structured part management  
- Responsive UI with Bootstrap 5  
- Jinja2 templating for dynamic HTML rendering  
- Organized using the MVC pattern  
- [In Progress] Add and edit inventory records  
- [Planned] Filter and search tools by category or part number  
- [Planned] Authentication system for secure access  

---

## Tech Stack

- **Backend:** Python, Flask, SQLAlchemy  
- **Frontend:** HTML5, CSS, Bootstrap 5, Jinja2  
- **Database:** MySQL or MariaDB  
- **Routing & Views:** Flask blueprints and dynamic templating  
- **Project Structure:** Modular MVC-style organization  

---

## Screenshot

![Tooling Inventory Dashboard](./screenshots/catalog.jpg)  
*Dashboard showing tool categories and linked inventory views.*

---

## Getting Started (Local Dev)

### Prerequisites
- Python 3.x  
- MySQL or MariaDB  
- Flask  
- SQLAlchemy  
- See `requirements.txt` for full dependencies

### 1. Clone the Repo
```bash
git clone https://github.com/thekenpoist/inventory-tracking-system.git
cd inventory-tracking-system
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure Environment
Update your `config.py` or create a `.env` with the following connection string:

```python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@localhost/tooling_inventory'
```

### 4. Initialize the Database
If you're using Flask-Migrate:

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 5. Run the App
```bash
flask run
```

Then open your browser to `http://localhost:5000`

---

## Roadmap

- [ ] Add user authentication (login/logout with role access)  
- [ ] Enable CSV export for tool lists  
- [ ] Add audit log or activity history   
- [ ] Implement advanced search/sort/filter features  

---

## License

This project is licensed under the **GNU General Public License v3.0**

---

## Contact

If you have any questions or need further assistance, feel free to email:  
hullstevenj@gmail.com
