exports.manualGetAll = catchAsync(async (req, res, next) => {

    let queryObj = { ...req.query };

    const excludedFields = ['page', 'sort', 'limit', 'fields'];

    let _page = req.query.page;
    let _limit = req.query.limit;
    let _shouldPaginate = (_page !== undefined || _limit !== undefined);
    let _shouldSort = (req.query.sort !== undefined);
    let _sortBy = "-createdAt";
    let _fields = "-__v";
    console.log(req.query.fields !== undefined)

    if(req.query.fields !== undefined){
        _fields = req.query.fields.split(',').join(' ');
    }
    
    excludedFields.forEach(el => delete queryObj[el]);

    let queryStr = JSON.stringify(queryObj);

    queryStr = queryStr.replace(/\b(gte|gt|lte|lt)\b/g, match => `$${match}`);

    parsedQueryObj = JSON.parse(queryStr);
    
    let _query = User.find(parsedQueryObj).select(_fields);
   
    if(_shouldSort){
        _sortBy = req.query.sort.split(',').join(' ');
    }

    if(_shouldPaginate){
        const page = _page * 1 || 1;
        const limit = _limit * 1 || 5;
        const skip = (page - 1) * limit;
        _query = _query.skip(skip).limit(limit);

    }

    _query = _query.sort(_sortBy);
   
    const _users = await _query;
    
    return res.json({"msg": "manual get all here",
        "users": _users
    });
});