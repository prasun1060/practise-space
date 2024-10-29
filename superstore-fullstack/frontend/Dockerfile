FROM node:alpine
EXPOSE 4200
WORKDIR /frontend
COPY . .
RUN npm install -g @angular/cli
RUN rm -rf node_modules && npm install
RUN npm install --save bootstrap
CMD ["ng", "serve", "--host", "0.0.0.0", "--poll=2000"]