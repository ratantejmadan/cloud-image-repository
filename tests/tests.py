# import os
# import tempfile
#
# import pytest
#
# import app
# from app import login
#
#
# def login(client, username, password):
#     return client.post('/login', data=dict(
#         username=username,
#         password=password
#     ), follow_redirects=True)
#
#
# def logout(client):
#     return client.get('/logout', follow_redirects=True)
#
#
# def test_login():
#     username = app.config["username"]
#     password = app.confif[""]
