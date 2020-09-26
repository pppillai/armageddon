from flask import Flask, redirect, url_for, render_template, flash
from markupsafe import escape
import subprocess
import time
import os


app = Flask(__name__, static_url_path='')
app.secret_key = b'Thisissecret..out..secret..._5#y2L"F4Q8z\n\xec]/'

@app.route('/all_reports/')
def reports():
    links = []
    try:
        for name in os.scandir('static'):
            if name.is_file():
                if name.name.endswith('html'):
                    links.append(url_for('static', filename=name.name))
    except FileNotFoundError:
        pass
    return render_template('reports.html', links=links)


@app.route('/tests/')
def all_tests():
    flash("Starting All Tests... Please be patient", "alert alert-info")
    report_or_error, returncode = run_tests("")

    if returncode == 0:
        flash("Successfully completed the test... Please check reports", "alert alert-success")
        return redirect(url_for('home'))
    else:
        flash(f"Test failed Process exited with status code {returncode}", "alert alert-danger")
        return redirect(url_for('home'))

@app.route('/tests/<path:subpath>')
def some_tests(subpath):
    flash(f"Starting {subpath} Please be patient", "alert alert-info")
    report_or_error, returncode = run_tests(escape(subpath))
    if returncode == 0:
        flash("Successfully completed the test... Please check reports", "alert alert-success")
        return redirect(url_for('home'))
    else:
        flash(f"Test failed Process exited with status code {returncode}", "alert alert-danger")
        return redirect(url_for('home'))


@app.route('/cleanup')
def cleanup():
    flash("Deleting all generated Reports", "alert alert-info")
    try:
        subprocess.run("rm -rf static", shell=True, check=True)
        flash("Deleted all generated Reports", "alert alert-success")
    except subprocess.CalledProcessError as e:
        return_code = e.returncode
        flash(f"Cleanup did not complete successfully. Return code of process: {return_code}", "alert alert-danger")

    return redirect(url_for('home'))


@app.route('/')
@app.route('/index')
def home():
    """
    Root path controller.
    :return: template index.html
    """
    return render_template('/index.html', testlist=get_all_test_module_names())


def run_tests(test_name):
    suffix = str(time.time()).replace('.','')
    filename = f"static/test_{suffix}.html"
    if test_name == "":
        command = f"pytest --html {filename} tests/"
    else:
        command = f"pytest --html {filename} tests/{test_name}"
    try:
        cmd_process = subprocess.run(command, shell=True, check=True)
        return_code = cmd_process.returncode
    except subprocess.CalledProcessError as e:
        return_code = e.returncode
        error_str = f"Tests Run did not complete successfully. Return code of process: {return_code}"
    if return_code == 0:
        return filename[7:], return_code
    else:
        return error_str, return_code

    return None


def get_all_test_module_names():
    tests = []
    for dirpath, dirnames, files in os.walk('tests'):
        for file_name in files:
            if file_name.endswith('.py'):
                if file_name.startswith('test'):
                    tests.append(file_name)
    return tests


