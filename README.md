[![GitHub release](https://img.shields.io/github/v/release/colibris-xyz/iredadmin-docker.svg?style=flat)](https://github.com/colibris-xyz/iredadmin-docker/releases/latest)
[![GitHub license](https://img.shields.io/github/license/colibris-xyz/iredadmin-docker)](https://github.com/colibris-xyz/iredadmin-docker/blob/main/LICENSE)

# All-in-one (nginx + uwsgi + cron) Docker image for iRedAdmin

[iRedAdmin (Open Source Edition)](https://github.com/iredmail/iRedAdmin) is the admin panel of the iRedMail project. You will need a working iRedMail setup to be able to use this image.

## Basic usage

```console
$ docker run -d -p 8080:80 --env-file .env -v /var/vmail/vmail1:/var/vmail/vmail1
```

All the basic configuration is done by environment variables, see the list below.

## Environment variables configuration
The following variables can be set to configure iRedAdmin:

### iRedAdmin database configuration
- `IREDADMIN_DB_HOST` (not set by default) -  Hostname of the iRedAdmin database server.
- `IREDADMIN_DB_NAME` (default: `iredadmin`) - Name of the iRedAdmin database.
- `IREDADMIN_DB_USER` (default: `iredadmin`) - Username for the iRedAdmin database.
- `IREDADMIN_DB_PASSWORD`  (not set by default) - Password for the iRedAdmin database.
- `IREDADMIN_DB_PORT` (default: `3306`) - Port of the iRedAdmin database.

### Mail accounts backend configuration
- `DATABASE_BACKEND` (default: `ldap`) - The database backend to store mail accounts. Currently supported: `ldap`, `mysql`, `pgsql`.

__OpenLDAP backend__:
- `LDAP_URI` (not set by default)
- `LDAP_BASE_DN` (not set by default)
- `LDAP_DOMAINADMIN_DN` (not set by default)
- `LDAP_BIND_DN` (not set by default)
- `LDAP_BIND_PASSWORD` (not set by default)

__SQL backends__:
- `VMAIL_DB_HOST` (not set by default) -  Hostname of the vmail database server.
- `VMAIL_DB_NAME` (default: `vmail`) - Name of the vmail database.
- `VMAIL_DB_USER` (default: `vmailadmin`) - Username for the vmail database.
- `VMAIL_DB_PASSWORD` (not set by default) - Password for the vmail database.
- `VMAIL_DB_PORT` (default: `3306`) - Port of the vmail database.

### UI configuration
- `WEBMASTER_MAIL_ADDRESS` (not set by default) -  Site webmaster's mail address.
- `LOCAL_TIMEZONE` (default: `GMT`) - The default local timezone.
- `DEFAULT_LANGUAGE` (default: `en_US`) - The default language, see https://github.com/iredmail/iRedAdmin/tree/master/i18n for the possible values.

### amavisd-new cleanup tool configuration
iRedAdmin comes with a tool to clean up the amavisd-new database, you need to set the following variables to enable it:

- `AMAVISD_DB_HOST` (not set by default) - Hostname of the amavisd-new database server.
- `AMAVISD_DB_NAME` (default: `amavisd`) - Name of the amavisd-new database.
- `AMAVISD_DB_USER` (default: `amavisd`) - Username for the amavisd-new database.
- `AMAVISD_DB_PASSWORD`  (not set by default) - Password for the amavisd-new database.
- `AMAVISD_DB_PORT` (default: `3306`) - Port of the amavisd-new database.

### Misc configuration
- `DEFAULT_MTA_TRANSPORT` (default: `dovecot`) - The default MTA transfort, see iRedMail documentation for the other possible values.
- `VMAIL_UID` (default: `2000`) - Must match the host vmail user id.
