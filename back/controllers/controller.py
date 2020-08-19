# coding=UTF-8
import os
from youtube_search import YoutubeSearch

MAX_RESULTS = 200


def returnVideos(term):
    searches = YoutubeSearch(term, max_results=MAX_RESULTS).to_dict()

    return searches


def result(term, days):
    return returnVideos(term)
    return {
        "words_titles": ["TESTE", "teste2", "teste3", "teste4", "teste5"],
        "words_descriptions": ["TESTE", "teste2", "teste3", "teste4", "teste5"],
        "days": [
            {"urls": ["sfsdf", "sdfsdfs"]},
            {"urls": ["sfsdf", "sdfsdfs"]},
            {"urls": None},
            {"urls": ["sfsdf", "sdfsdfs"]},
        ],
    }
