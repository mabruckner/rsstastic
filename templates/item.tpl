% rebase('templates/base.tpl')
% from util import get_url
% if next_unread is not None :
    <a href="{{ get_url(next_unread) }}">next_unread</a>
% end
<a href="{{ get_url(next) if next is not None else '/' }}">next</a>
<a href="{{ get_url(prev) }}">previous</a>
<a href="/">home</a>
<h2>{{ itemid }} -- {{ timestamp }}</h2>
{{ !data }}
