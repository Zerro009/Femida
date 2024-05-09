from fastapi import APIRouter

from .views import *

router = APIRouter()

router.add_api_route(
    path='/ping/',
    endpoint=ping
)
