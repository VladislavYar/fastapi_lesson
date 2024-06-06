__all__ = (
    "calc_router",
    "users_router",
    "permissions_router",
)

from views.calc.views import router as calc_router
from views.users.views import router as users_router
from views.permissions.views import router as permissions_router
