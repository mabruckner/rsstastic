% rebase('templates/base.tpl')
% from util import get_url
<a href="{{ get_url(next) if next is not None else '/' }}">next</a>
<a href="{{ get_url(prev) }}">previous</a>
<a href="/">home</a>
<h2>{{ itemid }} -- {{ timestamp }}</h2>
{{ !data }}
