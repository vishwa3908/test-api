from flask import request
from app import app

class Test:

    tester = app.test_client()

    def test_1_get(self):
        response = self.tester.get("/")
        assert response.content_type=="application/json"
        response_data = response.json
        assert response_data=="welcome to test-api"
        assert response.status_code==200

    def test_2_post(self):
        data = {
            "member":"samuel",
            "role":"guest"
        }
        response = self.tester.post("/team",json=data)
        assert response.status_code==201
        assert response.content_type=="application/json"