FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -subj "/C=ES/ST=Madrid/L=Madrid/O=OrgName/OU=IT Recruitment/CN=localhost" -out cert.pem
RUN update-ca-certificates
COPY . .
