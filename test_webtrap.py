import json
import unittest
import app


class WebTrapResponseTest(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

    def test_get_without_param(self):
        response = self.app.get("/api")
        status = json.loads(str(response.status_code))
        self.assertEqual(status, 200)

    def test_get_invalid(self):
        response = self.app.get("/api?invalid=1")
        status = json.loads(str(response.status_code))
        self.assertEqual(status, 200)

    def test_get_invalid_2(self):
        response = self.app.get("/api?invalid=2")
        status = json.loads(str(response.status_code))
        self.assertEqual(status, 200)

    def test_get_notawaiting(self):
        response = self.app.get("/api?notawaiting=1")
        status = json.loads(str(response.status_code))
        self.assertEqual(status, 400)

    def test_get_invalid_notawaiting(self):
        response = self.app.get("/api?invalid=1&notawaiting=1")
        status = json.loads(str(response.status_code))
        self.assertEqual(status, 400)

    def test_post(self):
        response = self.app.post("/api")
        status = json.loads(str(response.status_code))
        self.assertEqual(status, 200)

    def test_put(self):
        response = self.app.put("/api")
        status = json.loads(str(response.status_code))
        self.assertEqual(status, 200)

    def test_delete(self):
        response = self.app.delete("/api")
        status = json.loads(str(response.status_code))
        self.assertEqual(status, 200)

    def test_patch(self):
        response = self.app.patch("/api")
        status = json.loads(str(response.status_code))
        self.assertEqual(status, 200)









