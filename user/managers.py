from django.contrib.auth.base_user import BaseUserManager

# Create your Manager here.

class UserManger(BaseUserManager):
    def _create_user(self, email,password, **extra_fields):
        if not email:
            raise ValueError('An email is required')
        if not password:
            raise ValueError('A password is required')
        
        email = self.normalize_email(email)
        email = email.lower()
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        
        return user
        
    def create_user(self, email,password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', False)
        
        return self._create_user(email,password,**extra_fields)
        
    def create_superuser(self, email,password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        
        return self._create_user(email,password,**extra_fields)