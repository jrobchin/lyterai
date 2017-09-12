FROM node:8

# Add user
ARG PUID=1010
ARG PGID=1010
RUN groupadd -g $PGID frontend && \
    useradd --create-home -u $PUID -g frontend -m frontend

RUN mkdir /home/frontend/.npm-global
RUN npm config set prefix '/home/frontend/.npm-global'

ENV PATH "$PATH:/home/frontend/.npm-global"

RUN chown -R frontend /home/frontend/.npm-global

COPY package.json /front/package.json
WORKDIR /front
RUN npm install --global

USER frontend