# sample-api

Minimal API used to validate CI, GitOps, observability, autoscaling, security and progressive delivery.

## Endpoints

- `GET /`: service and environment metadata
- `GET /health`: liveness check
- `GET /ready`: readiness check
- `GET /version`: application version from `APP_VERSION`, defaulting to `local`
