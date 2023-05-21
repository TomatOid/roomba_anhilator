import praw

print("Create a new app at https://www.reddit.com/prefs/apps, make sure you select \'script\' and put any url for redirect url")

bot_id = input("paste client ID (the string under \"personal use script\"): ")
bot_secret = input("paste secret: ")
bot_username = input("enter your reddit username: ")
bot_password = input("enter your reddit password: ")

reddit = praw.Reddit(
        client_id = bot_id,
        client_secret = bot_secret,
        password = bot_password,
        user_agent = "python",
        username = bot_username,
)

enemy = reddit.redditor("196_roomba")
counter = 0
for comment in enemy.comments.hot(limit=None):
    counter += 1
    comment.downvote()
    print("\rdownvoted comment #", counter, sep = '', end = '')


