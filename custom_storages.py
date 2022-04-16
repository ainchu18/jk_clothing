from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """Setting for Boto3/s3 static storage"""
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """Setting for Boto3/s3 media storage"""
    location = settings.MEDIAFILES_LOCATION
