#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask_login import login_required

app = Flask(__name__, template_folder='../templates')
app.config.from_object('config.Local')

from auth import *
from routings import *