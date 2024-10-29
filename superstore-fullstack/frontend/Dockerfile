FROM node:alpine
EXPOSE 4200
WORKDIR /frontend
RUN npm install -g @angular/cli
COPY . .
RUN npm install
RUN npm i
CMD ["ng", "serve", "--host", "0.0.0.0"]