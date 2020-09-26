FROM python:3.8

WORKDIR /armageddon

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

EXPOSE 4000

RUN pip install --upgrade pip

RUN pip install -e .

CMD ["gunicorn", "-w", "4", "--timeout","700", "-b", "0.0.0.0:4000", "app:app"]