import React from "react";
import { DEATHS } from "./queries";
import { useQuery } from "@apollo/react-hooks";

const CovidTable: React.SFC = () => {
  const { loading, data, error } = useQuery(DEATHS, {
    variables: {
      country: "Italy-",
    },
  });
  if (loading) return <span>Loading</span>;
  if (error) return <span>Error: {JSON.stringify(error)}</span>;

  return <div>{JSON.stringify(data["deaths"])}</div>;
};

export default CovidTable;
