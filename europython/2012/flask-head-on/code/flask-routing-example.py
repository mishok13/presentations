>>> from werkzeug.routing import Map, Rule
>>> r = Rule('/foo/<string(length=2):bar>'
         '/<int:baz>')
>>> m = Map()
>>> r.bind(m)
>>> print(r._regex.pattern)
^\|\/foo\/(?P<bar>[^/]{2})\/(?P<baz>\d+)$
>>> r._converters
{'baz': <werkzeug.routing.IntegerConverter>,
 'bar': <werkzeug.routing.UnicodeConverter>}
