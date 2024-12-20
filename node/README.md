# Node

## catchAsync
Usage
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