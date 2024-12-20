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