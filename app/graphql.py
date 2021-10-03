import graphene
from starlette.graphql import GraphQLApp


def start_graphql(app, database):

    class Author(graphene.ObjectType):
        name = graphene.String(default_value="Andrey")
        surname = graphene.String(default_value="Shein")

    class Note(graphene.ObjectType):
        topic = graphene.String()
        content = graphene.String()
        author = graphene.Field(Author)

        def resolve_author(self, info):
            return Author()

    class Query(graphene.ObjectType):
        get_notes = graphene.List(Note, offset=graphene.Int(), count=graphene.Int())

        def resolve_get_notes(self, info, offset: int, count: int):
            full = list(map(lambda note: Note(topic=note["topic"], content=note["content"]),
                            database.notes))
            return full[offset:][:count]

    app.add_route("/notes", GraphQLApp(schema=graphene.Schema(query=Query)))
