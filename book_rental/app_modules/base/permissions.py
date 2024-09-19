from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
User = get_user_model()


class AdminLoginRequiredMixin(LoginRequiredMixin):
    def has_permission(self):
        """
        Override this method to customize the way permissions are checked.
        """
        return True if (self.request.user.role in [User.SUPER_ADMIN, User.ADMIN]) else False

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not self.has_permission():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)