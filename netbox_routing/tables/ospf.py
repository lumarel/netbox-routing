import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable, columns
from netbox_routing.models import OSPFArea, OSPFInstance, OSPFInterface


__all__ = (
    'OSPFAreaTable',
    'OSPFInstanceTable',
    'OSPFInterfaceTable',
)


class OSPFInstanceTable(NetBoxTable):
    tags = columns.TagColumn(
        url_name='plugins:netbox_routing:ospfinstance_list'
    )

    class Meta(NetBoxTable.Meta):
        model = OSPFInstance
        fields = (
            'pk',
            'id',
            'name',
            'router_id',
            'process_id',
            'device',
            'vrf',
            'tags',
        )
        default_columns = (
            'pk',
            'id',
            'name',
            'router_id',
            'process_id',
            'device',
        )


class OSPFAreaTable(NetBoxTable):
    tags = columns.TagColumn(
        url_name='plugins:netbox_routing:ospfarea_list'
    )

    class Meta(NetBoxTable.Meta):
        model = OSPFArea
        fields = ('pk', 'id', 'area_id', 'area_type', 'tags')
        default_columns = ('pk', 'id', 'area_id', 'area_type')


class OSPFInterfaceTable(NetBoxTable):
    instance = tables.Column(verbose_name=_('Instance'), linkify=True)
    device = tables.Column(
        verbose_name=_('Device'),
        linkify=True,
        accessor='instance__device',
    )
    area = tables.Column(verbose_name=_('Area'), linkify=True)
    interface = tables.Column(verbose_name=_('Interface'), linkify=True)
    tags = columns.TagColumn(url_name='plugins:netbox_routing:ospfinterface_list')

    class Meta(NetBoxTable.Meta):
        model = OSPFInterface
        fields = (
            'pk',
            'id',
            'instance',
            'device',
            'area',
            'interface',
            'passive',
            'priority',
            'bfd',
            'authentication',
            'passphrase',
            'tags',
        )
        default_columns = ('pk', 'id', 'instance', 'area', 'interface', 'passive')
