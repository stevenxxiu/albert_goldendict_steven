from albert import (  # pylint: disable=import-error
    Action,
    PluginInstance,
    StandardItem,
    TriggerQueryHandler,
    runDetachedProcess,
)


md_iid = '2.3'
md_version = '1.3'
md_name = 'GoldenDict Steven'
md_description = 'Searches in GoldenDict'
md_url = 'https://github.com/stevenxxiu/albert_goldendict_steven'
md_maintainers = '@stevenxxiu'
md_bin_dependencies = ['goldendict']

ICON_URL = 'xdg:goldendict'


class Plugin(PluginInstance, TriggerQueryHandler):
    def __init__(self):
        TriggerQueryHandler.__init__(
            self, id=__name__, name=md_name, description=md_description, synopsis='query', defaultTrigger='gd '
        )
        PluginInstance.__init__(self)

    def handleTriggerQuery(self, query) -> None:
        query_str = query.string.strip()
        if not query_str:
            return

        query.add(
            StandardItem(
                id=md_name,
                text=md_name,
                subtext=f'Look up {query_str} using <i>GoldenDict</i>',
                iconUrls=[ICON_URL],
                actions=[Action(md_name, md_name, lambda: runDetachedProcess(['goldendict', query_str]))],
            )
        )
