from typing import TYPE_CHECKING, Optional

from django.contrib.auth.models import BaseUserManager

if TYPE_CHECKING:
    from user.models import User


class UsersManager(BaseUserManager):
    def create_user(
        self, email: str, password: Optional[str] = None, **extra_fields
    ) -> "User":
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.is_active = True
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self, email: str, password: Optional[str] = None, **extra_fields
    ) -> "User":
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is False:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)


