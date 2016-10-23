from flask import Flask, render_template, request, redirect, session, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy import func
# from model import connect_to_db, db, Instructor, Testimonial, InstTest
from jinja2 import StrictUndefined

app = Flask(__name__)