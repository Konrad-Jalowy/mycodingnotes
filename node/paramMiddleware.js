const checkID = async (req, res, next, val) => {

    if(!ObjectId.isValid(val))
        return res.status(404).json({"err": "invalid id"});
    
    let _user = await User.findOne({_id: val});

    if (_user === null) 
      return res.status(404).json({"err": "invalid id"});
    
    next();
  };