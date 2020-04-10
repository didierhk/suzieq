import typing

from suzieq.sqobjects import basicobj


class AddrObj(basicobj.SqObject):

    def __init__(self, engine: str = '', hostname: typing.List[str] = [],
                 start_time: str = '', end_time: str = '',
                 view: str = 'latest', namespace: typing.List[str] = [],
                 columns: typing.List[str] = ['default'],
                 context=None) -> None:
        super().__init__(engine, hostname, start_time, end_time, view,
                         namespace, columns, context=context, table='addr')
        self._sort_fields = ['namespace', 'hostname', 'ifname']
        self._cat_fields = []
        self._allcols = ["namespace", "hostname", "ifname", "state",
                         'ipAddressList', 'ip6AddressList', 'macaddr',
                         "timestamp"]
        self._basiccols = ["namespace", "hostname", "ifname", "state",
                           "timestamp"]
