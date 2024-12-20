# fluentAPI
Sorting, filtering, limiting fields and paginating in a lean, fluent manner.  

- **manual approach** - something i did before fluentAPI class
- **catchAsync** - just a helper
- **FluentAPI** - class itself
- **userModel** - model for my user  

How to use it:
```js
exports.fluentGetAll = catchAsync(async (req, res, next) => {

    let filter = {};

    const features = new FluentAPI(User.find(filter), req.query)
                    .filter()
                    .sort()
                    .limitFields()
                    .paginate();

    const _users = await features.query;

    return res.json({"users": _users});
});
```
