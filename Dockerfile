## Load env variables
FROM alpine as env-variables
WORKDIR /HolidayApp
COPY .env .env
RUN apk add --no-cache dos2unix
RUN dos2unix

## Copy relevant files and env variables
FROM python:3.9
WORKDIR /HolidayApp
COPY . /HolidayApp
COPY --from=env-variables /app/.env .env

## Copy encryption script
COPY encryption.py /HolidayApp/encryption.py
COPY ${ENCRYPTION_DICT_PATH} /HolidayApp/${ENCRYPTION_DICT_PATH}
COPY ${VALID_ENCRYPTION_KEYS_PATH} /HolidayApp/${VALID_ENCRYPTION_KEYS_PATH}

## Install dependancies
RUN pip3 install -r requirements.txt

## Expose port and start app
EXPOSE 5000
ENV FLASK_APP=server.py
CMD ["gunicorn", "-b", "0.0.0.0:8000", "server:app"]