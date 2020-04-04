import ApolloClient from "apollo-boost";

const client: any = new ApolloClient({
  uri: "http://localhost:8080/v1/graphql",
});
export default client;
