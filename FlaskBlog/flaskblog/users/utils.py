import os
import secrets
from PIL import Image
from flask import current_app
from flask_login import current_user

def save_picture(form_picture):
    rand_hex = secrets.token_hex(8)
    _, ext = os.path.splitext(form_picture.filename)
    file_name = rand_hex + ext
    file_path = os.path.join(current_app.root_path, 'static/profile_pics', file_name)
    
    # Resize image before saving
    i = Image.open(form_picture)
    i.thumbnail((125, 125))
    i.save(file_path)

    # Delete prev profile pic
    if current_user.image_file != 'default.jpg':
        prev_picture = os.path.join(current_app.root_path, 'static/profile_pics', current_user.image_file)
        if os.path.exists(prev_picture):
            os.remove(prev_picture)
        
    return file_name