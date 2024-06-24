from django.db import models
import random
import string

def generate_string(length=12):
    """Generate a strong password."""
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits

    # Combine character sets
    all_characters = lowercase_letters + uppercase_letters + digits

    # Ensure at least one character from each set
    password = random.choice(lowercase_letters)
    password += random.choice(uppercase_letters)
    password += random.choice(digits)

    # Fill remaining length with random characters
    for _ in range(length - 4):
        password += random.choice(all_characters)

    # Shuffle the password to make it more random
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password


# Create your models here.
class Media(models.Model):
    document = models.FileField(upload_to="documents/", blank=True)
    slug = models.CharField(max_length=20, default=None, null=True, unique=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            g = generate_string()
            slug_list = [s.slug for s in Media.objects.all()]
            while g in slug_list:
                g = generate_string()
            self.slug = g
        super().save(*args, **kwargs)
    def document_name(self):
        return self.document.name.split('/')[-1]
