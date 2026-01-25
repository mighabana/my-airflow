# K3s + Apache Airflow Deployment

A portable, repeatable Apache Airflow deployment on K3s (lightweight Kubernetes) for single-node servers.

## Features

- **Single-command deployment** — Get Airflow running with `./scripts/deploy-airflow`
- **Self-contained** — All persistent data stored in `volumes/` directory within the repo
- **KubernetesExecutor** — Each task runs in its own pod for isolation and scalability
- **External PostgreSQL** — Uses official `postgres:16` image instead of Bitnami for reliability
- **Customizable** — Easy configuration via environment variables and Helm values

## Prerequisites

- Linux server (Ubuntu 20.04+ recommended)
- Minimum 4 CPU cores, 8GB RAM, 50GB disk
- Root or sudo access
- Ports 6443 (K3s API) and 30123 (Airflow UI) available

## Quick Start

```bash
# 1. Clone the repository
git clone <your-repo-url> && cd airflow

# 2. Copy and configure environment
cp .env.example .env
# Edit .env if needed (secrets are auto-generated on first deploy)

# 3. Install K3s (skip if already installed)
./scripts/install-k3s

# 4. Deploy Airflow
./scripts/deploy-airflow

# 5. Access Airflow UI
echo "http://$(hostname -I | awk '{print $1}'):30123"
# Default credentials: admin / admin
```

## Repository Structure

```
airflow/
├── scripts/
│   ├── deploy-airflow       # Main deployment script
│   ├── install-k3s          # K3s installation
│   ├── teardown             # Clean uninstall
│   └── lib/
│       ├── _common.sh       # Shared functions
│       └── generate-secrets.sh
├── k8s/
│   ├── postgres.yaml        # PostgreSQL deployment (official image)
│   └── storage.yaml         # PersistentVolume definitions
├── helm/
│   ├── values.yaml          # Base Helm values (templated)
│   └── values.local.yaml    # Local overrides (git-ignored)
├── config/
│   └── webserver_config.py  # Webserver customization (auth, theme)
├── dags/
│   └── hello_world.py       # Example DAG
├── volumes/                  # Persistent storage (git-ignored)
│   ├── dags/                # DAGs synced here
│   └── logs/                # Airflow logs
├── .env.example             # Environment template
├── .env                     # Your configuration (git-ignored)
└── README.md
```

## Configuration

### Environment Variables (`.env`)

| Variable | Default | Description |
|----------|---------|-------------|
| `AIRFLOW_VERSION` | `3.1.6` | Airflow Docker image tag |
| `AIRFLOW_NAMESPACE` | `airflow` | Kubernetes namespace |
| `VOLUMES_PATH` | `./volumes` | Path to persistent storage directory |
| `WEBSERVER_PORT` | `30123` | NodePort for Airflow UI |
| `FERNET_KEY` | (auto-generated) | Encryption key for connections/variables |
| `WEBSERVER_SECRET_KEY` | (auto-generated) | Flask session secret |
| `POSTGRES_PASSWORD` | `airflow` | PostgreSQL password |
| `WEBSERVER_MEMORY_REQUEST` | `2Gi` | Webserver memory request |
| `WEBSERVER_MEMORY_LIMIT` | `4Gi` | Webserver memory limit |
| `SCHEDULER_MEMORY_REQUEST` | `2Gi` | Scheduler memory request |
| `SCHEDULER_MEMORY_LIMIT` | `4Gi` | Scheduler memory limit |

Secrets (`FERNET_KEY`, `WEBSERVER_SECRET_KEY`) are auto-generated on first deployment if left empty.

### Helm Values (`helm/values.local.yaml`)

Create this file for environment-specific overrides (git-ignored):

```yaml
# Extra Python packages
extraPipPackages:
  - polars
  - clickhouse-connect
  - apache-airflow-providers-slack

# Timezone and concurrency settings  
config:
  core:
    default_timezone: "Europe/Madrid"
    parallelism: 32
    max_active_tasks_per_dag: 16
    max_active_runs_per_dag: 5

# Airflow connections (alternative: configure via UI)
env:
  - name: AIRFLOW_CONN_CLICKHOUSE_DEFAULT
    value: "clickhouse://user:pass@host:8123/db"
  - name: AIRFLOW_CONN_MY_API
    value: "http://apikey@api.example.com"

# External PostgreSQL (required - disables bundled Bitnami PostgreSQL)
postgresql:
  enabled: false

data:
  metadataConnection:
    user: airflow
    pass: airflow
    host: airflow-postgres
    port: 5432
    db: airflow
```

### Webserver Configuration (`config/webserver_config.py`)

Customize authentication, theming, and other webserver settings:

```python
# Example: Dark theme
APP_THEME = "darkly"

# Example: OAuth with Google
from airflow.providers.fab.auth_manager.security_manager.override import FabAirflowSecurityManagerOverride
AUTH_TYPE = AUTH_OAUTH
AUTH_USER_REGISTRATION = True
OAUTH_PROVIDERS = [...]
```

See the file for complete examples including LDAP, OAuth, and RBAC configuration.

## Commands Reference

### Deployment

```bash
# Full deployment (creates namespace, PVs, PostgreSQL, Airflow)
./scripts/deploy-airflow

# Sync DAGs only (fast, no Helm upgrade)
./scripts/deploy-airflow --dags-only

# Complete teardown (removes everything)
./scripts/teardown
```

### Adding DAGs

```bash
# Option 1: Copy to dags/ directory and sync
cp my_dag.py dags/
./scripts/deploy-airflow --dags-only

# Option 2: Copy directly to volumes (immediate)
cp my_dag.py volumes/dags/
```

DAGs appear in the UI within 30 seconds.

### Debugging

```bash
# Check pod status
kubectl get pods -n airflow

# View scheduler logs (DAG parsing errors appear here)
kubectl logs -f deployment/airflow-scheduler -n airflow

# View webserver logs
kubectl logs -f deployment/airflow-webserver -n airflow

# Shell into a pod
kubectl exec -it deployment/airflow-scheduler -n airflow -- bash

# Check PostgreSQL
kubectl logs deployment/airflow-postgres -n airflow
```

### Airflow CLI

```bash
# List DAGs
kubectl exec -it deployment/airflow-scheduler -n airflow -- airflow dags list

# Trigger a DAG
kubectl exec -it deployment/airflow-scheduler -n airflow -- airflow dags trigger hello_world

# Test a specific task
kubectl exec -it deployment/airflow-scheduler -n airflow -- airflow tasks test hello_world hello_python 2024-01-01

# Force DAG refresh
kubectl exec -it deployment/airflow-scheduler -n airflow -- airflow dags reserialize
```

### Maintenance

```bash
# Restart components after config changes
kubectl rollout restart deployment/airflow-webserver -n airflow
kubectl rollout restart deployment/airflow-scheduler -n airflow

# Check resource usage
kubectl top pods -n airflow

# View events (useful for debugging)
kubectl get events -n airflow --sort-by='.lastTimestamp'
```

## Advanced Configuration

### Git Sync for DAGs

Automatically sync DAGs from a Git repository instead of manual copying:

```yaml
# helm/values.local.yaml
dags:
  persistence:
    enabled: false
  gitSync:
    enabled: true
    repo: "https://github.com/your-org/airflow-dags.git"
    branch: "main"
    subPath: "dags"
    wait: 60
```

For private repositories:

```bash
kubectl create secret generic git-credentials \
  --from-literal=GIT_SYNC_USERNAME=your-username \
  --from-literal=GIT_SYNC_PASSWORD=your-token \
  -n airflow
```

### Custom Docker Image

For complex dependencies or private packages, build a custom image:

```dockerfile
FROM apache/airflow:3.1.6

USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

USER airflow
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt
```

```bash
docker build -t your-registry/airflow:custom .
docker push your-registry/airflow:custom
```

```yaml
# helm/values.local.yaml
defaultAirflowRepository: your-registry/airflow
defaultAirflowTag: custom
```

### Task-Level Resources

For KubernetesExecutor, configure resources per task in your DAG:

```python
from kubernetes.client import models as k8s

heavy_task = PythonOperator(
    task_id="heavy_processing",
    python_callable=process_data,
    executor_config={
        "pod_override": k8s.V1Pod(
            spec=k8s.V1PodSpec(
                containers=[k8s.V1Container(
                    name="base",
                    resources=k8s.V1ResourceRequirements(
                        requests={"memory": "4Gi", "cpu": "1"},
                        limits={"memory": "8Gi", "cpu": "2"}
                    )
                )]
            )
        )
    }
)
```

## Troubleshooting

### Pods stuck in Pending

```bash
kubectl describe pod <pod-name> -n airflow
# Common causes: PVC not bound, insufficient resources
```

Check PVC status:

```bash
kubectl get pvc -n airflow
kubectl get pv
```

### DAGs not appearing

```bash
# Check for syntax errors in scheduler logs
kubectl logs deployment/airflow-scheduler -n airflow | grep -i error

# Verify DAG files exist
ls -la volumes/dags/

# Force refresh
kubectl exec -it deployment/airflow-scheduler -n airflow -- airflow dags reserialize
```

### Database connection issues

```bash
# Test PostgreSQL connectivity
kubectl exec -it deployment/airflow-postgres -n airflow -- psql -U airflow -c "SELECT 1;"

# Check PostgreSQL logs
kubectl logs deployment/airflow-postgres -n airflow

# Restart PostgreSQL
kubectl rollout restart deployment/airflow-postgres -n airflow
```

### Helm upgrade failures

If you see "Job is immutable" errors:

```bash
# Delete stuck jobs and retry
kubectl delete jobs --all -n airflow
./scripts/deploy-airflow
```

### Context deadline exceeded

This usually means pods aren't becoming ready. Debug with:

```bash
# Check which pods are failing
kubectl get pods -n airflow

# Check events for errors
kubectl get events -n airflow --sort-by='.lastTimestamp' | tail -20

# Check specific pod logs
kubectl logs <pod-name> -n airflow
kubectl describe pod <pod-name> -n airflow
```

## Updating Airflow

1. Update `AIRFLOW_VERSION` in `.env`
2. Run `./scripts/deploy-airflow`

> **Note:** Check Airflow release notes for breaking changes before major version upgrades. The Helm chart version must be compatible with the Airflow version.

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        K3s Cluster                          │
│  ┌─────────────────────────────────────────────────────────┐│
│  │                  airflow namespace                      ││
│  │  ┌───────────┐  ┌───────────┐  ┌───────────┐            ││
│  │  │ Webserver │  │ Scheduler │  │ Triggerer │            ││
│  │  └─────┬─────┘  └─────┬─────┘  └─────┬─────┘            ││
│  │        │              │              │                  ││
│  │        └──────────────┼──────────────┘                  ││
│  │                       │                                 ││
│  │                       ▼                                 ││
│  │            ┌─────────────────────┐                      ││
│  │            │     PostgreSQL      │                      ││
│  │            │  (airflow-postgres) │                      ││
│  │            └─────────────────────┘                      ││
│  │                       │                                 ││
│  │        ┌──────────────┼──────────────┐                  ││
│  │        ▼              ▼              ▼                  ││
│  │  ┌───────────┐  ┌───────────┐  ┌───────────┐            ││
│  │  │ DAGs PVC  │  │ Logs PVC  │  │Postgres PVC│           ││
│  │  └───────────┘  └───────────┘  └───────────┘            ││
│  └─────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────┘
         │                 │
         ▼                 ▼
   ./volumes/dags    ./volumes/logs
```

## License

MIT
