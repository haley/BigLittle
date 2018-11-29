# Preliminary Database Demonstration

### Edward Bachoura, Brian Joerger, Haley Fletcher

##### November 27th, 2018



#### Big Little ERD

![ERD](../resources/detailedERD.png)



##### Example Queries

1. Access the email of a specific member.

   ```
   Match (u:User)-[:MEMBERSHIP]->(Member {ID: 17})
   Return u.Email
   ```


2. Access a specific Users related Member entities, specified by the user's first and last name.

   ```
   Match (User {FirstName: "Waluigi", LastName:"Jones"})-[:MEMBERSHIP]->(m:Member)
   Return m
   ```

3. Access the User for a Member's most preffered Member.

   ```
   Match (m:Member {ID: 17})-[:PREFERS {rank: 1}]->(n:Member)<-[:MEMBERSHIP]-(u:User)
   Return u
   ```

4. Access all the matches for a specific organization.

   ```
   Match (Organization {ID: 0})-[:HAS_MEMBER]->(Member)-[b:BIG]->(Member)
   Return b
   ```

5. Access all of the organizations that a user is involved in.

   ```
   Match (u:User)-[:MEMBERSHIP]->(Member)<-[:HAS_MEMBER]-(Organization {ID: 0})
   Return u
   ```
