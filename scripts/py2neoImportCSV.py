from py2neo import Graph, Schema

graph = Graph(auth=("neo4j", "137137137"))
graph.delete_all()

# Create Indexes for primary keys of entites
tx = graph.begin()
tx.run('''CREATE INDEX ON :Member(ID)''')
tx.run('''CREATE INDEX ON :Organization(ID)''')
tx.run('''CREATE INDEX ON :User(ID)''')
tx.commit()

# Create Entities
tx = graph.begin()
tx.run('''
    LOAD CSV WITH HEADERS FROM "file:///data/member.csv" AS row
    CREATE (m:Member)
    SET m = row,
        m.ID = toInteger(row.ID),
        m.OrganizationID = toInteger(row.OrganizationID),
        m.UserID = toInteger(row.UserID)
    RETURN m
''')
tx.run('''
    LOAD CSV WITH HEADERS FROM "file:///data/organization.csv" AS row
    CREATE (o:Organization)
    SET o = row,
        o.ID = toInteger(row.ID)
    RETURN o
''')
tx.run('''
    LOAD CSV WITH HEADERS FROM "file:///data/user.csv" AS row
    CREATE (u:User)
    SET u = row,
        u.ID = toInteger(row.ID)
    RETURN u
''')
tx.commit()

# Create Relationships
tx = graph.begin()
tx.run('''
    MATCH (n:User),(m:Member)
    WHERE n.ID = m.UserID
    CREATE (n)-[:MEMBERSHIP]->(m)
''')
tx.run('''
    MATCH (o:Organization),(m:Member)
    WHERE o.ID = m.OrganizationID
    CREATE (o)-[:HAS_MEMBER]->(m)
''')
tx.run('''
    LOAD CSV WITH HEADERS FROM "file:///data/prefers.csv" AS row
    MATCH (m:Member {ID: toInteger(row.MemberID)}),(p:Member {ID: toInteger(row.PreferredMemberID)})
    CREATE (m)-[:PREFERS {rank: toInteger(row.Rank)}]->(p)
''')
tx.run('''
    LOAD CSV WITH HEADERS FROM "file:///data/matched.csv" AS row
    MATCH (b:Member {ID: toInteger(row.BigMemberID)}),(l:Member {ID: toInteger(row.LittleMemberID)})
    CREATE (b)-[:BIG]->(l), (l)-[:LITTLE]->(b)
''')
tx.commit()
