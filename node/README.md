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