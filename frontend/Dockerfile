FROM node:12-alpine
COPY . /frontend
WORKDIR /frontend
RUN npm install yarn && \
    yarn && \
    yarn run build && \
    yarn cache clean
CMD [ "yarn", "serve" ]
