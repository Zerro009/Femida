from fastapi import APIRouter

from .views import *

router = APIRouter()

router.add_api_route(
    path='/ping/',
    endpoint=ping_view
)

router.add_api_route(
    path='/tcp/scan/',
    endpoint=tcp_scan_view
)

router.add_api_route(
    path='/os/scan/',
    endpoint=os_scan_view
)
