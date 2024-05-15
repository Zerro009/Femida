#!/usr/bin/env  python

from fastapi import FastAPI

from scanner.router import router as scanner
from startup import *

import os

app = FastAPI()

app.include_router(scanner, prefix='/scanner')

if os.geteuid() != 0:
    print('This service requires root privileges!')
    exit(1)

startup(app)
