The program simulates a new type of social media platform where users can create posts, reply to posts, invite new users, upvote and downvote posts, with their stakes(￠).

Users are created by the realm initially and later by invitation from existing users. Each user runs in an independent will(thread) and has a wallet to hold credit. They spend one credit to create a post or reply, the interval of post and reply is random and regulated by several different personas. The realm holds all the posts and replies for data provision.

Users can also upvote a post by giving one to n cents, or downvote a post by giving it one to n cents as well. The realm receives the downvote credits, while the upvote credits are paid to the user who created the post.

Users also have the ability to deposit credit randomly if their credit is less than the average balance of all users.

Based on progressive data, the realm is to print statistics of users, posts, total credits and median balance of all users. We will stop the simulation at a level of users(e.g. 5000) or by force. In the implementation, it provided a way to stop all the threads by using join() function and also by using the flag variable.

## All rules we may consider to put into HIP:
1. Post with 1￠ (or 10x if it's with 10 minutes, and so on)
2. Reply with 1￠ (same anti-spam measure like post)
3. Post with image 2￠/image
4. Upvote with 1￠ or any amount(n￠ won't change the weight much), all upvote credits go to post creator
5. Downvote with 1￠ or any amount(n￠ won't change the weight much), all downvote credits go to system
6. Reputation will build up along with continuous activities
7. Top news emerges by open algorithm
8. Topics curated by higher reputation players
9. Commands and extensions (archive, translate, etc.) 