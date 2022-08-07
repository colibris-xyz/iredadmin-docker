FROM python:3.8.12-alpine3.13

ENV VMAIL_UID=2000
ENV PYTHONPATH=/usr/local/lib/python3.8/site-packages:/usr/lib/python3.8/site-packages
ENV UWSGI_PLUGIN=python3

RUN apk add --no-cache nginx uwsgi-python3 supervisor postgresql-libs \
  && apk add --no-cache --virtual .build-deps curl gcc musl-dev postgresql-dev libffi-dev openldap-dev

RUN mkdir -p /var/www/app \
  && chown -R nobody.nobody /var/www/app \
  && chown -R nobody.nobody /run \
  && chown -R nobody.nobody /var/lib/nginx \
  && chown -R nobody.nobody /var/log/nginx

WORKDIR /var/www/app

ARG IREDADMIN_VERSION=1.8

RUN curl -L https://github.com/iredmail/iRedAdmin/archive/refs/tags/${IREDADMIN_VERSION}.tar.gz | tar -xz --strip-components=1 \
  && pip install -r requirements.txt --no-cache-dir \
  && apk --purge del .build-deps

COPY config/crontab /var/spool/cron/crontabs/root
COPY config/nginx.conf /etc/nginx/nginx.conf
COPY config/uwsgi.ini /etc/uwsgi/uwsgi.ini
COPY config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY config/settings.py /var/www/app/settings.py

COPY --chown=nobody:nobody entrypoint.sh /

EXPOSE 80

ENTRYPOINT ["/entrypoint.sh"]
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
