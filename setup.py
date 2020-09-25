from setuptools import setup

setup(
    name="armageddon",
    version="01",
    author="pradeep",
    install_requires=[
        "pytest==5.3.4",
        "pytest-html==2.1.1",
        "loguru==0.5.0",
        "jsons==1.2",
        "requests==2.22.0",
        "requests-toolbelt==0.9.1",
        "flask",
        "gunicorn"
    ]
)