function isValidTagname(tagname) {
    return document.createElement(tagname).toString() != "[object HTMLUnknownElement]";
  }