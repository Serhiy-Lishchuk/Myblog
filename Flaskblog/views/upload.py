import os
from flask import redirect, render_template, request, url_for
from Flaskblog.config.config import (IMAGE_EXTENSIONS, MAX_WIDTH, MUSIC_EXTENSIONS,
                                     UPLOAD_MUSIC, UPLOAD_IMAGE, WATERMARK)
from PIL import Image
from werkzeug import secure_filename


def allowed_music(filename):
    """
    Checking if files are in allowed list
    """
    return '.' in filename and filename.rsplit('.', 1)[1] in MUSIC_EXTENSIONS


def allowed_image(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in IMAGE_EXTENSIONS


def upload():
    """
    Upload media files, resizing image add watermark
    """
    if request.method == 'POST':
        upload_file = request.files['file']
        if upload_file and allowed_music(upload_file.filename):
            file_music = secure_filename(upload_file.filename)
            upload_file.save(os.path.join(UPLOAD_MUSIC, file_music))
            return redirect(url_for('show_entries'))
        elif upload_file and allowed_image(upload_file.filename):
            file_image = secure_filename(upload_file.filename)
            upload_file.save(os.path.join(UPLOAD_IMAGE, file_image))
            img = Image.open(os.path.join(UPLOAD_IMAGE, file_image))
            if img.size[0] > MAX_WIDTH:
                width_image = (MAX_WIDTH / float(img.size[0]))
                height_image = int(float(img.size[1] * width_image))
                res_image = img.resize((MAX_WIDTH, height_image), Image.ANTIALIAS)
                water_image = Image.open(WATERMARK)
                res_image.paste(water_image, (250, -100), water_image)
                res_image.save(os.path.join(UPLOAD_IMAGE, file_image))
            return redirect(url_for('show_entries'))
    return render_template('home.html')
