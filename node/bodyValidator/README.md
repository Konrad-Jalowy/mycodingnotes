# bodyValidator class
Looks like some time ago i wrote a class to validate body. I didnt know express-validator package back then.  

Class is in bodyValidator file.

Thats how you use it:
```js
exports.postUserMiddleware = (req, res, next) => {
    const _fields = [
        {
        required: true,
        name: "firstName",
        type: "string",
        notEmpty: true
        },
        {
            required: true,
            name: "lastName",
            type: "string",
            notEmpty: true
        },
        {
            required: true,
            name: "age",
            type: "number"
        },
        {
            required: true,
            name: "cash",
            min: 0,
            default: 0
        }
   ];
    const _validator = new BodyValidator(req.body, _fields)
    const _errorList = _validator.validate();
    //todo - use body validator class here
    console.log("post user middleware used");
    console.log(_errorList);
    next();
}
```
In place of todo add check if error list is empty and use next only then. Its old code im not doing it anymore, but maybe itll be useful to somebody.