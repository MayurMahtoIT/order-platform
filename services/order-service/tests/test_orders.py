VALID = {"customer_id": "c1", "product_id": "p1", "quantity": 2, "total_amount": 99.5}


def test_create_order(client):
    r = client.post("/orders", json=VALID)
    assert r.status_code == 201
    body = r.json()
    assert body["status"] == "PENDING"
    assert body["quantity"] == 2


def test_get_order(client):
    order_id = client.post("/orders", json=VALID).json()["id"]
    r = client.get(f"/orders/{order_id}")
    assert r.status_code == 200
    assert r.json()["id"] == order_id


def test_get_missing_order_404(client):
    assert client.get("/orders/does-not-exist").status_code == 404


def test_invalid_quantity_rejected(client):
    r = client.post("/orders", json={**VALID, "quantity": 0})
    assert r.status_code == 422


def test_liveness(client):
    assert client.get("/health/live").json() == {"status": "ok"}
