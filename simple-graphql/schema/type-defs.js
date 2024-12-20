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