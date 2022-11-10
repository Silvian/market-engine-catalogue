FROM python:3.10-buster

WORKDIR /app
EXPOSE 50051

COPY requirements* ./
RUN --mount=type=cache,mode=0755,target=/root/.cache/pip \
    pip install --upgrade pip pip-tools \
    && pip install -r requirements.txt \
    && pip install -r requirements-dev.txt \
    && pip wheel --wheel-dir=/root/wheels -r requirements.txt -r requirements-dev.txt

COPY app app/
COPY tests/ tests/
COPY pyproject.toml ./

ENTRYPOINT ["app/server.py"]
