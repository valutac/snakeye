class Project(object):
    def __init__(self, name="", version="", author="", email="", description="", long_description="", url="",
                 license_type=""):
        self.name = name
        self.version = version
        self.author = author
        self.email = email
        self.description = description
        self.long_description = long_description
        self.url = url
        self.license_type = license_type

    def to_ctx(self):
        return {
            'pkg_name': self.name,
            'pkg_version': self.version,
            'author': self.author,
            'author_email': self.email,
            'description': self.description,
            'long_description': self.long_description,
            'url': self.url,
        }

    def to_flit_metadata(self):
        return {
            'module': self.name,
            'author': self.author,
            'author-email': self.email,
            'home-page': self.url,
            'requires': ["flit"],
            'requires-python': 3,
            'description-file': 'README.md',
        }
