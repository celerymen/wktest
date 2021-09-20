FROM python:3.8-buster

RUN apt update && apt upgrade -y
RUN apt install -y wkhtmltopdf=0.12.5-1
RUN pip install pdfminer.six

RUN mkdir /app /out
ADD pdfcheck.py /app
ADD entrypoint.sh /app
RUN chmod a+x /app/entrypoint.sh
WORKDIR /app
ENTRYPOINT ["./entrypoint.sh"]