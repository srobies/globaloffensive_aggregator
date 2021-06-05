import curses
import posts

post_match_threads, news, clips_fluff = posts.retrieve_posts()

def main():
    curses.wrapper(curses_main)

def add_text(w, title, main_text):
    try:
        w.addstr(title+"\n",curses.A_BOLD)
        w.addstr(main_text+"\n")
    except curses.error:
        pass

def curses_main(w):
    post_match_threads, news, clips_fluff = posts.retrieve_posts()
    thread_text = posts.format_post_data(post_match_threads, list(post_match_threads[0].keys()), 15)
    news_text = posts.format_post_data(news, list(news[0].keys()), 5)
    fluff_text = posts.format_post_data(clips_fluff, list(clips_fluff[0].keys()), 2)
    print(news_text)
    print(fluff_text)
    add_text(w, "Post-Match Threads", thread_text)
    add_text(w, "News", news_text)
    add_text(w, "Fluff", fluff_text)
    # w.addstr("Post-Match Threads\n",curses.A_BOLD)
    # w.addstr(thread_text)
    # w.addstr("News\n",curses.A_BOLD)
    # w.addstr(news_text)
    # w.addstr("Fluff\n",curses.A_BOLD)
    # w.addstr(fluff_text)
    w.refresh()
    w.getch()

main()
