from typing import List, Set
import re
import math


class KeywordExtractor:

    EXTRACTOR_THRESHOLD = 0.06
    SPECIFIC_WORD_PATTERN = r'(?=((\s|^){}(\s|$)))'

    @staticmethod
    def calculate_term_frequency(word, text):
        pattern = KeywordExtractor.SPECIFIC_WORD_PATTERN.format(word)
        all_words = text.split(" ")
        occurrences = re.findall(pattern, text, re.IGNORECASE)

        return len(occurrences) / len(all_words)


    @staticmethod
    def extract_keywords(corpus: Set[str], text: str) -> Set[str]:
        # relevant for scenario 1 & 3
        words = set(KeywordExtractor.clean_words(text.split(" ")))
        cleaned_text = KeywordExtractor.clean_text(text)
        cleaned_corpus = [KeywordExtractor.clean_text(d) for d in corpus]

        tf = {}

        for w in words:
            tf[w] = KeywordExtractor.calculate_term_frequency(w, cleaned_text)

        idf = {}
        for w in words:
            idf[w] = 1
            for d in cleaned_corpus:
                if re.search(KeywordExtractor.SPECIFIC_WORD_PATTERN.format(w), d, re.IGNORECASE) is not None:
                    idf[w] = idf[w] + 1
            
            
            idf[w] = math.log10(len(cleaned_corpus) / idf[w]) 

        tf_idf = [{w: tf[w]*(idf[w] if idf[w] is not None else 0)} for w in tf.keys()]
        result = {list(x.keys())[0] for x in tf_idf if list(x.values())[0] > KeywordExtractor.EXTRACTOR_THRESHOLD}

        if len(result) == 0:
            sorted_result = sorted(tf_idf, key=lambda x: list(x.values())[0], reverse=True)[:3]
            result = {list(x.keys())[0] for x in sorted_result}

        return result


    @staticmethod
    def clean_text(text: str) -> str:
        return " ".join(KeywordExtractor.clean_words(text.split(" ")))

    @staticmethod
    def clean_words(words: List[str]) -> List[str]:
        advanced_split_words = re.split(" |\/|_|\n|\r|\t", " ".join(words))

        return [re.sub(r'\?|\.|\!|\(|\)|;|:|,', '', w).lower() for w in advanced_split_words if re.sub(r'\W', '', w) != ""]

corpus = [
    "python is a great programming language",
    "django is a great web framework",
    "it-jobs.de loves to uses python and django because they are great",
    "Tenhil is the parent company of it-jobs.de and is a great company",
    "check out their profile at https://platform.entwicklerheld.de/company/tenhil-gmbh-co-kg"
]

text = """job it-jobs jobby job2 job3 job4 job5 job6 job7 entwicklerheld entwicklerheld entwicklerinnen"""

print(KeywordExtractor.extract_keywords(corpus, text))

#unclean_list = ["Luminaire/lamp ", "(amazon),", "YOUR TASKS:", "advantage.", "interested?", "...", "!", "html(5)", "front-end", "back-end", "python;", "amazon"]

#print(KeywordExtractor.clean_words(unclean_list))