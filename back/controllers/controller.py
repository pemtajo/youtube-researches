# coding=UTF-8
import os
from youtube_search import YoutubeSearch
from collections import Counter

MAX_RESULTS = 200


def convertToSeconds(duration):
    minutes, seconds = duration.split(":")
    return int(minutes) * 60 + int(seconds)


def returnVideos(term):
    searches = YoutubeSearch(term, max_results=MAX_RESULTS).to_dict()

    return [
        {
            "id": s["id"],
            "title": s["title"],
            "description": s["long_desc"],
            "duration": convertToSeconds(s["duration"]),
            "used": False,
        }
        for s in searches
    ]


def topWords(strs, top=5):
    s = " ".join(strs)
    sts = s.split(" ")
    return Counter(sts).most_common(top)


def calculateDays(days, videos):
    seconds = [int(d) * 60 for d in days]
    max_seconds = max(seconds)
    watch_in_days = []
    videos_useful = videos
    for s in seconds:
        count = 0
        videos_useful = [v for v in videos_useful if not v["used"]]
        urls = []
        for video in videos_useful:
            if video["duration"] > max_seconds:
                video["used"] = True
            if count + video["duration"] <= s:
                video["used"] = True
                urls.append("http://www.youtube.com/watch?v=%s" % video["id"])
                count += video["duration"]

        watch_in_days.append(urls)

    return watch_in_days


def result(term, days):
    videos = returnVideos(term)
    return {
        "words_titles": topWords([v["title"] for v in videos]),
        "words_descriptions": topWords([v["description"] for v in videos]),
        "days": calculateDays(days, videos),
    }
