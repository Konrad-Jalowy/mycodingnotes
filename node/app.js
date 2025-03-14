//its just a skeleton to copy-paste along with server.js to setup some project with some structure...

const express = require('express');

const UserRouter = require("./routes/userRoutes");
const UserController = require('./controllers/userController');

const app = express();
app.use(express.json());
app.use("/v1", UserRouter);
app.use(UserController.errorHandler);
app.get('*', UserController.notFound);

module.exports = app;