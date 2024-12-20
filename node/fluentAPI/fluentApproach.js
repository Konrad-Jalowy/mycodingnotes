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