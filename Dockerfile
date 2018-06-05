FROM python:3.6-alpine
WORKDIR /code
ADD . /code
RUN pip install -r requirements.txt
ENTRYPOINT ["/code/entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0:8000"]
EXPOSE 8000
