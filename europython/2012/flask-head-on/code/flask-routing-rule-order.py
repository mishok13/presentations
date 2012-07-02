class Rule(RuleFactory):

    def match_compare_key(self):
        return (bool(self.arguments),
                -len(self._weights),
                self._weights)

# Somewhere in Map implementation

self._rules.sort(
    key=lambda x: x.match_compare_key())
