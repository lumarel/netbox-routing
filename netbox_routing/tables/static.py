import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable, columns
from netbox_routing.models import StaticRoute


class StaticRouteTable(NetBoxTable):
    devices = tables.ManyToManyColumn(
        verbose_name=_('Devices'),
        linkify_item=True,
    )
    vrf = tables.Column(
        verbose_name=_('VRF'),
        linkify=True,
    )
    tags = columns.TagColumn(
        url_name='plugins:netbox_routing:staticroute_list'
    )

    class Meta(NetBoxTable.Meta):
        model = StaticRoute
        fields = (
            'pk',
            'id',
            'devices',
            'vrf',
            'prefix',
            'next_hop',
            'name',
            'metric',
            'permanent',
            'tag',
            'description',
            'comments',
            'tags',
        )
        default_columns = ('pk', 'id', 'devices', 'vrf', 'prefix', 'next_hop', 'name')
