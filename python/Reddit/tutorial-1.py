import praw


reddit = praw.Reddit(
                     client_id='JWpGkX-s6DiVtg',
                     client_secret='9KB_5-S4X0yAhwfk-Ijvgo6bOmE',
                     username='unknown_guest17',
                     password='Gingerbread235',
                     user_agent='pythonscript',
                    )


subreddit = reddit.subreddit('python')


hot = subreddit.hot(limit=10)


for sub in hot:
    if not sub.stickied:  # Donot print the pinned post(s)
        print(
                "Title: {}, Upvotes: {}, Downvotes: {}, Visited: {}"
                .format(
                    sub.title,
                    sub.ups,
                    sub.downs,
                    sub.visited
                    )
                )

