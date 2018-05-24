# coding=utf-8

from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import ValidationError
from werkzeug import secure_filename


app = Flask(__name__)

app.config['WTF_CSRF_ENABLED'] = False


class UploadImageForm(FlaskForm):
    image = FileField('图片', validators=[
        FileRequired(message='请上传图片'),
        FileAllowed(['gif', 'png', 'jpg', 'jpeg'],
                    '上传失败，图片类型只能是 gif, png, jpg, jpeg')
    ])

    def validate_image(self, field):
        filename = secure_filename(field.data.filename)
        field.data.filename = filename
        size = field.data.content_length
        print(dir(field.data))
        print(size)
        if size > 2:
            raise ValidationError('图片大小不能超过 5M')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    form = UploadImageForm()
    if form.validate_on_submit():
        print(form.image.data)
        fd = request.files['image']
        print(fd.content_length)
        return 'hello world'
    return jsonify(form.errors)


if __name__ == '__main__':
    app.run(debug=True)
