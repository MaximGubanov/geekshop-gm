from locust import HttpUser, TaskSet, task


def login(l):
    l.client.post("/auth/login", {"username": "admin", "password": "admin"})


def logout(l):
    l.client.post("/auth/logout", {"username": "admin", "password": "admin"})


def index(l):
    l.client.get("/")


def profile(l):
    l.client.get("/products/")

@task
class UserBehavior(TaskSet):
    tasks = {index: 2, profile: 1}


@task
class WebsiteUser(HttpUser):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000