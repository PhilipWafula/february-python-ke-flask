def test_create_user(create_user):
    user = create_user()

    assert user.first_name == 'Test'
    assert user.last_name == 'User'
