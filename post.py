class Post:
    def __init__(self, author, text):
        self.author = author
        self.text = text
        self.upvotes = 0
        self.downvotes = 0
        self.replies = []

class Reply(Post):
    def __init__(self, author, text, root_post):
        super().__init__(author, text)
        self.root_post = root_post