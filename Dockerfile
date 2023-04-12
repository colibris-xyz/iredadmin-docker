FROM python:3.11.2-alpine3.17

ENV VMAIL_UID=2000
ENV PYTHONPATH=/usr/local/lib/python3.11/site-packages:/usr/lib/python3.11/site-packages
ENV UWSGI_PLUGIN=python3

RUN apk add --no-cache nginx uwsgi-python3 supervisor postgresql-libs openldap-dev

RUN mkdir -p /var/www/app \
  && chown -R nobody.nobody /var/www/app \
  && chown -R nobody.nobody /run \
  && chown -R nobody.nobody /var/lib/nginx \
  && chown -R nobody.nobody /var/log/nginx

WORKDIR /var/www/app

ARG IREDADMIN_VERSION=2.3

RUN apk add --no-cache --virtual .build-deps cargo curl gcc linux-headers musl-dev postgresql-dev \
  && curl -L https://github.com/iredmail/iRedAdmin/archive/refs/tags/${IREDADMIN_VERSION}.tar.gz | tar -xz --strip-components=1 \
  && pip install -r requirements.txt --no-cache-dir \
  && cp /usr/local/lib/python3.11/site-packages/_ldap.*.so /usr/local/lib/python3.11/site-packages/_ldap.so \
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
