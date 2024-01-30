import io
import json
import os
import shutil
import uuid
from datetime import datetime
from fastapi.testclient import TestClient
from app.main import app
import pytest
import unittest


class TestMetadataService(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.client = TestClient(app)
    @classmethod
    def tearDownClass(self):
        """dispose"""
    def setUp(self):
        """pre-test"""
    def tearDown(self):
        """post-test"""
    def test_health(self):
        response = self.client.get("/healthcheck")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}
    def test_get_startlist(self):
        response = self.client.get("/api/events/startlists")
        assert response.status_code == 200
        assert len(list(response.json())) > 0
    def test_post_startlist(self):
        start_list_data = {
        "id": "111",
        "eventId": "e000",
        "raceId": "r001",
        "ticketId": "t010",
        "eventTitle": "Hackney Moves",
        "raceTitle": "10k",
        "ticketTitle": "Standard Ticket",
        "createdAt": "2022-11-27T01:20:57.371Z",
        "updatedAt": "2023-01-21T11:15:51.236Z",
        "fields": [
        { "id": "firstName", "name": "First Name", "value": "Fiona" },
        { "id": "lastName", "name": "Last Name", "value": "Jones" },
        {
            "id": "emailAddress",
            "name": "Email Address",
            "value": "fiona.jones@example.com"
        },
        { "id": "gender", "name": "Gender", "value": "NON BINARY" },
        { "id": "dateOfBirth", "name": "Date of Birth", "value": "2002-04-03" },
        {
            "id": "addressLine1",
            "name": "Address (Line 1)",
            "value": "168 Main Street"
        },
        { "id": "addressLine2", "name": "Address (Line 2)", "value": "Apt 87B" },
        { "id": "addressCity", "name": "Address (City)", "value": "London" },
        {
            "id": "addressPostcode",
            "name": "Address (Postcode)",
            "value": "NW2 8EE"
        },
        {
            "id": "addressCountry",
            "name": "Address (Country)",
            "value": "United Kingdom"
        },
        { "id": "phone", "name": "Phone Number", "value": "+447708192027" },
        {
            "id": "emergencyContactName",
            "name": "Emergency Contact",
            "value": "Alice Miller"
        },
        {
            "id": "emergencyContactPhone",
            "name": "Emergency Phone",
            "value": "+447531101769"
        }
        ]
        }
        create_res = self.client.post("/api/events/startlists", data=json.dumps(start_list_data))
        assert create_res.status_code == 201

    
    