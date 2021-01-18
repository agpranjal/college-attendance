FROM alpine:latest

RUN apk update && apk add \
    python3 \
    curl

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3 get-pip.py

COPY . .
RUN pip3 install -r requirements.txt

CMD python3 attendance.py
