import os
from distutils.util import strtobool

# -*- coding: utf-8 -*-
#
############################################################
# DO NOT MODIFY THIS LINE, IT'S USED TO IMPORT DEFAULT SETTINGS.
from libs.default_settings import *

LOG_TARGET = "stdout"

# Default timezone
if os.getenv('LOCAL_TIMEZONE'):
    LOCAL_TIMEZONE = os.getenv('LOCAL_TIMEZONE')

############################################################
# General settings.
#
# Site webmaster's mail address.

webmaster = os.getenv('WEBMASTER_MAIL_ADDRESS')

# Default language.
default_language = os.getenv('DEFAULT_LANGUAGE', 'en_US')

# Database backend
backend = os.getenv('DATABASE_BACKEND', 'ldap').lower()

# Directory used to store mailboxes. Defaults to /var/vmail/vmail1.
# Note: This directory must be owned by 'vmail:vmail' with permission 0700.
storage_base_directory = '/var/vmail/vmail1'

# Default mta transport.
# There're 3 transports available in iRedMail:
#
#   1. dovecot: default LDA transport. Supported by all iRedMail releases.
#   2. lmtp:unix:private/dovecot-lmtp: LMTP (socket listener). Supported by
#                                      iRedMail-0.8.6 and later releases.
#   3. lmtp:inet:127.0.0.1:24: LMTP (TCP listener). Supported by iRedMail-0.8.6
#                              and later releases.
#
# Note: You can set per-domain or per-user transport in account profile page.
default_mta_transport = os.getenv('DEFAULT_MTA_TRANSPORT', 'dovecot')

# Min/Max admin password length. 0 means unlimited.
#   - min_passwd_length: at least 1 character is required.
# Normal admin can not set shorter/longer password lengths than global settings
# defined here.
min_passwd_length = 8
max_passwd_length = 0

#####################################################################
# Database used to store iRedAdmin data. e.g. sessions, log.
#
iredadmin_db_host = os.getenv('IREDADMIN_DB_HOST')
iredadmin_db_port = int(os.getenv('IREDADMIN_DB_PORT', '3306'))
iredadmin_db_name = os.getenv('IREDADMIN_DB_NAME', 'iredadmin')
iredadmin_db_user = os.getenv('IREDADMIN_DB_USER', 'iredadmin')
iredadmin_db_password = os.getenv('IREDADMIN_DB_PASSWORD')

##############################################################################
# Settings used for Amavisd-new integration. Provides spam/virus quaranting,
# releasing, etc.

if os.getenv('AMAVISD_DB_HOST'):

    amavisd_enable_logging = True
    amavisd_enable_quarantine = True

    amavisd_db_host = os.getenv('AMAVISD_DB_HOST')
    amavisd_db_port = int(os.getenv('AMAVISD_DB_PORT', '3306'))
    amavisd_db_name = os.getenv('AMAVISD_DB_NAME', 'amavisd')
    amavisd_db_user = os.getenv('AMAVISD_DB_USER', 'amavisd')
    amavisd_db_password = os.getenv('AMAVISD_DB_PASSWORD')

##############################################################################
# Settings used for iRedAPD integration. Provides throttling and more.
#
iredapd_enabled = False

############################################################################
# Settings used for OpenLDAP backend.
#
if backend == 'ldap':

    # LDAP server uri. Examples:
    # - ldap://127.0.0.1    normal LDAP connection (port 389)
    # - ldaps://127.0.0.1   secure connection through STARTTLS (port 389)
    ldap_uri = os.getenv('LDAP_URI')

    # LDAP suffix.
    # basedn: dn which contains virtual domains.
    # domainadmin_dn: dn which contains virtual domain admins.
    ldap_basedn = os.getenv('LDAP_BASE_DN')
    ldap_domainadmin_dn = os.getenv('LDAP_DOMAINADMIN_DN')

    # Bind dn and password.
    #   - bind dn should have write privilege in LDAP.
    #   - bind pw is plain text, not encryped/hashed.
    ldap_bind_dn = os.getenv('LDAP_BIND_DN')
    ldap_bind_password = os.getenv('LDAP_BIND_PASSWORD')

elif backend == 'mysql' or backend == 'pgsql':

    ############################################
    # Database used to store mail accounts.
    #
    vmail_db_host = os.getenv('VMAIL_DB_HOST')
    vmail_db_port = int(os.getenv('VMAIL_DB_PORT', '3306'))
    vmail_db_name = os.getenv('VMAIL_DB_NAME', 'vmail')
    vmail_db_user = os.getenv('VMAIL_DB_USER', 'vmailadmin')
    vmail_db_password = os.getenv('VMAIL_DB_PASSWORD')
