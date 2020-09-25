from flask import Flask, redirect, url_for
import subprocess

app = Flask(__name__, static_url_path='')


@app.route('/')
def get():
    try:
        subprocess.run("pytest --html static/report.html tests/", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        return_code = e.returncode
        return f"Tests Run did not complete successfully. Return code of process: {return_code}"
    return redirect(url_for('static', filename='report.html'))


