FROM python:3

RUN apt-get update && apt-get -y install cron

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR .

RUN mkdir -p /data0/logs/renewal_manager/

RUN python manage.py migrate

EXPOSE 17007

RUN python manage.py crontab add

CMD gunicorn renewal_manager.wsgi -w 6 -t 120 -k gevent  --threads 5 -b 0.0.0.0:17007  --access-logfile -


