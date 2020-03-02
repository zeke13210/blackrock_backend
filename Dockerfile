FROM zeke13210/blackrock:jet
WORKDIR '/app/'
COPY . .
EXPOSE 7000
CMD [ "python3", "app.py"]