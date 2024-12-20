const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
  firstName: {
    type: String,
    required: true,
  },
  lastName: {
    type: String,
    required: true,
  },
  age: {
    type: Number,
    required: true
  },
  cash: {
    type: Number,
    required: true,
    default: 0,
    min: 0,
  }
  
}, {timestamps: true, 
    toJSON: {virtuals: true}, 
    toObject: {virtuals: true}
   }
);

userSchema.virtual('fullname').get(function() {
    return this.firstName + " " + this.lastName;
  });
userSchema.virtual('adult').get(function() {
    return this.age >= 18;
  });


module.exports = mongoose.model('User', userSchema);