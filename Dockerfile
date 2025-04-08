ARG PYTHON_VERSION=3.13
FROM python:$PYTHON_VERSION-slim

WORKDIR /usr/src/marz-g-node

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x generate_certs.sh
RUN chmod +x entrypoint.sh

EXPOSE 50051
CMD ["sh", "./entrypoint.sh"]