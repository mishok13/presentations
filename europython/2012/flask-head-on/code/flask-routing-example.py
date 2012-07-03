>>> from werkzeug.routing import Map, Rule
>>> rule = Rule('/yada/daba/'
                '<string(length=2):bar>'
                '/<int:baz>')
>>> Map([rule])
>>> print(rule._regex.pattern)
^\|\/yada\/daba\/(?P<bar>[^/]{2})\/(?P<baz>\d+)$
>>> rule._converters
{'baz': <werkzeug.routing.IntegerConverter>,
 'bar': <werkzeug.routing.UnicodeConverter>}
>>> rule._trace
[(False, '|'), (False, '/yada/daba/'),
 (True, 'bar'), (False, '/'), (True, 'baz')]
>>> rule._weights
[(0, -4), (0, -4), (1, 100), (1, 50)]
