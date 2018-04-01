"""Application.

The API application is a `flask` application.
"""
import os
import email.parser
import shutil
from service import process_msg_file

from flask import Flask, request, render_template


__author__ = 'omkar'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload():
    """
    # this is to verify that folder to upload to exists.
    if os.path.isdir(os.path.join(APP_ROOT, 'files/{}'.format(folder_name))):
        print("folder exist")
    """
    folder_name = 'uploads'
    if request.form['submit']:
        target = os.path.join(APP_ROOT, format(folder_name))
        print(target)

        if not os.path.isdir(target):
            os.mkdir(target)
        print(request.files.getlist("file"))
        for upload in request.files.getlist("file"):
            print(upload)
            print("{} is the file name".format(upload.filename))
            filename = upload.filename
            # This is to verify files are supported
            ext = os.path.splitext(filename)[1]
            if ext.lower() == ".msg":
                print("File supported moving on...")
            else:
                render_template("error.html",
                                message="Files uploaded are not supported...")
            destination = "/".join([target, filename])
            print("Accept incoming file:", filename)
            print("Save it to:", destination)
            upload.save(destination)

            msg = process_msg_file.Message(destination)
            email_data = msg.save(True, False)
            print(email_data)

            source_path = "/".join([APP_ROOT, email_data['attachments_path']])
            dest_path = "/".join([APP_ROOT, 'static'])
            for filename in os.listdir(source_path):
                attachment = "/".join([source_path, filename])
                shutil.copy2(attachment, dest_path)

            shutil.rmtree(source_path)

    return render_template("complete.html", message=msg.save(True, False))


if __name__ == "__main__":
    app.run(port=5000, debug=True)
