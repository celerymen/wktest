FROM python:3.8-buster

RUN apt update && apt upgrade -y
RUN apt install rsync wget
RUN cd /opt                                                                                                              && \
    wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz && \
    tar xJf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz                                                                  && \
    rsync -r /opt/wkhtmltox/ /usr/
RUN pip install pdfminer.six

RUN mkdir /app /out
ADD pdfcheck.py /app
ADD entrypoint.sh /app
RUN chmod a+x /app/entrypoint.sh
WORKDIR /app
ENTRYPOINT ["./entrypoint.sh"]