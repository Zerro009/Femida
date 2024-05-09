#!/usr/bin/env  python

from fastapi import FastAPI

from scanner.router import router as scanner

import os

app = FastAPI()

app.include_router(scanner, prefix='/scanner')

if __name__ == '__main__':
    if os.geteuid() != 0:
        print('This service requires root privileges!')
        exit(1)
