class ResultHandler:
    @classmethod
    def parse_results(cls, response):
        results = []
        for each in response:
            results.append(each)
        return results
