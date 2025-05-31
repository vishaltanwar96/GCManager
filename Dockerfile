FROM python:3.13.2-slim-bullseye
RUN apt-get update
RUN apt-get install curl -y
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:${PATH}"
ENV APP_ENV=PROD
COPY ./ /app/
WORKDIR /app
RUN uv sync --no-group dev --no-install-project
ENTRYPOINT ["gunicorn", "-w", "1", "--bind", "0.0.0.0:8000" , "gcmanager.app:create_app()"]
