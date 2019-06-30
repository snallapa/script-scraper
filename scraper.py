import urllib.request
from html.parser import HTMLParser
# BASE_URL = "https://www.springfieldspringfield.co.uk/view_episode_scripts.php?"
# show = "brooklyn-nine-nine"
# fp = urllib.request.urlopen(BASE_URL + "tv-show=" + show)
# episodes = []

# class ShowParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         if tag == "a":
#             for attr in attrs:
#                 if attr[0] == "href" and "&episode=" in attr[1]:
#                     episodes.append(attr[1][attr[1].index("&episode") + 1:])
# class EpisodeParser(HTMLParser):
#     def handle_data(self, data):
#         print(data)
# parser = ShowParser()
# parser.feed(fp.read().decode("utf8"))
# episodeParser = EpisodeParser()
# for episode in episodes:
#     fp = urllib.request.urlopen(BASE_URL + "tv-show={}&{}".format(show, episode))
#     lines = fp.read().decode("utf8")
#     lines = lines[lines.index("<div class=\"scrolling-script-container\">") + 40:]
#     lines = lines[:lines.index("</div>")]
#     lines = lines.lstrip().strip().replace("<br>", "\n")
#     print(lines)
    
# BASE_URL = "http://atla.avatarspirit.net/transcripts.php"
BASE_URL = "http://korra.avatarspirit.net/transcripts.php"
fp = urllib.request.urlopen(BASE_URL)
episodes = []

class ShowParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for attr in attrs:
                if attr[0] == "href" and "num=" in attr[1]:
                    episodes.append(attr[1])
                        
showParser=  ShowParser()
showParser.feed(fp.read().decode("utf8"))
episodes = episodes[7:]
for episode in episodes:
    fp = urllib.request.urlopen(episode)
    lines = fp.read().decode("utf8")
    lines = lines[lines.index("<blockquote>") + 12:lines.index("</blockquote>")]
    print(lines)

