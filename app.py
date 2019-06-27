from flask import Flask
from flask_graphql import GraphQLView

from .schema import app_schema

# Create flask app
app = Flask(__name__)

# Create the GraphQL view for flask
graphql_view = GraphQLView.as_view('graphql', schema=app_schema, graphiql=True)

# Attach graphql view to flask
app.add_url_rule('/', view_func=graphql_view)
