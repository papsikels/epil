from django.core.validators import MaxValueValidator
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, full_name, password=None, status='user', **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, full_name=full_name, status=status, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staff(self, username, email, full_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self.create_user(username, email, full_name, password, status='staff', **extra_fields)

    def create_superuser(self, username, email, full_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, full_name, password, status='superuser', **extra_fields)

class CustomerUser(AbstractBaseUser, PermissionsMixin):
    STATUS_CHOICES = [
        ('user', 'User'),
        ('staff', 'Staff'),
        ('superuser', 'Superuser'),
    ]

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    profile = models.ImageField(upload_to='profile/', null=True, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    birthdate = models.DateField(unique=True, null=True, blank=True)
    date_created = models.DateField(default=timezone.now)
    
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='user')

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name','email']

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='customeruser_set',
        related_query_name='user',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='customeruser_set',
        related_query_name='user',
    )


    def __str__(self):
        return self.full_name 
    def get_short_name(self):
        return self.full_name or self.email.split('@')[0]
    

class Message(models.Model):
    sender = models.ForeignKey('CustomerUser', on_delete=models.CASCADE, related_name='sent_messages', related_query_name='sent_message')
    receiver = models.ForeignKey('CustomerUser', on_delete=models.CASCADE, related_name='received_messages', related_query_name='received_message')
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.sender} to {self.receiver} - {self.timestamp}'

    
class Costume(models.Model):
    STATUS = [
        ('adult', 'Adult'),
        ('child', 'Child'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    photo1 = models.ImageField(upload_to='costume_photos/', null=True, blank=True)
    photo2 = models.ImageField(upload_to='costume_photos/', null=True, blank=True)
    photo3 = models.ImageField(upload_to='costume_photos/', null=True, blank=True)
    status = models.CharField(max_length=5, choices=STATUS)
    date_created = models.DateField(default=timezone.now)

    bookmarked_by = models.ManyToManyField(CustomerUser, through='Bookmark', related_name='bookmarks')

    def get_costume_type(self):
        return "Adult" if self.status == 'adult' else "Child"

    def is_bookmarked_by_current_user(self, user):
        return self.is_bookmarked_by_user(user)
        
    def is_bookmarked_by_user(self, user):
        return self.bookmark_set.filter(user=user).exists()

    def __str__(self):
        return f"{self.get_costume_type()} Costume: {self.name}"

class Review(models.Model):
    costume = models.ForeignKey(Costume, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(limit_value=5)])
    comment = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def get_user_name(self):
        return self.user.full_name

    def __str__(self):
        return f"Review for {self.costume.name} by {self.get_user_name()}"

    class Meta:
        unique_together = ('costume', 'user')

class Bookmark(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    costume = models.ForeignKey(Costume, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.full_name} - {self.costume.name} - {self.costume.status}"


