
<h2>Book Rental System</h2>

This system is an open-source web application designed to empower librarian and individual organizations to efficiently manage their books.


### Key Features

- **Rent Book:** Easily record and rent a book to the registered students. Students can rent a book for one month without any charge. If they desire to keep the book beyond the initial month, they are
charged a fee determined by the book's page count divided by 100. For instance, if a
book has 300 pages, the fee would be $3.00 for every subsequent month.

- **Register new student:** To borrow a book student have to register himself in the system undertaken of admin.

- **View list of rented books:** Admin can view list of books rented by a perticular student and other details also.

### Installation

1. Clone the repository.
    - `git clone https://github.com/Anuj411/book-rental-system.git`
2. Create a new virtual environment in project directory.
    - `virtualenv venv`
3. Activate virtual venv and install requirements.
    - `pip install -r requirements/local.txt`
4. Create .env file from .env.example file and set database configurations.
5. Run seed command.
    - `python manage.py seed`
6. Now, start the django server.
    - `python manage.py runserver`
7. You can login with admin credentials provided in .env file.
