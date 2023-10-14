"""CRUD operations."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from model import db, connect_to_db

