from os import getenv
from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    database=getenv('DB_NAME', 'wishlist'),
    user=getenv('DB_USER', 'wishlist'),
    password=getenv('DB_PASSWORD', None),
    host=getenv('DB_HOST', 'localhost'),
    port=getenv('DB_PORT', 5432),
)
