FROM python:3.8 
WORKDIR /app
COPY . .
EXPOSE 5000
RUN apt-get update && apt-get install -y \
    python3-pip 
RUN pip3 install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
CMD [ "/bin/sh", "-c","python3.8 app.py" ]
