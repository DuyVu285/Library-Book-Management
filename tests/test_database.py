import pytest
from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.exc import OperationalError
from config import DATABASE_URL

TEST_DATABASE_URL = DATABASE_URL
test_engine = create_engine(TEST_DATABASE_URL)


# Fixture for setting up and tearing down the test database
@pytest.fixture(scope="function")
def db_session():
    SQLModel.metadata.create_all(test_engine)
    with Session(test_engine) as session:
        yield session
    SQLModel.metadata.drop_all(test_engine)


# Test for checking the database connection
def test_connection():
    try:
        # Use the existing test_engine instead of creating a new engine
        with test_engine.connect() as connection:
            assert connection is not None, "Connection failed"
            print("Database connection successful!")
    except OperationalError as e:
        pytest.fail(f"Database connection failed: {e}")
