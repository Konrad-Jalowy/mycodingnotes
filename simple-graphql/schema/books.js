const books = [
    {
      id: "1",
      title: 'The Awakening',
      author: 'Kate Chopin',
    },
    {
      id: "2",
      title: 'City of Glass',
      author: 'Paul Auster',
    },
  ];
  let _id = books.length;

function getNextId(){
    return ++_id;
};

exports.getAllBooks = function(){
    return books;
};

exports.getBookById = function(id){
    return books.find((book) => {
        return book.id === id;
      });
};

exports.addNewBook = function(title, author) {
    let _newId = getNextId();
    const _newBook = {
      id: `${_newId}`,
      title,
      author
    };
  
    books.push(_newBook);
    return _newBook;
  }

exports.addNewBookInput = function(input){
    let _newId = getNextId();
    const _newBook = {
      id: `${_newId}`,
      title: input.title,
      author: input.author
    };
  
    books.push(_newBook);
    return _newBook;
}