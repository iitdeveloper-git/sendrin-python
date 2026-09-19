#!/usr/bin/env bash
# Regenerates packages/sendrin-python/src/sendrin/generated from the Sendrin
# OpenAPI spec. Run this whenever apps/docs/content/openapi.json changes.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PACKAGE_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
REPO_ROOT="$(cd "${PACKAGE_DIR}/../.." && pwd)"

openapi-python-client generate \
  --path "${REPO_ROOT}/apps/docs/content/openapi.json" \
  --meta none \
  --output-path "${PACKAGE_DIR}/src/sendrin/generated" \
  --overwrite
