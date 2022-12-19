FROM python:3.8

COPY requirements.txt /
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /requirements.txt
	