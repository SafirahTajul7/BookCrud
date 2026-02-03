# BookCrud: Full-Stack Book Management System

This project is a simple yet robust full-stack application designed to manage a collection of books. It allows users to add, view, update, and delete book records through an intuitive web interface. The frontend is built with React, providing a dynamic user experience, while the backend is powered by FastAPI, offering a fast and efficient RESTful API. Data persistence is handled using SQLAlchemy, with a default SQLite database.

## Features

*   **Add New Books:** Easily add new book entries with title, author, and published year.
*   **View All Books:** Display a comprehensive list of all stored books in a tabular format.
*   **Edit Book Details:** Update information for existing books.
*   **Delete Books:** Remove book entries from the system.
*   **Responsive UI:** User-friendly web interface built with React.
*   **RESTful API:** Efficient backend API for seamless data interaction.

## Technologies Used

### Frontend
*   **React:** A JavaScript library for building user interfaces.
*   **Axios:** Promise-based HTTP client for making API requests.
*   **CSS:** For styling the application.

### Backend
*   **FastAPI:** A modern, fast (high-performance) web framework for building APIs with Python 3.7+.
*   **SQLAlchemy:** The Python SQL Toolkit and Object Relational Mapper (ORM) that gives application developers the full power and flexibility of SQL.
*   **Pydantic:** Data validation and settings management using Python type hints.
*   **Uvicorn:** An ASGI web server for Python, used to run FastAPI applications.
*   **FastAPI-CORS:** Middleware for handling Cross-Origin Resource Sharing.

### Database
*   **SQLite:** A lightweight, file-based database (default).
*   **PostgreSQL/MySQL:** Configurable via environment variables for production use.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have the following installed:
*   **Node.js & npm/yarn:** For the React frontend.
    *   [Download Node.js](https://nodejs.org/) (includes npm)
*   **Python 3.8+ & pip:** For the FastAPI backend.
    *   [Download Python](https://www.python.org/downloads/)

### Project Structure (Recommended)

It's good practice to separate your frontend and backend code into distinct directories. Assuming the following structure:

BookCrud/
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx (or index.js)
│   ├── public/
│   ├── package.json
│   └── ... (other React files)
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── requirements.txt
│   └── .env (optional)
├── .gitignore
├── README.md
└── LICENSE


Code

### Backend Setup

1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install Python dependencies:**
    First, create a `requirements.txt` file in your `backend` directory with the following content:
    ```
    fastapi
    uvicorn[standard]
    sqlalchemy
    pydantic
    python-dotenv
    ```
    Then install them:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Database Configuration (Optional):**
    By default, the application uses a SQLite database (`books.db`) which will be created automatically. If you want to use a different database (e.g., PostgreSQL), create a `.env` file in the `backend` directory:
    ```
    DATABASE_URL="postgresql://user:password@host:port/dbname"
    ```
    Replace the placeholder with your actual database connection string.

5.  **Run the FastAPI application:**
    ```bash
    uvicorn main:app --reload
    ```
    The backend API will be running at `http://localhost:8000`.

### Frontend Setup

1.  **Navigate to the frontend directory:**
    ```bash
    cd ../frontend # If you are in the backend directory
    # Or if you just cloned:
    # cd frontend
    ```

2.  **Install Node.js dependencies:**
    ```bash
    npm install
    # or
    yarn install
    ```

3.  **Start the React development server:**
    ```bash
    npm start
    # or
    yarn start
    ```
    The frontend application will be available at `http://localhost:3000`.

## Usage

1.  Ensure both the backend (FastAPI) and frontend (React) servers are running.
2.  Open your web browser and navigate to `http://localhost:3000`.
3.  You will see a form to add new books and a table displaying existing books.
4.  Use the form to `Add New Book` by entering the title, author, and published year.
5.  Click the `Edit` button next to a book in the table to modify its details.
6.  Click the `Delete` button to remove a book entry.

## API Endpoints

The FastAPI backend provides the following endpoints:

*   **`GET /books`**: Retrieve a list of all books.
    *   Response: `[{ "id": 1, "title": "Book Title", "author": "Author Name", "published_year": 2023 }]`
*   **`GET /books/{book_id}`**: Retrieve a specific book by its ID.
    *   Example: `GET /books/1`
    *   Response: `{ "id": 1, "title": "Book Title", "author": "Author Name", "published_year": 2023 }`
*   **`POST /books`**: Create a new book.
    *   Request Body: `{ "title": "New Book", "author": "New Author", "published_year": 2024 }`
    *   Response: `{ "id": 2, "title": "New Book", "author": "New Author", "published_year": 2024 }`
*   **`PUT /books/{book_id}`**: Update an existing book.
    *   Example: `PUT /books/1`
    *   Request Body: `{ "title": "Updated Title", "author": "Updated Author", "published_year": 2023 }`
    *   Response: `{ "id": 1, "title": "Updated Title", "author": "Updated Author", "published_year": 2023 }`
*   **`DELETE /books/{book_id}`**: Delete a book.
    *   Example: `DELETE /books/1`
    *   Response: `{ "message": "Book deleted successfully" }`

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please feel free to:
1.  Fork the repository.
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

.gitignore Content

When creating your repository, you'll want to add a .gitignore file to prevent unnecessary files from being committed. Create a file named .gitignore in the root of your BookCrud directory with the following content:


Code
# Python
__pycache__/
*.pyc
.venv/
venv/
.env
*.db # To ignore the default SQLite database file

# Node
node_modules/
build/
.env.local
.env.development.local
.env.test.local
.env.production.local
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.DS_Store
