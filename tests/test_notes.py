import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from model_bakery import baker
from rest_framework.test import APIClient

from notes.models import Note


@pytest.mark.django_db
def test_list_notes():
    note = baker.make(Note, text="from test")

    client = APIClient()

    response = client.get('/api/notes/')
    assert response.status_code == 200
    data = response.json()
    assert data[0]['text'] == 'from test'
