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