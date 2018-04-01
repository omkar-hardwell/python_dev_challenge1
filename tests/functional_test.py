"""Tests for Routes."""
import json
from unittest.mock import MagicMock
from unittest.mock import patch

from oto import response
from oto import status as http_status

from src import app


def test_get_product_live_time_detail_success(monkeypatch):
    """Test get product live time with valid product id."""
    expected_response = {
        "from": "test@test.com",
        "to": "test@test.com",
        "cc": "test@test.com",
        "subject": "MSG Test File",
        "date": "",
        "attachments": [],
        "body": "Test message"}

    monkeypatch.setattr(
        app, 'upload',
        MagicMock(return_value=response.Response(message=expected_response)))

    with app.test_client() as client:
        result = client.post(
            '/product', data=json.dumps(expected_response))
        message = json.loads(result.data.decode())

        assert result.status_code == http_status.OK
        assert message == expected_response
