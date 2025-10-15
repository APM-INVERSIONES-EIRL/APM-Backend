from django.utils import timezone
from django.contrib.auth import get_user_model

def get_anonymous_user_instance(user_model=None):
    User = user_model or get_user_model()

    try:
        from architect.models import DocumentType
    except Exception:
        DocumentType = None

    doc_type = None
    if DocumentType is not None:
        doc_type, _ = DocumentType.objects.get_or_create(
            code="ANON",
            defaults={"name": "Anonymous / N/A"}
        )

    return User(
        username="anonymous",
        email="",
        first_name="",
        paternal_lastname="",
        maternal_lastname="",
        sex="N",
        document_type=doc_type,
        document_number="",
        is_active=True,
        is_staff=False,
        is_superuser=False,
        date_joined=timezone.now(),
    )
