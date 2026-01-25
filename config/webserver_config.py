#
# Airflow 3.x Webserver/API Server Configuration
#
# Note: Airflow 3.x has significant changes to authentication.
# The FAB (Flask-AppBuilder) auth manager is now a provider package.
#
# Documentation:
# - https://airflow.apache.org/docs/apache-airflow/stable/security/webserver.html
#

import os

# ------------------------------------------------------------------------------
# Authentication Configuration
# ------------------------------------------------------------------------------
# Airflow 3.x uses a new authentication system. The default is "simple" auth
# which uses the database for user management.
#
# For OAuth, LDAP, etc., you need to install apache-airflow-providers-fab
# and configure the auth manager in airflow.cfg or via environment variables.

# Application name shown in navbar
APP_NAME = "Airflow"

# Theme options (Airflow 3.x may have different theming support)
# Check the Airflow 3.x documentation for available themes
APP_THEME = "darkly"

# ------------------------------------------------------------------------------
# Session Configuration
# ------------------------------------------------------------------------------

# Session lifetime in minutes (default: 1440 = 24 hours)
# PERMANENT_SESSION_LIFETIME = 1440


# ------------------------------------------------------------------------------
# Custom Menu Links (Optional)
# ------------------------------------------------------------------------------

# Add custom links to the navbar
# FAB_ADD_MENU_LINKS = [
#     {
#         'name': 'Documentation',
#         'href': 'https://airflow.apache.org/docs/',
#         'category': 'Docs',
#         'icon': 'fa-book'
#     },
# ]


# ------------------------------------------------------------------------------
# Airflow 3.x Authentication Notes
# ------------------------------------------------------------------------------
#
# Airflow 3.x changed how authentication works:
#
# 1. Simple Auth (default):
#    Uses database-backed users. Configure via UI or CLI.
#
# 2. FAB Auth Manager (OAuth, LDAP, etc.):
#    Install: apache-airflow-providers-fab
#    Set in values.local.yaml:
#      config:
#        core:
#          auth_manager: airflow.providers.fab.auth_manager.fab_auth_manager.FabAuthManager
#
# 3. For OAuth with FAB, add to values.local.yaml env:
#    env:
#      - name: AIRFLOW__FAB__AUTH_TYPE
#        value: "AUTH_OAUTH"
#      - name: GOOGLE_OAUTH_CLIENT_ID
#        value: "your-client-id"
#      - name: GOOGLE_OAUTH_CLIENT_SECRET
#        value: "your-client-secret"
#
# See: https://airflow.apache.org/docs/apache-airflow-providers-fab/stable/auth-manager/index.html
