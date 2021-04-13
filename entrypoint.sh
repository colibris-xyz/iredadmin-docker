#!/bin/sh

## Add a vmail user for the cron job "delete_mailboxes.py"
## The script verifies that the vmail dir is owned by the user "vmail", so VMAIL_UID must math the host's one (default to 2000)
adduser --system --no-create-home --uid "$VMAIL_UID" vmail

exec "$@"
