# ---------- Builder stage ----------
FROM python:3.12-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install uv
RUN pip install --no-cache-dir uv

# Copy Dependency Definitions first for better caching
COPY pyproject.toml uv.lock ./

# Install project dependencies into virtual environment
RUN uv sync --frozen --no-dev

# COPY the application source
COPY . .

# ---------- Runtime Stage ------------ #
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1
ENV PYTHONPATH=/app/src
ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app

# COPY THE VIRTUAL ENVIRONMENT
COPY --from=builder /app/.venv /app/.venv

# COPY THE APPLICATION
COPY --from=builder /app /app

EXPOSE 8000

CMD ["uvicorn", "copilot.main:app", "--host", "0.0.0", "--port", "8000"]