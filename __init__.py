from albert import Action, Item, Query, QueryHandler, runDetachedProcess  # pylint: disable=import-error


md_iid = '0.5'
md_version = '1.0'
md_name = 'GoldenDict Steven'
md_description = 'Searches in GoldenDict'
md_url = 'https://github.com/stevenxxiu/albert_goldendict_steven'
md_maintainers = '@stevenxxiu'
md_bin_dependencies = ['goldendict']

ICON_PATH = 'xdg:goldendict'


class Plugin(QueryHandler):
    def id(self) -> str:
        return __name__

    def name(self) -> str:
        return md_name

    def description(self) -> str:
        return md_description

    def defaultTrigger(self) -> str:
        return 'gd '

    def synopsis(self) -> str:
        return 'query'

    def handleQuery(self, query: Query) -> None:
        query_str = query.string.strip()
        if not query_str:
            return

        query.add(
            Item(
                id=md_name,
                text=md_name,
                subtext=f'Look up {query_str} using <i>GoldenDict</i>',
                icon=[ICON_PATH],
                actions=[Action(md_name, md_name, lambda: runDetachedProcess(['goldendict', query_str]))],
            )
        )
