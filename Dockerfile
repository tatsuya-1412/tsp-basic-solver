FROM python:3.11-buster AS builder
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update \
  && apt-get install --no-install-recommends -y \
  default-mysql-client \
  tzdata \
  vim \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -U pip setuptools wheel \
  && pip install --no-cache-dir pdm

WORKDIR /project

COPY pyproject.toml pdm.lock README.md .env ./
COPY src src
COPY lib lib
COPY results results

RUN mkdir __pypackages__ \
  && pdm install --no-lock --no-editable --prod

EXPOSE 80
CMD ["bash"]