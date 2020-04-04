import gql from "graphql-tag";

export const DEATHS = gql`
  query deathsByCountry($country: String!, $limit: Int = 20) {
    deaths(
      where: { place: { _eq: $country } }
      order_by: { timestamp: desc }
      limit: $limit
    ) {
      place
      count
      timestamp
    }
  }
`;
