import difflib


class Match:
    def fuzzy_matching(self, string1, string2):
        s = difflib.SequenceMatcher(None, string1, string2)
        similarity = s.ratio()
        return similarity