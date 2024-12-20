import { useState } from "react";
import {gql, useMutation} from "@apollo/client"

const CREATE_BOOK_MUTATION = gql`
  mutation CreateBook($input: createBookInput!) {
    addNewBookIpt(input: $input) {
      id
    }
  }
`;
function AddBook(){
    const [title, setTitle] = useState("");
    const [author, setAuthor] = useState("");
    const [createBook] = useMutation(CREATE_BOOK_MUTATION);
    return (
        <>
        <input 
        type="text"
        placeholder="title"
        onChange={(event) => {
            setTitle(event.target.value);
          }}
        />
        <input 
        type="text"
        placeholder="author"
        onChange={(event) => {
            setAuthor(event.target.value);
          }}
         />
         <button  onClick={() => {
            console.log(title, author)
            createBook({
              variables: {
                input: { title: title, author: author},
              },
            });
        }}>Add</button>
        <p>Add book not implemented yet!</p>
        </>
    );
};

export {AddBook};