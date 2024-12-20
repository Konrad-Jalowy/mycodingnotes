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