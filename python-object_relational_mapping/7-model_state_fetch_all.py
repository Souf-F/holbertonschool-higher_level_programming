#!/usr/bin/python3
"""
Script that lists all State objects from the database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Main function."""
    if len(sys.argv) != 4:
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f'mysql+pymysql://{username}:{password}@localhost:3306/{database}',
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == "__main__":
    main()
