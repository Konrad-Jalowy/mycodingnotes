# Node

## catchAsync
It is so that you can catch errors in async/await syntax without stupid try/catch that is not so great in JS async/await.
Heres code:
```js
module.exports = fn => {
    return (req, res, next) => {
      fn(req, res, next).catch(next);
    };
  };
```
Usage:
```js
exports.registerPost = catchAsync(async (req, res, next) => {
    const hashedPassword = await bcrypt.hash(req.body.password, 10);

    let created = await User.create(
        { 
        name: req.body.name,
        email: req.body.email,
        password: hashedPassword
     });
    
    return res.status(201).redirect("/users/login");
  }
);
```
Super easy and gets the work done.

## Server js and App js
That how i do most of my node backend apps and such separation really works for me:
```js
const mongoose = require('mongoose');

require('dotenv').config();

const app = require("./app.js");

mongoose
  .connect(process.env.MONGO_URL)
  .then(() => console.log('DB connection successful!'));

const port = process.env.SERVER_PORT;

const server = app.listen(port, () => {
  console.log(`App running on port http://localhost:${port}...`);
});
```

Ok, now app.js, from another project, its just a skeleton:
```js
const express = require('express');

const UserRouter = require("./routes/userRoutes");
const UserController = require('./controllers/userController');

const app = express();
app.use(express.json());
app.use("/v1", UserRouter);
app.use(UserController.errorHandler);
app.get('*', UserController.notFound);

module.exports = app;
```
Thats how it looks like, routes in router, methods in controller, app exported, server.js handles db connection and starting the app.

## Param Middleware
I seem to foget from time to time how its done so heres param middleware.  
Always remember to check for correct ObjectId (if were doing mongodb):
```js
const checkID = async (req, res, next, val) => {

    if(!ObjectId.isValid(val))
        return res.status(404).json({"err": "invalid id"});
    
    let _user = await User.findOne({_id: val});

    if (_user === null) 
      return res.status(404).json({"err": "invalid id"});
    
    next();
  };
```
And dont forget about:
```js
app.param('id', checkID);
```

## Err handler (err middleware)
Basically if function has err, req, res and next, its error middleware. 
Err handler
```js
exports.errorHandler = (err, req, res, next) => {
    res.status(500).json({"Error": "Some kind of error occurred."});
};

exports.notFound = function(req, res){
    res.status(404).render("404");
  }
```
And how to use:
```js
app.use(MainController.errorHandler);
app.get('*', MainController.notFound);
```

# Node Libraries
Libraries worth installing:
- express-ejs-layouts
- express-validator
## express-ejs-layouts
Layouts for ejs. 
```sh
npm i express-ejs-layouts
```
How to use:
```js
//(...)
const expressLayouts = require('express-ejs-layouts');
//(...)
const app = express();
//(...)
app.use(expressLayouts);
app.set('view engine', 'ejs');
app.set("layout extractScripts", true)
```
Lates one is so that we could use scripts.
Now layout.ejs:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Layout</title>
    <link rel="stylesheet" href="http://localhost:3010/style.css">
</head>
<body>
    <%- include('partials/header.ejs') %>
    <%- body %>
    <%- script %>
</body>
</html>
```
And thats how inheriting from this layout looks like, body and scripts:
```html
<%if (error.length > 0) { %>
    <p>Some kind of error happened. Check your login credentials</p>
<% } %>

<%if (locals.message.length > 0) { %>
    <div class="error-message ani-fadein"><p><%= locals.message %></p></div>
<% } %>

<%- include('partials/loginForm.ejs') %>

<script src="/error-message.js"></script>
```
And for rendering it you use simple render with filename. It will render it together with layout.ejs.
And thats mostly basic setup, this library has some other features, all in the docs.

## express-validator
Simple example how to use it. Import:
```js
const { body, validationResult } = require('express-validator');
```
Ok, helper, first middleware:
```js
exports.loginValidator = [
    body('email', 'Please enter an email').isEmail().trim(),
    body('password', 'Please enter password').not().isEmpty(),
    body('email').custom(async value => {
        const user = await User.findOne({email: value});
        if (user === null) {
          throw new Error('User doesnt exist');
        }
      }),
];
```
Second middleware:
```js
exports.validateAndForwardLogin = (req, res, next) => {
    const errors = validationResult(req)
    if (errors.isEmpty()) {
      
      return next();
    }
    console.log(errors);
    
    req.flash('message', `Login Failed`);
    return res.redirect('/users/login');
}
```
How we use it:
```js
router.post("/login", forwardAuthenticated, UserController.loginValidator, UserController.validateAndForwardLogin);
router.post('/login', UserController.loginPost);
```
First is middleware that checks if user is not logged in and lets guests only. Then our middlewares.