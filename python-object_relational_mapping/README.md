# Python - Object-Relational Mapping (ORM) Project

## Overview

This project bridges two worlds: **Databases and Python**. It demonstrates how to interact with MySQL databases using both direct SQL queries (MySQLdb) and an Object-Relational Mapper (SQLAlchemy).

The key difference: with ORM, you write Python code instead of SQL queries, making your code more maintainable and database-agnostic.

---

## Part 1: MySQLdb (Direct SQL Queries)

### What I Learned

- Connecting to MySQL from Python scripts
- Executing SELECT, INSERT, UPDATE, DELETE queries
- Handling database connections and cursors
- The dangers of SQL injection attacks
- How to protect against SQL injection using prepared statements

### Technologies Used

- **MySQLdb 2.0.3** - MySQL connector for Python
- **MySQL 8.0** - Database server
- Python's `sys` module for command-line arguments

### Tasks Completed

1. **0-select_states.py** - List all states from database
   - Connect to MySQL
   - Execute SELECT query
   - Display results as tuples

2. **1-filter_states.py** - Filter states starting with 'N'
   - Use WHERE clause with LIKE operator
   - Filter hardcoded pattern

3. **2-my_filter_states.py** - Filter by user input
   - Accept state name as command-line argument
   - Use `.format()` to build SQL query
   - **VULNERABLE to SQL injection!**

4. **3-my_safe_filter_states.py** - Safe filtering
   - Use prepared statements with `%s` placeholders
   - Pass parameters as tuple to `execute()`
   - Protected against SQL injection

5. **4-cities_by_state.py** - List all cities with states
   - Use JOIN to combine two tables
   - Display format: `(city_id, 'city_name', 'state_name')`

6. **5-filter_cities.py** - Filter cities by state name
   - Accept state name as argument
   - Use JOIN with WHERE clause
   - Display cities as comma-separated list

### Key Concepts

- **SQL Injection**: Malicious input can execute unintended SQL commands
- **Prepared Statements**: Safe way to insert user input into queries
- **JOINs**: Combine data from multiple tables
- **Cursor**: Tool to execute queries and fetch results
- **Session Management**: Proper opening and closing of connections

---

## Part 2: SQLAlchemy (ORM)

### What I Learned

- Mapping Python classes to database tables
- Using ORM to avoid writing SQL queries
- Creating relationships between tables
- Performing CRUD operations with objects instead of SQL
- How to query, insert, update, and delete using ORM syntax

### Technologies Used

- **SQLAlchemy 1.4.22** - Python ORM library
- **model_state.py** - Base State class definition
- **model_city.py** - Base City class definition
- Python's `sessionmaker` for database sessions

### Core Concepts

#### 1. Model Definition (Classes)

```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
```

- Classes inherit from `Base`
- `__tablename__` maps to database table
- Attributes are columns with data types
- No SQL required - just Python!

#### 2. Database Connection

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://user:pass@localhost/db_name')
Session = sessionmaker(bind=engine)
session = Session()
```

#### 3. CRUD Operations

**CREATE** - Add new record:
```python
new_state = State(name='Louisiana')
session.add(new_state)
session.commit()
```

**READ** - Fetch records:
```python
states = session.query(State).all()
state = session.query(State).filter(State.id == 2).first()
```

**UPDATE** - Modify record:
```python
state = session.query(State).filter(State.id == 2).first()
state.name = "New Mexico"
session.commit()
```

**DELETE** - Remove records:
```python
states = session.query(State).filter(State.name.contains('a')).all()
for state in states:
    session.delete(state)
session.commit()
```

### Tasks Completed

7. **7-model_state_fetch_all.py** - List all states
   - Query all State objects
   - Order by id
   - Display as "id: name"

8. **8-model_state_fetch_by_id.py** - Get state by ID
   - Query with filter condition
   - Handle if not found

9. **9-model_state_filter_asc.py** - List states with 'a' in name
   - Use `.contains()` method
   - Order by id ascending

10. **10-model_state_my_get.py** - Find state by name
    - Accept state name as argument
    - Use `.filter()` with equality check

11. **11-model_state_insert.py** - Add new state
    - Create State object
    - Add to session
    - Print new id

12. **12-model_state_update_id_2.py** - Update state
    - Find state by id
    - Modify attribute
    - Commit changes

13. **13-model_state_delete_a.py** - Delete states with 'a'
    - Find all states containing 'a'
    - Delete each one
    - Commit all deletions

14. **14-model_city_fetch_by_state.py** - List cities with states
    - Use relationships between State and City
    - Join data from both tables
    - Display format: "state_name: (city_id) city_name"

---

## Key Advantages of ORM

1. **No SQL** - Write Python instead of database-specific SQL
2. **Database Agnostic** - Switch databases without code changes
3. **Type Safe** - Catch errors at Python level, not database level
4. **Relationships** - Handle table relationships naturally
5. **Less Code** - Cleaner, more readable code

---

## Requirements

- Python 3.8.5
- MySQLdb 2.0.x
- SQLAlchemy 1.4.x
- MySQL 8.0
- Pycodestyle 2.7.*

---

## Installation

```bash
pip install mysqlclient==2.0.3 --break-system-packages
pip install SQLAlchemy==1.4.22 --break-system-packages
```

---

## File Structure

```
python-object_relational_mapping/
├── README.md                           # This file
├── model_state.py                      # State class definition
├── model_city.py                       # City class definition
├── 0-select_states.py                  # MySQLdb: Basic SELECT
├── 1-filter_states.py                  # MySQLdb: WHERE clause
├── 2-my_filter_states.py               # MySQLdb: User input (unsafe)
├── 3-my_safe_filter_states.py          # MySQLdb: Safe prepared statements
├── 4-cities_by_state.py                # MySQLdb: JOIN queries
├── 5-filter_cities.py                  # MySQLdb: JOIN with filter
├── 7-model_state_fetch_all.py          # ORM: Fetch all
├── 8-model_state_fetch_by_id.py        # ORM: Fetch by id
├── 9-model_state_filter_asc.py         # ORM: Filter with contains
├── 10-model_state_my_get.py            # ORM: Get by name
├── 11-model_state_insert.py            # ORM: Insert new
├── 12-model_state_update_id_2.py       # ORM: Update
├── 13-model_state_delete_a.py          # ORM: Delete
└── 14-model_city_fetch_by_state.py     # ORM: Relationships
```

---

## Key Takeaways

### MySQLdb (Part 1)

- Direct SQL gives full control but requires SQL knowledge
- Always use prepared statements for user input
- Proper connection management is essential
- JOINs allow combining data from multiple tables

### SQLAlchemy (Part 2)

- ORM abstracts database operations into Python objects
- Classes define tables, attributes define columns
- Sessions manage database transactions
- Relationships between tables are defined in model classes
- Query API is intuitive and Pythonic

---

## What's the Difference?

**Without ORM (MySQLdb):**
```python
cur.execute("SELECT * FROM states WHERE name = %s", (name,))
results = cur.fetchall()
for row in results:
    print(row)  # Tuple: (1, 'California')
```

**With ORM (SQLAlchemy):**
```python
states = session.query(State).filter(State.name == name).all()
for state in states:
    print(f"{state.id}: {state.name}")  # Object: State(id=1, name='California')
```

The ORM version is cleaner, more readable, and doesn't require SQL knowledge!

---

## Author

Developed as part of Holberton School's Python curriculum to understand database interactions in Python.

---
