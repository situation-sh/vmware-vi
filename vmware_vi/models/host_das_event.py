# coding: utf-8

"""
    Virtual Infrastructure JSON API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 8.0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Union

from vmware_vi.models.host_event import HostEvent
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HostDasEvent(HostEvent):
    """
    Top-level event for host DAS events to extend.  ***Since:*** VI API 2.5 
    """ # noqa: E501
    __properties: ClassVar[List[str]] = ["_typeName"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[List[str]] = '_typeName'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'ArrayOfAnyURI': 'ArrayOfURI','ArrayOfBase64Binary': 'ArrayOfBinary','ArrayOfPropertyPath': 'ArrayOfPropPath','MethodName': 'PrimitiveMethodName','PropertyPath': 'PrimitivePropPath','TypeName': 'PrimitiveTypeName','anyURI': 'PrimitiveURI','base64Binary': 'PrimitiveBinary','boolean': 'PrimitiveBoolean','byte': 'PrimitiveByte','dateTime': 'PrimitiveDateTime','double': 'PrimitiveDouble','float': 'PrimitiveFloat','int': 'PrimitiveInt','long': 'PrimitiveLong','short': 'PrimitiveShort','string': 'PrimitiveString','HostExtraNetworksEvent': 'HostExtraNetworksEvent','HostIsolationIpPingFailedEvent': 'HostIsolationIpPingFailedEvent','HostMissingNetworksEvent': 'HostMissingNetworksEvent','HostNoAvailableNetworksEvent': 'HostNoAvailableNetworksEvent','HostNoHAEnabledPortGroupsEvent': 'HostNoHAEnabledPortGroupsEvent','HostNoRedundantManagementNetworkEvent': 'HostNoRedundantManagementNetworkEvent','HostNotInClusterEvent': 'HostNotInClusterEvent','HostPrimaryAgentNotShortNameEvent': 'HostPrimaryAgentNotShortNameEvent','HostShortNameInconsistentEvent': 'HostShortNameInconsistentEvent'
    }

    @classmethod
    def get_discriminator_value(cls, obj: Dict) -> str:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Union[Self, Self, Self, Self, Self, Self, Self, Self, Self]:
        """Create an instance of HostDasEvent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Union[Self, Self, Self, Self, Self, Self, Self, Self, Self]:
        """Create an instance of HostDasEvent from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = globals()[object_type]
            return klass.from_dict(obj)
        else:
            raise ValueError("HostDasEvent failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

from vmware_vi.models.array_of_binary import ArrayOfBinary
from vmware_vi.models.array_of_prop_path import ArrayOfPropPath
from vmware_vi.models.array_of_uri import ArrayOfURI
from vmware_vi.models.host_extra_networks_event import HostExtraNetworksEvent
from vmware_vi.models.host_isolation_ip_ping_failed_event import HostIsolationIpPingFailedEvent
from vmware_vi.models.host_missing_networks_event import HostMissingNetworksEvent
from vmware_vi.models.host_no_available_networks_event import HostNoAvailableNetworksEvent
from vmware_vi.models.host_no_ha_enabled_port_groups_event import HostNoHAEnabledPortGroupsEvent
from vmware_vi.models.host_no_redundant_management_network_event import HostNoRedundantManagementNetworkEvent
from vmware_vi.models.host_not_in_cluster_event import HostNotInClusterEvent
from vmware_vi.models.host_primary_agent_not_short_name_event import HostPrimaryAgentNotShortNameEvent
from vmware_vi.models.host_short_name_inconsistent_event import HostShortNameInconsistentEvent
from vmware_vi.models.primitive_binary import PrimitiveBinary
from vmware_vi.models.primitive_boolean import PrimitiveBoolean
from vmware_vi.models.primitive_byte import PrimitiveByte
from vmware_vi.models.primitive_date_time import PrimitiveDateTime
from vmware_vi.models.primitive_double import PrimitiveDouble
from vmware_vi.models.primitive_float import PrimitiveFloat
from vmware_vi.models.primitive_int import PrimitiveInt
from vmware_vi.models.primitive_long import PrimitiveLong
from vmware_vi.models.primitive_method_name import PrimitiveMethodName
from vmware_vi.models.primitive_prop_path import PrimitivePropPath
from vmware_vi.models.primitive_short import PrimitiveShort
from vmware_vi.models.primitive_string import PrimitiveString
from vmware_vi.models.primitive_type_name import PrimitiveTypeName
from vmware_vi.models.primitive_uri import PrimitiveURI
# TODO: Rewrite to not use raise_errors
HostDasEvent.model_rebuild(raise_errors=False)

