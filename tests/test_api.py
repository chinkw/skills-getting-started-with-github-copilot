import copy
import importlib
from urllib.parse import quote

import pytest
from fastapi.testclient import TestClient


@pytest.fixture(autouse=True)
def snapshot_activities():
    """Snapshot and restore the in-memory activities dict around each test."""
    app_mod = importlib.import_module("src.app")
    original = copy.deepcopy(app_mod.activities)
    yield app_mod
    app_mod.activities.clear()
    app_mod.activities.update(original)


def client_for(mod):
    return TestClient(mod.app)


def encode_activity(name: str) -> str:
    return quote(name, safe='')


def test_get_activities(snapshot_activities):
    mod = snapshot_activities
    client = client_for(mod)
    resp = client.get("/activities")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data


def test_signup_success(snapshot_activities):
    mod = snapshot_activities
    client = client_for(mod)
    activity = "Chess Club"
    email = "newstudent@mergington.edu"
    url = f"/activities/{encode_activity(activity)}/signup"
    resp = client.post(url, params={"email": email})
    assert resp.status_code == 200
    assert email in mod.activities[activity]["participants"]
    assert "Signed up" in resp.json().get("message", "")


def test_signup_duplicate(snapshot_activities):
    mod = snapshot_activities
    client = client_for(mod)
    activity = "Chess Club"
    email = "michael@mergington.edu"
    url = f"/activities/{encode_activity(activity)}/signup"
    resp = client.post(url, params={"email": email})
    assert resp.status_code == 400
    assert resp.json().get("detail") == "Student is already signed up for this activity"


def test_signup_capacity(snapshot_activities):
    mod = snapshot_activities
    client = client_for(mod)
    activity = "Art Workshop"
    max_p = mod.activities[activity]["max_participants"]
    # Fill to capacity
    mod.activities[activity]["participants"] = [f"user{i}@example.com" for i in range(max_p)]
    url = f"/activities/{encode_activity(activity)}/signup"
    resp = client.post(url, params={"email": "extra@mergington.edu"})
    assert resp.status_code == 400
    assert resp.json().get("detail") == "Activity is full"


def test_unregister(snapshot_activities):
    mod = snapshot_activities
    client = client_for(mod)
    activity = "Chess Club"
    email = "michael@mergington.edu"
    assert email in mod.activities[activity]["participants"]
    url = f"/activities/{encode_activity(activity)}/signup"
    resp = client.delete(url, params={"email": email})
    assert resp.status_code == 200
    assert email not in mod.activities[activity]["participants"]
    assert "Unregistered" in resp.json().get("message", "")
