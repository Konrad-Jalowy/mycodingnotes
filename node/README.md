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

## Server js
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