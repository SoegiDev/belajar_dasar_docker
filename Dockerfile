# ---- Base python ----
FROM python:3.9 AS base
# Create app directory

WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# We use a Docker multi-stage build here in order that we only take the compiled go executable
FROM python:3.9-alpine
WORKDIR /app
COPY --from=base /app ./
RUN pip install --no-cache-dir -r ./requirements.txt
CMD ["python", "app.py"]


