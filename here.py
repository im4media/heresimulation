
import time

from realm import Realm
from user import User
from post import Post, Reply



if __name__ == "__main__":
    #timewarp = 1        #10s *10000 = 100,000 = 30 h

    # _pi = 0.03*timewarp    # Post 
    # _ri = 0.05*timewarp     # Reply
    # _ii = 0.001*timewarp    # Invite
    # _ui = 0.03*timewarp     # Upvote
    # _di = 0.003*timewarp    # Downvote
    # _dwi = 0.01*timewarp    # Deposit/Withdraw

    realm = Realm()
    user = realm.create_user("User 1", 100)
    user = realm.create_user("User 2", 100)
    user = realm.create_user("User 3", 100)
    day = 0

    try:
        while True:
            time.sleep(10)
            # Site statistics
                    
            print("Day:", day)
            print("Number of Users: ", len(realm.users))
            print("Number of Posts: ", len(realm.posts))
            #print("Median Balance: ", site.average_balance)
            
            print("Total economy(in ￠): ", realm.wallet + realm.average_balance*len(realm.users))
            print()
            day +=1

            if len(realm.users)> 5000:
                realm.should_stop = True
                break 

    except KeyboardInterrupt:
        realm.should_stop = True

    # Clean up
    for user in realm.users:
        user.thread.join()
    
    # Final data
    total_replies = 0
    for post in realm.posts:
        total_replies += len(post.replies)
    print("==========")
    print("Total replies:", total_replies)