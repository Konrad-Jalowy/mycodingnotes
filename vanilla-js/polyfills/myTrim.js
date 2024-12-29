String.prototype.myTrim = function(trimmedChar = " "){
    
    if(trimmedChar.length < 1)
        trimmedChar = " ";

    if(trimmedChar.length > 1)
        trimmedChar = trimmedChar[0];

    let left = 0;
    let right = this.length - 1;

    while(this[left] === trimmedChar){
        left++;
    }

    while(this[right] === trimmedChar){

        if(this[right -1] !== trimmedChar)
            break;

        right--;
    }

    if(left > right)
        return "";

    return this.substring(left, right);
}