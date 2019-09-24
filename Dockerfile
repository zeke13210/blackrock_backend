FROM zeke13210/blackrock:jet

WORKDIR '/app'

COPY . .
EXPOSE 5000
CMD [ "python3", "app.py" ]