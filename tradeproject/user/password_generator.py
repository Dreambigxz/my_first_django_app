import uuid


def forgot_password_generator():
    return (uuid.uuid4().hex[:6])
