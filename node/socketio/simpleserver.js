const express = require("express");
const app = express();
const http = require("http");
const { Server } = require("socket.io");
const cors = require("cors");

app.use(cors());

const server = http.createServer(app);

const io = new Server(server, {
  cors: {
    origin: "http://localhost:3000",
    methods: ["GET", "POST"],
  },
});

let users_number = 0;
const users = {};

io.on("connection", (socket) => {
  console.log(`User Connected: ${socket.id}`);
  users_number++;
  console.log(`Number of users: ${users_number}`);
  io.emit("users-number-change", users_number);

  socket.on("send_message", (data) => {
    io.emit("receive_message", {message: data, name: users[socket.id], time: new Date()});
  });

  socket.on('new-user', name => {
    users[socket.id] = name;
    console.log(users);
    console.log(`User names: ${Object.values(users)}`);
    io.emit('user-names-change', Object.values(users));
  });

  socket.on('disconnect', () => {
    users_number--;
    delete users[socket.id];
    console.log(`Number of users: ${users_number}`);
    console.log(`User names: ${Object.values(users)}`);
    io.emit("users-number-change", users_number);
  })
});

server.listen(3001, () => {
  console.log("SERVER IS RUNNING");
});