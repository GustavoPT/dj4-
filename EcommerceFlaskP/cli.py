import click
from flask import Flask
from flask.cli import AppGroup
from app import app
from models import *

cli = AppGroup('custom')

@cli.command('create-db')
def create_db():
    """Create the database."""
    db.create_all()
    print("Database created.")

@cli.command('drop-db')
def drop_db():
    """Drop the database."""
    db.drop_all()
    print("Database dropped.")

app.cli.add_command(cli)
