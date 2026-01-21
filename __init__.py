from collections.abc import Generator
from typing import override

from albert import (
    Action,
    GeneratorQueryHandler,
    Icon,
    Item,
    PluginInstance,
    QueryContext,
    StandardItem,
    runDetachedProcess,
)

md_iid = '5.0'
md_version = '1.5'
md_name = 'GoldenDict Steven'
md_description = 'Searches in GoldenDict'
md_license = 'MIT'
md_url = 'https://github.com/stevenxxiu/albert_goldendict_steven'
md_authors = ['@stevenxxiu']
md_bin_dependencies = ['goldendict']

ICON_NAME = 'goldendict'


class Plugin(PluginInstance, GeneratorQueryHandler):
    def __init__(self):
        PluginInstance.__init__(self)
        GeneratorQueryHandler.__init__(self)

    @override
    def synopsis(self, _query: str) -> str:
        return 'query'

    @override
    def defaultTrigger(self):
        return 'gd '

    @override
    def items(self, ctx: QueryContext) -> Generator[list[Item]]:
        query_str = ctx.query.strip()
        if not query_str:
            return

        item = StandardItem(
            id='goldendict',
            text=md_name,
            subtext=f'Look up {query_str} using <i>GoldenDict</i>',
            icon_factory=lambda: Icon.theme(ICON_NAME),
            actions=[Action('goldendict', md_name, lambda: runDetachedProcess(['goldendict', query_str]))],
        )
        yield [item]
