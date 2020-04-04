import React from "react";
import CovidTable from "covid-table";
import { ApolloProvider } from "@apollo/react-hooks";
import client from "./apollo-client";

function App() {
  return (
    <ApolloProvider client={client}>
      <h1>Covid-19</h1>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. In ac
        consectetur risus, ac pulvinar odio. Phasellus sit amet dictum orci.
        Vestibulum rutrum posuere nibh, at finibus leo maximus id. In eu leo mi.
        Praesent euismod placerat orci, ut eleifend nunc placerat egestas. Fusce
        pretium purus sit amet est condimentum sodales. Sed sollicitudin elit
        sit amet ligula consequat, eget iaculis nunc tincidunt. Pellentesque
        efficitur aliquet massa quis commodo.
      </p>
      <CovidTable />
    </ApolloProvider>
  );
}

export default App;
