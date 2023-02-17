
import random
import threading
import time

from post import Post, Reply

PERSONAS = [{"_pt":0.05, "_rt":0.05, "_it": 0.001, "_ut": 0.06, "_dt": 0.01, "_dwt": 0.001}, 
            {"_pt":0.04, "_rt":0.06, "_it": 0.002, "_ut": 0.07, "_dt": 0.02, "_dwt": 0.002}, 
            {"_pt":0.01, "_rt":0.02, "_it": 0.003, "_ut": 0.2, "_dt": 0.02, "_dwt": 0.04}, 
            {"_pt":0.005, "_rt":0.01, "_it": 0.001, "_ut": 0.09, "_dt": 0.01, "_dwt": 0.05},
            {"_pt":0.001, "_rt":0.001, "_it": 0.001, "_ut": 0.2, "_dt": 0.03, "_dwt": 0.09}

        ]


class User:
    def __init__(self, realm, name, initial_credits=0):
        self.realm = realm
        self.name = name
        self.credits = initial_credits
        self.persona = random.choice(PERSONAS)
        #print(self.persona)

        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def run(self):
        while not self.realm.should_stop:
            if random.random() < self.persona['_pt'] and self.credits>0:
                self.create_post("Hello, World!")
            if random.random() < self.persona['_rt'] and self.credits>0:
                self.reply_random_post("Hello, World!")
            if random.random() < self.persona['_it'] and self.credits>0:
                self.invite_new_user()
            if random.random() < self.persona['_ut'] and self.credits>0:
                self.upvote_random_post(1)
            if random.random() < self.persona['_dt'] and self.credits>0:
                self.downvote_random_post(1)
            if self.credits <= self.realm.average_balance and random.random() < self.persona['_dwt']:
                self.deposit_credit()
            time.sleep(0.1)

    def create_post(self, text):
        post = Post(self, text)
        self.realm.create_post(self, text)

    def reply_random_post(self, text):
        if len(self.realm.posts) > 0:
            post = random.choice(self.realm.posts)
            self.realm.reply_post(self, post, text)

    def invite_new_user(self):
        user = self.realm.create_user(name=f"user{len(self.realm.users)}")
        user.earn_credit(100)

    def upvote_random_post(self, credits):
        if len(self.realm.posts) > 0:
            post = random.choice(self.realm.posts)
            self.realm.upvote_post(self, post, credits)

    def downvote_random_post(self, credits):
        if len(self.realm.posts) > 0:
            post = random.choice(self.realm.posts)
            self.realm.downvote_post(self, post, credits)
            
    def spend_credit(self, amount):
        self.credits -= amount
        
    def earn_credit(self, amount):
        self.credits += amount
        
    def deposit_credit(self):
        deposit_amount = random.randrange(1, self.realm.average_balance if self.realm.average_balance > 100 else 101)
        self.credits += deposit_amount


