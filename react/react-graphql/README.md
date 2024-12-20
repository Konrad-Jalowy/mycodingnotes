# Simple React-Graphql setup

## Install
Use this command:
```sh
npm install @apollo/client
```

## Setup App js
Like this:
```js
import { ApolloClient, InMemoryCache, ApolloProvider} from "@apollo/client";

function App() {
  const client = new ApolloClient({
    cache: new InMemoryCache(),
    uri: "http://localhost:4000/graphql",
  });
  return (
    <ApolloProvider client={client}>
        
    </ApolloProvider>
  );
}

export default App;
```

## useQuery
Import useQuery and prepare query using gql
```js
import { useQuery, gql} from "@apollo/client";
const QUERY_ALL_BOOKS = gql`
  query GetAllBooks {
    books {
      id
      title 
      author
    }
  }
`;
```
Rest is pretty self-descriptive:
```js
function AllBooks(){
  const { data, loading, refetch } = useQuery(QUERY_ALL_BOOKS);
  if (loading) {
    return <h1> DATA IS LOADING...</h1>;
  }
    return (
        <>
        <ul>
        {data &&
        data.books.map((book) => {
          return (
            <li key={book.id}>
             <em>{book.title}</em> by <strong>{book.author}</strong>
            </li>
          );
        })}
        </ul>
        <button onClick={() => refetch()}>Refetch</button>
        </>
    );
};

export {AllBooks};
```
Theres one thing you should watch out for - **error means error, like something went wrong**. Situations in which data is null, or data.books is null are not treated as error.  

**In graphql you can ask for item, with non-existing id and you will get data.item equal to null**. It will not be an error (like in REST APIs). And data itself can be undefined. So you need to be extra careful with these.

## useLazyQuery
First prepare our graphql query:
```js
import { useState, useEffect } from "react";
import { useLazyQuery, gql } from "@apollo/client";
const GET_BOOK_BY_ID = gql`
  query Book($id: ID!) {
    book(id: $id) {
      id,
      title,
      author
    }
  }
`;
```
Ok done now the rest:
```js
function OneBook(){
    const [bookSearched, setBookSearched] = useState(1);
   
    const [
        fetchBook,
        { data, error, loading },
      ] = useLazyQuery(GET_BOOK_BY_ID);

      useEffect(() => {
        fetchBook({variables: {id: `${bookSearched}`}});
      }, [bookSearched, fetchBook]);
```
Ok self descriptive, now ifs:
```js
if(loading){
        return <h1>Loading</h1>
      }
      if(error){
        return <h1>Error</h1>
      }
      if(data?.book === null){
        return (<>
        <input type="number" value={bookSearched} onChange={(e) => {
            setBookSearched(e.target.value);
        }} />
        <h1>Such book doesnt exist</h1>
        </>
        );
      }
```
Main return:
```js
return (
        <>
        <input type="number" value={bookSearched} onChange={(e) => {
            setBookSearched(e.target.value);
        }} />
        <p>Book title: {data && data.book && data.book.title}</p>
        <p>Book author: {data && data.book && data.book.author}</p>
        </>
    );
};
```
And **DISCLAIMER**, one more time:  

Theres one thing you should watch out for - **error means error, like something went wrong**. Situations in which data is null, or data.books is null are not treated as error.  

**In graphql you can ask for item, with non-existing id and you will get data.item equal to null**. It will not be an error (like in REST APIs). And data itself can be undefined. So you need to be extra careful with these.

## useMutation
Its simple. First, define mutation to make:
```js
import { useState } from "react";
import {gql, useMutation} from "@apollo/client"

const CREATE_BOOK_MUTATION = gql`
  mutation CreateBook($input: createBookInput!) {
    addNewBookIpt(input: $input) {
      id
    }
  }
`;
```
**Always remember about return type - mutations also have one. And you must specify what the mutation returns**.

Ok, heres component:
```js
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
```
Simple.