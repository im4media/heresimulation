from post import Post, Reply
from user import User

class Realm:
    def __init__(self):
        self.posts = []
        self.users = []
        self.average_balance = 0
        self.wallet = 0
        self.should_stop = False
    
    def create_post(self, user, text):
        post = Post(user, text)
        self.posts.append(post)
        user.spend_credit(1)
        self.wallet +=1
        
    def reply_post(self, user, post, text):
        reply = Reply(user, text, post)
        post.replies.append(reply)
        user.spend_credit(1)
        self.wallet +=1

    def upvote_post(self, user, post, credits):
        if user == post.author:
            #print(f"{user.name} can't upvote their own post.")
            return
        post.upvotes += credits
        user.spend_credit(credits)
        post.author.earn_credit(credits)
        
    def downvote_post(self, user, post, credits):
        if user == post.author:
            #print(f"{user.name} can't upvote their own post.")
            return
        post.downvotes += credits
        user.spend_credit(credits)
        self.earn_credit(credits)
        
    def create_user(self, name, initial_credits=0):
        user = User(self,        name, initial_credits)
        self.users.append(user)
        self.average_balance = self.get_average_balance()
        return user
    
    def get_average_balance(self):
        #balances = [user.credits for user in self.users]
        total_balance = sum(u.credits for u in self.users)
        average_balance = total_balance / len(self.users)
        # balances.sort()
        # median = balances[len(balances) // 2]
        return int(average_balance)

    def earn_credit(self, amount):
        self.wallet += amount
    