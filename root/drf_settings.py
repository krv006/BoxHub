REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',

}


SPECTACULAR_SETTINGS = {
    'TITLE': 'BoxHub Project',
    'DESCRIPTION': 'V1 apis',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}
