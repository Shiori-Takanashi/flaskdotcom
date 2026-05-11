# ==========================================
# Global Settings
# ==========================================

set dotenv-load := true

TARGETS := "src tests"
HOOK_TYPES := "pre-commit pre-push"

# ==========================================
# Default Task
# ==========================================

default:
    @just --list

# ==========================================
# ALL
# ==========================================

all: hooks modify verify

# ==========================================
# Git Hook
# ==========================================


hooks:
    @for hook in {{HOOK_TYPES}}; do \
        echo "Installing hook: $hook ..."; \
        uv run pre-commit install --hook-type $hook; \
    done

# ==========================================
# Modification
# ==========================================

modify: r-modify

r-modify:
    uv run ruff check --fix {{TARGETS}}
    uv run ruff format {{TARGETS}}

djl-modify:
    uv run djlint --reformat src/flaskdotcom/templates/

djh-modify:
    uv run djhtml src/flaskdotcom/templates/

# ==========================================
# Verification
# ==========================================

verify: r-verify type test

r-verify:
    uv run ruff check {{TARGETS}}
    uv run ruff format --check {{TARGETS}}

type:
    uv run mypy {{TARGETS}}

test:
    uv run pytest

djl-verify:
    uv run djlint --lint src/flaskdotcom/templates/


# ==========================================
# server
# ==========================================

server:
    uv run python -m flaskdotcom.app


# ==========================================
# HTML
# ==========================================

htmls: djl-modify djh-modify djl-verify

# ==========================================
# deploy
# ==========================================

deploy:
    gcloud run deploy snkflask-app \
      --source . \
      --region asia-northeast1 \
      --allow-unauthenticated
