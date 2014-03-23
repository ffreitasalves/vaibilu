# coding: utf-8

def get_hn(qtd = 1):
    #pega as Notícias do Hacker News
    from hn import HN

    novidades = HN()
    results = []
    for s in novidades.get_stories(story_type='newest', limit = qtd):
        results.append(s.link)

    if qtd > 1:
        return results
    else:
        return results[0]