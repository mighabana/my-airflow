#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/_common.sh"

log_info "Generating secrets..."

ENV_FILE="${PROJECT_ROOT}/.env"

# Ensure .env exists
if [[ ! -f "$ENV_FILE" ]]; then
    cp "${PROJECT_ROOT}/.env.example" "$ENV_FILE"
fi

# Generate Fernet key if not set
if ! grep -q "^FERNET_KEY=.\+" "$ENV_FILE" 2>/dev/null; then
    log_info "Generating Fernet key..."
    
    # Try to generate with Python, fall back to a valid base64 key
    FERNET_KEY=$(generate_fernet_key)
    
    if [[ -z "$FERNET_KEY" ]]; then
        log_warn "Python cryptography not available, installing..."
        pip3 install cryptography --quiet 2>/dev/null || \
        pip install cryptography --quiet 2>/dev/null || \
        sudo apt-get install -y python3-pip && pip3 install cryptography --quiet
        
        FERNET_KEY=$(generate_fernet_key)
    fi
    
    if [[ -n "$FERNET_KEY" ]]; then
        sed -i "s|^FERNET_KEY=.*|FERNET_KEY=${FERNET_KEY}|" "$ENV_FILE"
        log_success "Fernet key generated"
    else
        log_error "Failed to generate Fernet key"
        exit 1
    fi
else
    log_info "Fernet key already set"
fi

# Generate webserver secret key if not set
if ! grep -q "^WEBSERVER_SECRET_KEY=.\+" "$ENV_FILE" 2>/dev/null; then
    log_info "Generating webserver secret key..."
    SECRET_KEY=$(generate_random_string 32)
    sed -i "s|^WEBSERVER_SECRET_KEY=.*|WEBSERVER_SECRET_KEY=${SECRET_KEY}|" "$ENV_FILE"
    log_success "Webserver secret key generated"
else
    log_info "Webserver secret key already set"
fi

log_success "Secrets configured in .env"
