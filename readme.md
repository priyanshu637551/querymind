# QueryMind

AI-powered Business Analytics Assistant that converts natural language business questions into SQL queries, executes them on a PostgreSQL database, generates interactive visualizations, and provides AI-generated business insights.

---

## Overview

QueryMind enables users to analyze business data without writing SQL manually. Users simply ask questions in plain English, and the application automatically:

- Generates SQL using Google's Gemini AI
- Executes SQL on PostgreSQL
- Displays tabular results
- Generates interactive charts
- Produces AI-powered business summaries
- Maintains query history for future reference

---

## Features

### AI-Powered SQL Generation
- Converts natural language into SQL queries
- Uses Google Gemini API
- Automatically fixes invalid SQL queries

### Business Analytics
- Executes SQL on PostgreSQL
- Supports aggregation, joins, filtering, grouping, ordering, etc.
- Interactive charts using Plotly
- AI-generated business summaries

### Dashboard
- Total Orders
- Total Revenue
- Total Customers
- Total Products

### Query History
- Stores every executed query
- Search previous queries
- Filter by execution status
- Pagination support
- View complete historical reports

### Export
- Export query results to CSV

---

## Tech Stack

### Backend
- Python
- Django
- PostgreSQL

### AI
- Google Gemini API

### Frontend
- HTML
- CSS
- Bootstrap 5

### Visualization
- Plotly

### Database
- PostgreSQL

---

## Project Structure

```
QueryMind/

analytics/
│
├── services/
│   ├── gemini_service.py
│   ├── sql_executor.py
│   ├── summary_generator.py
│   ├── chart_generator.py
│   └── dashboard_service.py
│
├── templates/
│   ├── home.html
│   ├── history.html
│   └── report_detail.html
│
├── static/
│   ├── css/
│   └── images/
│
├── models.py
├── views.py
├── forms.py
└── urls.py

manage.py
requirements.txt
README.md
```

---

## Workflow

```
User Question
      │
      ▼
Google Gemini
(SQL Generation)
      │
      ▼
SQL Validation
      │
      ▼
PostgreSQL Execution
      │
      ▼
Query Results
      │
      ├────────► Plotly Chart
      │
      ├────────► AI Summary
      │
      ▼
History + Report Storage
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/querymind.git

cd querymind
```

---

### Create Virtual Environment

```bash
python -m venv myenv
```

Windows

```bash
myenv\Scripts\activate
```

Linux / macOS

```bash
source myenv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Configure Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

### Apply Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

---

### Run Server

```bash
python manage.py runserver
```

---

## Example Questions

```
Which category generates the highest revenue?

Show monthly sales.

Top 5 products by revenue.

Which payment method is most popular?

Which country has the highest sales?

Average customer rating by category.

Orders completed this month.

Top customers by spending.
```

---

## Screenshots

### Home Page

(Add screenshot here)

---

### AI Generated SQL

(Add screenshot here)

---

### Interactive Analytics Chart

(Add screenshot here)

---

### Query History

(Add screenshot here)

---

## Future Improvements

- Excel Export
- PDF Report Export
- Authentication
- Multiple Database Support
- Deployment
- Gemini SDK Migration
- Responsive UI Enhancements

---

## Learning Outcomes

This project demonstrates practical knowledge of:

- Django Application Development
- PostgreSQL
- RESTful Backend Architecture
- Prompt Engineering
- Google Gemini API Integration
- SQL Generation
- Data Visualization
- Plotly
- Bootstrap
- CSV Export
- Query History Management

---

## Author

**Priyanshu Sharma**

GitHub:
https://github.com/priyanshu637551

LinkedIn:
(Add LinkedIn Profile)

---

## License

This project is intended for educational and portfolio purposes.