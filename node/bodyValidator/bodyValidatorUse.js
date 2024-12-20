//it was long time ago i didnt know about express-validator package
//and it only shows the errors in the console, then does the next()
//just add if check that use next only when errorlist is empty
//and of course this is controller file, you need some routing for that
//you can figure out how it works or use express-validator package


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
exports.postUser =  async (req, res) => {
    return res.json({"body": req.body});
};