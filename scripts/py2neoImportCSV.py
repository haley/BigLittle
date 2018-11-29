from py2neo import Graph, Schema

create_index = '''CREATE INDEX ON :{entity}(ID)'''

def _csv_to_neo_entity(path, entity):
    return f'''
        LOAD CSV WITH HEADERS FROM "{path}" AS row
        CREATE (n:{entity})
        SET n = row,
            n.ID = toInteger(row.ID)
        RETURN n
    '''

def _create_relationship(relater, relatee, relation):
    return f'''
        MATCH (n:{relater}),(m:{relatee})
        WHERE n.ID = m.{relater}ID
        CREATE (n)-[:{relation}]->(m)
    '''

graph = Graph(auth=("neo4j", "137137137"))
graph.delete_all()

tx = graph.begin()
tx.run('''CREATE INDEX ON :Member(ID)''')
tx.run('''CREATE INDEX ON :Organization(ID)''')
tx.run('''CREATE INDEX ON :User(ID)''')
tx.commit()

tx = graph.begin()
tx.run(_csv_to_neo_entity(path="file:///data/member.csv", entity="Member"))
tx.run(_csv_to_neo_entity(path="file:///data/organization.csv", entity="Organization"))
tx.run(_csv_to_neo_entity(path="file:///data/user.csv", entity="User"))
tx.commit()

tx = graph.begin()
tx.run(_create_relationship(relater="User", relatee="Member", relation="MEMBERSHIP"))
tx.run(_create_relationship(relater="Organization", relatee="Member", relation="HAS_MEMBER"))
tx.commit()

tx = graph.begin()
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
