from setuptools import setup

setup(
    name="armageddon",
    version="1.0.0",
    author="pradeep",
    install_requires=[
        "pytest",
        "pytest-html",
        "loguru==0.5.0",
        "jsons==1.2",
        "requests==2.22.0",
        "requests-toolbelt==0.9.1",
        "flask",
        "gunicorn", 'markupsafe'
    ]
)