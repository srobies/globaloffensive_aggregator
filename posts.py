import praw
import re

def retrieve_posts():
    reddit = praw.Reddit(
        client_id = "mLo_owryg3pRQQ",
        client_secret = "k1aHbkWRVQ4QX7Mkgn9M9oka4i9FIw",
        user_agent = "globalOffensive_aggregator"
        )

    posts = reddit.subreddit("globaloffensive").search('flair:"esports"', time_filter='week', sort='hot')
    post_match_threads = []
    news = []
    clips_fluff = []


    for i in posts:
        link = "https://www.reddit.com" + i.permalink
        post_flair = i.link_flair_text
        post_title = i.title
        if(post_flair.find("Discussion") != -1):
            if(post_title.find("Post-Match Discussion") != -1):
                score = re.findall("\d-\d", i.selftext)
                score[0].strip()
                post_title = post_title[0:post_title.find('/ Post-Match Discussion')-1]
                post_data = {'post_title':post_title, 'score':score[0], 'link':link}
                post_match_threads.append(post_data)
            else:
                post_data = {'post_title':post_title, 'link':link}
                news.append(post_data)
        elif(post_flair.find("Fluff") != -1
                or post_flair.find("Highlight") != -1
                or post_flair.find("Gameplay") != -1):
            post_data = {'post_title':post_title, 'link':link}
            clips_fluff.append(post_data)
    return post_match_threads, news, clips_fluff

def format_post_data(post_list, post_data, number_of_posts):
    # print('\033[1m' + title)
    # print('\033[0m',end='')
    # total_string = '\033[1m' + title 
    # total_string += '\033[0m'
    total_string = ""
    for i in range(0, number_of_posts):
        for j in post_data:
            if(len(post_data) == 3):
                if(j == "post_title"):
                    # print(f"{post_list[i][j]}")
                    total_string += post_list[i][j]
                elif(j == "score"):
                    total_string += f" ({post_list[i][j]})\n"
                else:
                    # print(f"\t{post_list[i][j]}")
                    total_string += "\t" + post_list[i][j]
                    total_string += "\n"
            else:
                if(j == "post_title"):
                    # print(f"{post_list[i][j]}")
                    total_string += post_list[i][j]
                    total_string += "\n"
                else:
                    total_string += "\t" + post_list[i][j]
                    total_string += "\n"
        # total_string += "\n"
        # print()
    return total_string
    

# post_match_threads, news, clips_fluff = retrieve_posts()
# test0 = format_post_data(post_match_threads, list(post_match_threads[0].keys()), 15)
# test1 = format_post_data(news, list(news[0].keys()), 5)
# test2 = format_post_data(clips_fluff, list(clips_fluff[0].keys()), 2)
# print(test1)
# print(test2)
