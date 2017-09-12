FROM python:3.6

# Install python dependencies
ADD requirements.txt .
RUN pip3 install -r requirements.txt

# Add user
ARG PUID=1000
ARG PGID=1000
RUN groupadd -g $PGID django && \
    useradd -u $PUID -g django -m django

USER django