from typing import override

from albert import (
    Action,
    PluginInstance,
    Query,
    StandardItem,
    TriggerQueryHandler,
    runDetachedProcess,
)

md_iid = '3.0'
md_version = '1.4'
md_name = 'GoldenDict Steven'
md_description = 'Searches in GoldenDict'
md_license = 'MIT'
md_url = 'https://github.com/stevenxxiu/albert_goldendict_steven'
md_authors = ['@stevenxxiu']
md_bin_dependencies = ['goldendict']

ICON_URL = 'xdg:goldendict'


class Plugin(PluginInstance, TriggerQueryHandler):
    def __init__(self):
        PluginInstance.__init__(self)
        TriggerQueryHandler.__init__(self)

    @override
    def synopsis(self, _query: str) -> str:
        return 'query'

    @override
    def defaultTrigger(self):
        return 'gd '

    @override
    def handleTriggerQuery(self, query: Query) -> None:
        query_str = query.string.strip()
        if not query_str:
            return

        item = StandardItem(
            id=md_name,
            text=md_name,
            subtext=f'Look up {query_str} using <i>GoldenDict</i>',
            iconUrls=[ICON_URL],
            actions=[Action(md_name, md_name, lambda: runDetachedProcess(['goldendict', query_str]))],
        )
        query.add(item)  # pyright: ignore[reportUnknownMemberType]
