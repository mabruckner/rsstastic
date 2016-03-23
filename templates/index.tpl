% rebase('templates/base.tpl')
% from util import get_url
<a href="/reload">reload</a>
<h2>Unread</h2>
<ul>
    % for item in unread :
        % iid = item['id']
        <li><a href="{{get_url(iid)}}">{{ item['timestamp'] }} -- {{ item['id'] }}</a></li>
    % end 
</ul>
<h2>Read</h2>
<ul>
    % for item in read :
        % iid = item['id']
        <li><a href="{{get_url(iid)}}">{{ item['timestamp'] }} -- {{ item['id'] }}</a></li>
    % end 
</ul>
