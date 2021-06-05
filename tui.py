import curses
import posts

post_match_threads, news, clips_fluff = posts.retrieve_posts()

def main():
    curses.wrapper(curses_main)

def curses_main(w):
    # w.addstr("test")
    post_match_threads, news, clips_fluff = posts.retrieve_posts()
    thread_text = posts.format_post_data('Post-Match Threads', post_match_threads, list(post_match_threads[0].keys()), 15)
    # news_text = posts.format_post_data('News', news, list(news[0].keys()), 5)
    # fluff_text = posts.format_post_data('Fluff', clips_fluff, list(clips_fluff[0].keys()), 2)
    w.addstr("Post-Match Threads",curses.A_BOLD)
    w.addstr(thread_text)

    w.refresh()
    w.getch()

main()
