#!/usr/bin/env bash
# Common functions and variables for all scripts

set -euo pipefail

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging functions
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1" >&2
}

# Get script and project directories
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [[ -z "${PROJECT_ROOT:-}" ]]; then
  PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
fi

# Load environment variables
load_env() {
    local env_file="${PROJECT_ROOT}/.env"
    
    if [[ ! -f "$env_file" ]]; then
        log_warn ".env file not found, copying from .env.example"
        cp "${PROJECT_ROOT}/.env.example" "$env_file"
    fi
    
    # Export variables from .env file
    set -a
    source "$env_file"
    set +a
    
    # Set defaults for any missing variables
    export AIRFLOW_NAMESPACE="${AIRFLOW_NAMESPACE:-airflow}"
    export AIRFLOW_VERSION="${AIRFLOW_VERSION:-2.8.1}"
    export VOLUMES_PATH="${VOLUMES_PATH:-${PROJECT_ROOT}/volumes}"
    export WEBSERVER_PORT="${WEBSERVER_PORT:-30080}"
    export POSTGRES_PASSWORD="${POSTGRES_PASSWORD:-airflow}"
    export KUBECONFIG="${KUBECONFIG:-${HOME}/.kube/config}"
}

# Check if a command exists
require_command() {
    if ! command -v "$1" &> /dev/null; then
        log_error "Required command '$1' not found. Please install it first."
        exit 1
    fi
}

# Wait for a deployment to be ready
wait_for_deployment() {
    local deployment=$1
    local namespace=$2
    local timeout=${3:-300}
    
    log_info "Waiting for deployment/${deployment} to be ready..."
    kubectl rollout status "deployment/${deployment}" \
        -n "$namespace" \
        --timeout="${timeout}s"
}

# Wait for all pods in namespace to be ready
wait_for_pods() {
    local namespace=$1
    local timeout=${2:-300}
    
    log_info "Waiting for all pods in ${namespace} to be ready..."
    kubectl wait --for=condition=ready pod \
        --all \
        -n "$namespace" \
        --timeout="${timeout}s" 2>/dev/null || true
}

# Generate a random string
generate_random_string() {
    local length=${1:-32}
    openssl rand -hex "$length" | head -c "$length"
}

# Generate Fernet key
generate_fernet_key() {
    python3 -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())" 2>/dev/null || \
    python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())" 2>/dev/null || \
    echo ""
}
