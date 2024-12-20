# Simple graphql
How to setup and make basic tasks using graphql simple tutorial/reminder

## What graphql is
Its not a database (in our example we use in-memory storage). Its rather alternative to rest api. One endpoint, one method (usually POST) and one query language common to all apis using graphql. One thing you must learn using api is what are the types and what are their fields. Thats not a lot compared to learning all the endpoints and typical things that come with rest api.

## How to start
- Create server directory
- create package.json (npm init -y)
- Install these packages
```sh
npm i apollo-server graphql
```
Btw i hope you have nodemon globally installed, if not, consider installing it.
Your server will look like that:
```js
const { ApolloServer } = require("apollo-server");

const typeDefs = require("./schema/type-defs");
const resolvers = require("./schema/resolvers");

const server = new ApolloServer({ typeDefs, resolvers });

server.listen().then(({ url }) => {
  console.log(`YOUR API IS RUNNING AT: ${url} :)`);
});
```
Of course we need to create those resolvers and typedefs.
## typedefs and resolvers
Heres our example
```js
const { gql } = require("apollo-server");

const typeDefs = gql`
  type Book {
    id: ID!
    title: String!
    author: String!
  }
  type Query {
    books: [Book]
    book(id: ID!): Book
  }
   input createBookInput {
    title: String!
    author: String!
    
  }
   type Mutation {
  addNewBook(title: String! author: String!): Book
  addNewBookIpt(input: createBookInput!): Book
  }
`;
module.exports = typeDefs;
```
Btw its tagged template literal function. They are not very often found, but they exist. Ok, so we have scalar types that are used to compose user-defined types.

We also have queries, input types (you dont need those), and mutation types. 