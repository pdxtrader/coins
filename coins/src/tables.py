from sqlalchemy import Table, Column, Integer, String, ForeignKey

slams = Table(
    'slams', meta,
    Column('name', String, primary_key=True),
    Column('country', String)
)

results = Table(
    'results', meta,
    Column('slam', String, ForeignKey('slams.name')),
    Column('year', Integer),
    Column('result', String)
)

# Create the above tables
meta.create_all(con)
