from flask.ext.mongokit import Document
from datetime import datetime

class Post(Document):
    __collection__= "posts"
    use_schemaless = True
    structure = {
        "titel": unicode,
        "body": {"html":unicode,
                 "md": unicode},
        "excerpt":unicode,
        "datum": datetime,
        "categorie": unicode,
        "pub": bool,
        "tags": list,
        "last_updated": datetime
    }
    required_fields = []
    use_dot_notation = True
