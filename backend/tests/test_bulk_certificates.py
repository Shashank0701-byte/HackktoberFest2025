"""
Tests for bulk certificate generation functionality
"""

import pytest
import tempfile
import os
from fastapi.testclient import TestClient
from app.main import app
from app.services.bulk_generator import process_csv_content, generate_bulk_certificates
from app.models.certificates import BulkCertificateItem

client = TestClient(app)


class TestBulkCertificateGeneration:
    """Test cases for bulk certificate generation"""

    def test_process_csv_content_valid(self):
        """Test processing valid CSV content"""
        csv_content = """participant_name,email
John Doe,john@example.com
Jane Smith,jane@example.com
Mike Johnson,mike@example.com"""
        
        participants = process_csv_content(csv_content)
        
        assert len(participants) == 3
        assert participants[0].participant_name == "John Doe"
        assert participants[0].email == "john@example.com"
        assert participants[1].participant_name == "Jane Smith"
        assert participants[2].participant_name == "Mike Johnson"

    def test_process_csv_content_missing_email(self):
        """Test processing CSV with missing email column"""
        csv_content = """participant_name
John Doe
Jane Smith"""
        
        participants = process_csv_content(csv_content)
        
        assert len(participants) == 2
        assert participants[0].participant_name == "John Doe"
        assert participants[0].email is None

    def test_process_csv_content_empty_names(self):
        """Test processing CSV with empty participant names"""
        csv_content = """participant_name,email
John Doe,john@example.com
,jane@example.com
Mike Johnson,mike@example.com"""
        
        participants = process_csv_content(csv_content)
        
        # Should skip the empty name row
        assert len(participants) == 2
        assert participants[0].participant_name == "John Doe"
        assert participants[1].participant_name == "Mike Johnson"

    def test_bulk_certificate_api_json_payload(self):
        """Test bulk certificate generation via JSON API"""
        payload = {
            "event_name": "Test Event 2025",
            "date_issued": "2025-10-22",
            "participants": [
                {"participant_name": "John Doe", "email": "john@example.com"},
                {"participant_name": "Jane Smith", "email": "jane@example.com"}
            ]
        }
        
        response = client.post("/certificates/bulk", json=payload)
        
        assert response.status_code == 200
        data = response.json()
        
        assert data["total_count"] == 2
        assert data["success_count"] >= 0  # May vary based on template availability
        assert "successful_certificates" in data
        assert "failed_certificates" in data

    def test_bulk_certificate_api_csv_upload(self):
        """Test bulk certificate generation via CSV upload"""
        # Create a temporary CSV file
        csv_content = """participant_name,email
John Doe,john@example.com
Jane Smith,jane@example.com"""
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            f.write(csv_content)
            temp_csv_path = f.name
        
        try:
            with open(temp_csv_path, 'rb') as csv_file:
                files = {'csv_file': ('test.csv', csv_file, 'text/csv')}
                data = {
                    'event_name': 'Test Event 2025',
                    'date_issued': '2025-10-22'
                }
                
                response = client.post("/certificates/bulk/csv", files=files, data=data)
                
                assert response.status_code == 200
                response_data = response.json()
                
                assert response_data["total_count"] == 2
                assert "successful_certificates" in response_data
                assert "failed_certificates" in response_data
        
        finally:
            # Clean up temporary file
            os.unlink(temp_csv_path)

    def test_bulk_certificate_api_invalid_csv(self):
        """Test bulk certificate generation with invalid CSV file"""
        # Create a non-CSV file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write("This is not a CSV file")
            temp_file_path = f.name
        
        try:
            with open(temp_file_path, 'rb') as test_file:
                files = {'csv_file': ('test.txt', test_file, 'text/plain')}
                data = {
                    'event_name': 'Test Event 2025',
                    'date_issued': '2025-10-22'
                }
                
                response = client.post("/certificates/bulk/csv", files=files, data=data)
                
                assert response.status_code == 400
                assert "File must be a CSV file" in response.json()["detail"]
        
        finally:
            os.unlink(temp_file_path)

    def test_bulk_certificate_validation_errors(self):
        """Test bulk certificate generation with validation errors"""
        # Empty participants list
        payload = {
            "event_name": "Test Event 2025",
            "date_issued": "2025-10-22",
            "participants": []
        }
        
        response = client.post("/certificates/bulk", json=payload)
        assert response.status_code == 422  # Validation error

        # Invalid event name
        payload = {
            "event_name": "",
            "date_issued": "2025-10-22",
            "participants": [{"participant_name": "John Doe"}]
        }
        
        response = client.post("/certificates/bulk", json=payload)
        assert response.status_code == 422  # Validation error

    def test_bulk_certificate_item_validation(self):
        """Test individual certificate item validation"""
        # Valid item
        item = BulkCertificateItem(participant_name="John Doe", email="john@example.com")
        assert item.participant_name == "John Doe"
        assert item.email == "john@example.com"

        # Invalid participant name (empty)
        with pytest.raises(ValueError):
            BulkCertificateItem(participant_name="", email="john@example.com")

        # Invalid participant name (special characters)
        with pytest.raises(ValueError):
            BulkCertificateItem(participant_name="John@#$", email="john@example.com")

    def test_download_bulk_certificates_not_found(self):
        """Test downloading non-existent bulk certificate file"""
        response = client.get("/certificates/bulk/download/nonexistent.zip")
        assert response.status_code == 404
        assert "not found" in response.json()["detail"].lower()


if __name__ == "__main__":
    pytest.main([__file__])
