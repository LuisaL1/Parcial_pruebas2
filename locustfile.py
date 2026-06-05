from locust import HttpUser, task, between


class QuickUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def recarga(self):
        payload = {"monto": 1000, "premium": False}
        self.client.post("/recarga", json=payload)
