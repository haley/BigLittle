# BigLittle
BigLittle is a system inteded to help match bigs and littles in college organizations. If you have not heard of "bigs" and "littles" before, they are basically pairnings of uperclassmen mentors and underclassmen mentees in some college organizations. Using a n=Neo4j database and a genetic algorithm (TODO), BigLittle will allow users to input their information, and eventually use that information to match bigs and littles within organizations.

# How to install and use our database
1. You'll need to get the Neo4j desktop app to locally upload member data, view data, and eventually run the genetic algorithm which will use the data in the local databse. This page has some detailed instructions to ensure you get Neo4j up and running. http://bjohnson.lmu.build/cmsi486web/neo4jinstall.html. As these instruction say, create a new project, and a new Graph, but don't run it yet.
2. Clone this repo, and make new csv files for your organization. Once you have these files, you'll need to put them within the "import" folder within your Neo4j desktop installation. The path should look something like the following... D:\username\neo4jDatabases\database-c56f86db-f3fd-478c-8b57-5f82bd491f40\installation-3.4.1\import
3. With the data within the import file, you can now run the Neo4j server within the desktop app. Now, ensure you have the latest version of Python3, and pip install py2neo. Next, run the python scripts on our repo to upload your data into Neo4j. You should be able to see the full graph of your data in the Neo4j desktop app now!
4. At this point, you would be able to run the matching algorithm within our scripts folder, but it does not yet exist. Keep a look out for it!

# Example Queries

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
   
# Big Little ERD

![ERD](./resources/finalERD.png)
