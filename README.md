# Portfolio_website_Django 

A **dynamic and responsive portfolio website** built using **Django, PostgreSQL, and Bootstrap**, following the **Model-View-Template (MVT) architecture**.  

## **📌 Features**  
✅ **Home Page** – Showcasing an introduction and brief about me.  
✅ **About Section** – Highlighting my education, skills, and experience.  
✅ **Projects Page** – Displaying my personal and academic projects.  
✅ **Skills Section** – Listing my technical expertise.  
✅ **Contact Form** – Allows visitors to send messages directly to me.  
✅ **Responsive Design** – Built using **Bootstrap** for a seamless user experience on all devices.  

## **🛠 Tech Stack**  
- **Framework:** Django  
- **Database:** PostgreSQL  
- **Frontend:** HTML, CSS, Bootstrap  
- **Backend:** Django (Python)  
- **Version Control:** Git & GitHub  

## **🔧 Setup & Installation**  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/your-username/portfolio-website.git
cd portfolio-website
```

### **2️⃣ Create and Activate a Virtual Environment**  
```sh
python -m venv venv
source venv/bin/activate   # For macOS/Linux
venv\Scripts\activate      # For Windows
```

### **3️⃣ Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **4️⃣ Configure Database**  
- Open `settings.py` and update database settings (PostgreSQL or SQLite).  
- Run migrations:  
```sh
python manage.py migrate
```

### **5️⃣ Run the Server**  
```sh
python manage.py runserver
```
Your portfolio will be accessible at `http://127.0.0.1:8000/` 🚀  

## **📂 Project Structure**  
```
portfolio/
│── qualification/        # Django app for education & skills
│── templates/            # HTML templates for frontend
│── static/               # CSS, JS, Images
│── portfolio/            # Main Django project files
│── db.sqlite3            # SQLite Database (can be PostgreSQL)
│── manage.py             # Django management script
│── README.md             # This file
```

## **📜 MVT Architecture Explained**  
The project follows the **Model-View-Template (MVT)** architecture:  
- **Model (M):** Handles database interactions (storing projects, skills, etc.).  
- **View (V):** Processes requests, fetches data, and sends it to templates.  
- **Template (T):** Renders the frontend using Django’s templating engine.

## **Snapshots** 
![image](https://github.com/user-attachments/assets/6cb3e7ce-4596-4324-945a-4c2c5f85d923)

![image](https://github.com/user-attachments/assets/9b7a47f8-abb2-462a-82f6-fb02da27a06d)


## **📩 Contact**  
If you have any queries or feedback, feel free to reach out via the **Contact** section of my portfolio or through:  
📧 **Email:** akshayenuguru3@gmail.com 

🔗 **LinkedIn:** https://www.linkedin.com/in/akshayenuguru/
