from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError, ProgrammingError

# Database connection
url = URL.create(drivername="postgresql", username="postgres", password="Supreeth@1",
                 host="localhost", database="my_db1", port=5432)

# Create a database engine
engine = create_engine(url)

# Create a base class for declarative models
Base = declarative_base()


# Define a model for your table
class StudentRegistration(Base):
    __tablename__ = 'student_registration'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)


# Function to create table if it doesn't exist
def create_table_if_not_exists():
    try:
        Base.metadata.create_all(engine)
    except ProgrammingError:
        pass


# Create a session
Session = sessionmaker(bind=engine)
session = Session()


# Function to check if the username exists
def check_username(session, username):
    return session.query(StudentRegistration).filter_by(username=username).first() is not None


# Function to check if the email exists
def check_email(session, email):
    return session.query(StudentRegistration).filter_by(email=email).first() is not None


# Function to check password whether requirements are met
def password_complexity(password):
    if len(password) < 8:
        return False
    digit_check = any(char.isdigit() for char in password)
    special_char_check = any(char in "!@#$%^&*()+_-{}[]<>?/" for char in password)
    return digit_check and special_char_check


# Inserting data into records
while True:
    create_table_if_not_exists()

    while True:
        username = input("Enter Username: ")
        if check_username(session, username):
            print(f"Username '{username}' already exists")
        else:
            break

    while True:
        email = input("Enter email: ")
        if check_email(session, email):
            print(f"Email '{email}' already exists. Please enter a different email.")
        else:
            break

    while True:
        password = input("Enter password: ")
        if not password_complexity(password):
            print("Password doesn't meet requirement. Please choose a different password")
        else:
            break

    try:
        new_record = StudentRegistration(username=username, email=email, password=password)
        session.add(new_record)
        session.commit()
        print(f"Record inserted successfully")
    except IntegrityError as e:
        print("Error inserting record", e)
        session.rollback()

    more_records = input("Do you want to insert more records? (y/n):")
    if more_records.lower() != 'y':
        break

# Close the session
session.close()
