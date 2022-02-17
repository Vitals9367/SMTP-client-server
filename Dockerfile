FROM python:3.9

ENV BUILD_MODE='DOCKER'
ENV SMTP_SERVER='<your SMTP_SERVER>'
ENV BUILD_MODE='<your PORT>'
ENV BUILD_MODE='<your SENDER>'
ENV BUILD_MODE='<your PASSWORD>'

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./server.py" ]