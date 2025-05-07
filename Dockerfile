FROM python:latest

RUN pip install --upgrade pip && pip install django

VOLUME ["/home/project_portfolio"]

ADD ./project_portfolio/. /home/project_portfolio

WORKDIR /home/project_portfolio/my_portfolio

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000
