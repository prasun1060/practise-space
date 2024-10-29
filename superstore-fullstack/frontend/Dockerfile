FROM node:alpine
EXPOSE 4200
WORKDIR /frontend
RUN npm install -g @angular/cli
COPY . .
RUN rm -rf node_modules && npm install
CMD ["ng", "serve", "--host", "0.0.0.0", "--poll=2000"]