from datetime import date

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models

# Custom validator for Indian phone numbers
indian_phone_validator = RegexValidator(
    regex=r'^\+?1?\d{10}$',
    message="Phone number must be a valid Indian phone number."
)


# Custom DOB Validator
def validate_age_range(date_of_birth):
    today = date.today()
    age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    if age < 18 or age > 99:
        raise ValidationError("Age should be between 18 and 99 years.")


# Choices for Policy Status
POLICY_STATUS_CHOICES = [
    ('Requirements Awaited', 'Requirements Awaited'),
    ('Requirements Closed', 'Requirements Closed'),
    ('Underwriting', 'Underwriting'),
    ('Policy Issued', 'Policy Issued'),
    ('Policy Rejected', 'Policy Rejected'),
]

# Choices for Medical Type (MaxLife & HDFC Life)
MEDICAL_TYPE_CHOICES = [
    ('Tele Medicals', 'Tele Medicals'),
    ('Physical Medicals', 'Physical Medicals'),
]

# Choices for Medicals Status (MaxLife & HDFC Life)
MEDICALS_STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Scheduled', 'Scheduled'),
    ('Waiting for Report', 'Waiting for Report'),
    ('Done', 'Done'),
]


class Policy(models.Model):
    application_number = models.CharField(max_length=50, unique=True)
    customer_name = models.CharField(max_length=100)
    email = models.EmailField(blank=False, null=False)
    phone_number = models.CharField(max_length=15, validators=[indian_phone_validator])
    date_of_birth = models.DateField(validators=[validate_age_range])
    policy_cover = models.DecimalField(
        max_digits=10, decimal_places=2,
        validators=[MinValueValidator(25), MaxValueValidator(50000000)]
    )
    policy_status = models.CharField(max_length=20, choices=POLICY_STATUS_CHOICES)
    policy_number = models.CharField(max_length=50, blank=True)
    medical_type = models.CharField(max_length=20, choices=MEDICAL_TYPE_CHOICES, blank=True)
    medicals_status = models.CharField(max_length=20, choices=MEDICALS_STATUS_CHOICES, blank=True)
    remarks = models.TextField(max_length=200, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.policy_status == 'Policy Issued' and not self.policy_number:
            raise ValidationError("Policy number is required when status is 'Policy Issued'.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.application_number

    class Meta:
        verbose_name_plural = "Policies"
