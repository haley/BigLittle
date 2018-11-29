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
    LOAD CSV WITH HEADERS FROM "file:///data/member.csv" AS row
    MATCH (u:User {ID: toInteger(row.UserID)}),(o:Organization {ID: toInteger(row.OrganizationID)})
    CREATE (u)-[:MEMBER {role: row.Role}]->(o)
''')
tx.run('''
    LOAD CSV WITH HEADERS FROM "file:///data/prefer.csv" AS row
    MATCH (u:User {ID: toInteger(row.UserID)}),(p:User {ID: toInteger(row.PreferredUserID)})
    CREATE (u)-[:PREFERS {Rank: toInteger(row.Rank), OrganizationID: toInteger(row.OrganizationID)}]->(p)
''')
tx.run('''
    LOAD CSV WITH HEADERS FROM "file:///data/match.csv" AS row
    MATCH (b:User {ID: toInteger(row.BigUserID)}),(l:User {ID: toInteger(row.LittleUserID)})
    CREATE (b)-[:BIG {OrganizationID: toInteger(row.OrganizationID)}]->(l),
        (l)-[:LITTLE {OrganizationID: toInteger(row.OrganizationID)}]->(b)
''')
tx.commit()
