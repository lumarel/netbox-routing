import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable, columns
from netbox_routing.models import EIGRPAddressFamily, EIGRPRouter, EIGRPNetwork, EIGRPInterface


__all__ = (
    'EIGRPAddressFamilyTable',
    'EIGRPRouterTable',
    'EIGRPNetworkTable',
    'EIGRPInterfaceTable',
)


class EIGRPRouterTable(NetBoxTable):
    tags = columns.TagColumn(
        url_name='plugins:netbox_routing:eigrprouter_list'
    )

    class Meta(NetBoxTable.Meta):
        model = EIGRPRouter
        fields = ('pk', 'id', 'name', 'mode', 'pid', 'rid', 'device', 'tags')
        default_columns = ('pk', 'id', 'name', 'device')


class EIGRPAddressFamilyTable(NetBoxTable):
    router = tables.Column(verbose_name=_('Router'), linkify=True)
    tags = columns.TagColumn(url_name='plugins:netbox_routing:eigrpaddressfamily_list')

    class Meta(NetBoxTable.Meta):
        model = EIGRPAddressFamily
        fields = ('pk', 'id', 'family', 'router', 'tags')
        default_columns = ('pk', 'id', 'family', 'router')


class EIGRPNetworkTable(NetBoxTable):
    router = tables.Column(verbose_name=_('Router'), linkify=True)
    address_family = tables.Column(verbose_name=_('Address Family'), linkify=True)
    network = tables.Column(verbose_name=_('Network'), linkify=True)
    tags = columns.TagColumn(url_name='plugins:netbox_routing:eigrpnetwork_list')

    class Meta(NetBoxTable.Meta):
        model = EIGRPNetwork
        fields = ('pk', 'id', 'router', 'address_family', 'network', 'tags')
        default_columns = ('pk', 'id', 'router', 'address_family', 'network')


class EIGRPInterfaceTable(NetBoxTable):
    router = tables.Column(verbose_name=_('Router'), linkify=True)
    address_family = tables.Column(verbose_name=_('Address Family'), linkify=True)
    interface = tables.Column(verbose_name=_('Interface'), linkify=True)
    tags = columns.TagColumn(url_name='plugins:netbox_routing:eigrpinterface_list')

    class Meta(NetBoxTable.Meta):
        model = EIGRPInterface
        fields = (
            'pk',
            'id',
            'router',
            'address_family',
            'interface',
            'passive',
            'bfd',
            'authentication',
            'passphrase',
            'tags',
        )
        default_columns = ('pk', 'id', 'router', 'address_family', 'interface')
