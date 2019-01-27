from os import environ
from flask import Flask

app = Flask(bot)
app.run(environ.get('PORT'))