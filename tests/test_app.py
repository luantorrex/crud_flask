def test_app_is_created(app):
    assert app.name == 'app'

def test_debug_is_false(app):
    assert app.config['DEBUG'] is False

def test_404(client):
    assert client.get("/page_that_doesnt_exists").status_code == 404
