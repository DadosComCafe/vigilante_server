FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim
WORKDIR /usr/src/app
COPY . .
RUN uv sync --locked --no-install-project
COPY . .
EXPOSE 7860
ENV GRADIO_SERVER_NAME="0.0.0.0"
RUN uv sync --locked
CMD ["uv", "run", "main.py"]
