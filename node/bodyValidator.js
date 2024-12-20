//long time ago when i didnt know about express-validator package i guess


//helper function for clearer code
function requiredEnabled(fieldObj){
    if(!Object.hasOwn(fieldObj, "required"))
        return false;
    return fieldObj.required;
}

function notEmptyEnabled(fieldObj){
    if(!Object.hasOwn(fieldObj, "notEmpty"))
        return false;
    return fieldObj.notEmpty;
}

function hasSpecifiedType(fieldObj){
    return Object.hasOwn(fieldObj, 'type');
}

function minMaxErrMsg(fieldObj){
    if(Object.hasOwn(fieldObj, "min") && Object.hasOwn(fieldObj, "max")){
        return `Field ${fieldObj.name} must be >= ${fieldObj.min} and <= ${fieldObj.max}`;
    }
    if(Object.hasOwn(fieldObj, "min") && !Object.hasOwn(fieldObj, "max")){
        return `Field ${fieldObj.name} must be >= ${fieldObj.min}`;
    }
    if(!Object.hasOwn(fieldObj, "min") && Object.hasOwn(fieldObj, "max")){
        return `Field ${fieldObj.name} must be <= ${fieldObj.max}`;
    }
}


function getMinMax(fieldObj){
    const min = Object.hasOwn(fieldObj, "min") ? fieldObj.min : Number.NEGATIVE_INFINITY;
    const max = Object.hasOwn(fieldObj, "max") ? fieldObj.max : Number.POSITIVE_INFINITY;
    return {min, max};
}

function hasMinOrMax(fieldObj){
    return Object.hasOwn(fieldObj, "min") || Object.hasOwn(fieldObj, "max");
}

class BodyValidator {
    constructor(body, fields) {
      this.errors = [];
      this.body = body;
      this.fields = [...fields];
    }

    //TODO: validate fields, return error-list

    _addErrorMessage(field, message){
        this.errors.push({field: field, message: message});
    }

    _bodyHas(fieldname){
        return Object.hasOwn(this.body, fieldname)
    }

    _bodyGet(fieldname){
        return this.body[fieldname];
    }

    _defaultCheck(fieldObj){
        if(!Object.hasOwn(fieldObj, "default"))
            return;
        if(this._bodyHas(fieldObj.name))
            return;
        this.body[fieldObj.name] = fieldObj.default;
    }

    _validateField(fieldObj){

        const _requiredEnabled = requiredEnabled(fieldObj);
        const _bodyHasThisField = this._bodyHas(fieldObj.name);

        if(_requiredEnabled){
            if(!_bodyHasThisField){
                    this._addErrorMessage(fieldObj.name, `Field ${fieldObj.name} is required`);
            }
        }

        if(!_bodyHasThisField){
            //no need to validate further
            return;
        }

        const _val = this._bodyGet(fieldObj.name);

        const _hasSpecifiedType = hasSpecifiedType(fieldObj);

        if(_hasSpecifiedType){
            if(fieldObj.type !== typeof this.body[fieldObj.name]){
                this._addErrorMessage(fieldObj.name, `Field ${fieldObj.name} must be of type ${fieldObj.type}`)
            }
        }

        const _notEmptyEnabled = notEmptyEnabled(fieldObj);

        if(_notEmptyEnabled){
            if(_val === "" ){
                this._addErrorMessage(fieldObj.name,`Field ${fieldObj.name} cant be empty`);
            }
        }

        const _hasMinOrMax = hasMinOrMax(fieldObj);

        if(_hasMinOrMax){

            const {min, max} = getMinMax(fieldObj);

            if((_val > max) || (_val < min) ){
                const _errMsg = minMaxErrMsg(fieldObj);
                this._addErrorMessage(fieldObj.name, _errMsg);
                }
        }

        return true;
    }

    _validateFields(){
        for (const fieldObj of this.fields) {
            this._defaultCheck(fieldObj);
            this._validateField(fieldObj);
        }
        return true;
    }

    validate(){
        this._validateFields();
        return this.errors;
    }

  }

  module.exports = BodyValidator;