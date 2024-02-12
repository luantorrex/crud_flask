
def test_app_is_created(app):
    assert app.name == 'app'

def test_debug_is_false(app):
    assert app.config['DEBUG'] is False
