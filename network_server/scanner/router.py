from fastapi import APIRouter

from .views import *

router = APIRouter()

router.add_api_route(
    path='/ping/',
    endpoint=ping_view
)

router.add_api_route(
    path='/port/',
    endpoint=port_scan_view
)

router.add_api_route(
    path='/service/',
    endpoint=service_detect_view
)

router.add_api_route(
    path='/os/',
    endpoint=os_scan_view
)
