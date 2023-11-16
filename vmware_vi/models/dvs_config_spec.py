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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import StrictInt, StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.distributed_virtual_switch_host_member_config_spec import DistributedVirtualSwitchHostMemberConfigSpec
from vmware_vi.models.distributed_virtual_switch_keyed_opaque_blob import DistributedVirtualSwitchKeyedOpaqueBlob
from vmware_vi.models.dv_port_setting import DVPortSetting
from vmware_vi.models.dvs_contact_info import DVSContactInfo
from vmware_vi.models.dvs_host_infrastructure_traffic_resource import DvsHostInfrastructureTrafficResource
from vmware_vi.models.dvs_policy import DVSPolicy
from vmware_vi.models.dvs_uplink_port_policy import DVSUplinkPortPolicy
from vmware_vi.models.dynamic_property import DynamicProperty
from vmware_vi.models.managed_object_reference import ManagedObjectReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DVSConfigSpec(DataObject):
    """
    The *DVSConfigSpec* data object contains configuration data for a *DistributedVirtualSwitch*.  Use the *DistributedVirtualSwitch.ReconfigureDvs_Task* method to apply the configuration to the switch.  ***Since:*** vSphere API 4.0 
    """ # noqa: E501
    dynamic_property: Optional[List[DynamicProperty]] = Field(default=None, description="Set of dynamic properties.  This property is optional because only the properties of an object that are unknown to a client will be part of this set. This property is not readonly just in case we want to send such properties from a client in the future. ", alias="dynamicProperty")
    config_version: Optional[StrictStr] = Field(default=None, description="The version string of the configuration that this spec is trying to change.  This property is required in reconfiguring a switch and should be set to the same value as *DVSConfigInfo.configVersion*. This property is ignored during switch creation.  ***Since:*** vSphere API 4.0 ", alias="configVersion")
    name: Optional[StrictStr] = Field(default=None, description="The name of the switch.  Must be unique in the parent folder.  ***Since:*** vSphere API 4.0 ")
    num_standalone_ports: Optional[StrictInt] = Field(default=None, description="The number of standalone ports in the switch.  Standalone ports are ports that do not belong to any portgroup. If set to a number larger than number of existing standalone ports in the switch, new ports get created to meet the number. If set to a number smaller than the number of existing standalone ports, free ports (uplink ports excluded) are deleted to meet the number. If the set number cannot be met by deleting free standalone ports, a fault is raised.  ***Since:*** vSphere API 4.0 ", alias="numStandalonePorts")
    max_ports: Optional[StrictInt] = Field(default=None, description="Deprecated as of vSphere API 5.0 The default value of this propoerty is maxint and there is no reason for users to change it to a lower value.  The maximum number of DistributedVirtualPorts allowed in the switch.  If specified in a reconfigure operation, this number cannot be smaller than the number of existing DistributedVirtualPorts.  ***Since:*** vSphere API 4.0 ", alias="maxPorts")
    uplink_port_policy: Optional[DVSUplinkPortPolicy] = Field(default=None, alias="uplinkPortPolicy")
    uplink_portgroup: Optional[List[ManagedObjectReference]] = Field(default=None, description="The uplink portgroups.  ***Since:*** vSphere API 4.0  Refers instances of *DistributedVirtualPortgroup*. ", alias="uplinkPortgroup")
    default_port_config: Optional[DVPortSetting] = Field(default=None, alias="defaultPortConfig")
    host: Optional[List[DistributedVirtualSwitchHostMemberConfigSpec]] = Field(default=None, description="The host member specification.  A particular host should have only one entry in this array. Duplicate entries for the same host will raise a fault. The host version should be compatible with the version of *DistributedVirtualSwitch*. Use *DistributedVirtualSwitchManager.QueryDvsCheckCompatibility* to check for compatibility.  ***Since:*** vSphere API 4.0 ")
    extension_key: Optional[StrictStr] = Field(default=None, description="The key of the extension registered by a remote server that controls the switch.  ***Since:*** vSphere API 4.0 ", alias="extensionKey")
    description: Optional[StrictStr] = Field(default=None, description="Set the description string of the switch.  ***Since:*** vSphere API 4.0 ")
    policy: Optional[DVSPolicy] = None
    vendor_specific_config: Optional[List[DistributedVirtualSwitchKeyedOpaqueBlob]] = Field(default=None, description="Set the opaque blob that stores vendor specific configuration.  ***Since:*** vSphere API 4.0 ", alias="vendorSpecificConfig")
    contact: Optional[DVSContactInfo] = None
    switch_ip_address: Optional[StrictStr] = Field(default=None, description="IP address for the switch, specified using IPv4 dot notation.  IPv6 address is not supported for this property. The utility of this address is defined by other switch features. switchIpAddress would be ignored when IPFIX collector uses IPv6.  ***Since:*** vSphere API 5.0 ", alias="switchIpAddress")
    default_proxy_switch_max_num_ports: Optional[StrictInt] = Field(default=None, description="The default host proxy switch maximum port number  ***Since:*** vSphere API 5.1 ", alias="defaultProxySwitchMaxNumPorts")
    infrastructure_traffic_resource_config: Optional[List[DvsHostInfrastructureTrafficResource]] = Field(default=None, description="The host infrastructure traffic resource allocation specification.  Only the traffic class resource allocations identified in the list will be updated. The other traffic class resource allocations that are not specified will not change.  ***Since:*** vSphere API 6.0 ", alias="infrastructureTrafficResourceConfig")
    net_resource_pool_traffic_resource_config: Optional[List[DvsHostInfrastructureTrafficResource]] = Field(default=None, description="The dynamic host infrastructure traffic resource allocation specification.  ***Since:*** vSphere API 6.7 ", alias="netResourcePoolTrafficResourceConfig")
    network_resource_control_version: Optional[StrictStr] = Field(default=None, description="Indicates the Network Resource Control APIs that are supported on the switch.  Possible value can be of *DistributedVirtualSwitchNetworkResourceControlVersion_enum*.  ***Since:*** vSphere API 6.0 ", alias="networkResourceControlVersion")
    __properties: ClassVar[List[str]] = ["_typeName"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[List[str]] = '_typeName'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'ArrayOfAnyURI': 'ArrayOfURI','ArrayOfBase64Binary': 'ArrayOfBinary','ArrayOfPropertyPath': 'ArrayOfPropPath','MethodName': 'PrimitiveMethodName','PropertyPath': 'PrimitivePropPath','TypeName': 'PrimitiveTypeName','anyURI': 'PrimitiveURI','base64Binary': 'PrimitiveBinary','boolean': 'PrimitiveBoolean','byte': 'PrimitiveByte','dateTime': 'PrimitiveDateTime','double': 'PrimitiveDouble','float': 'PrimitiveFloat','int': 'PrimitiveInt','long': 'PrimitiveLong','short': 'PrimitiveShort','string': 'PrimitiveString','VMwareDVSConfigSpec': 'VMwareDVSConfigSpec'
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
    def from_json(cls, json_str: str) -> Union[Self]:
        """Create an instance of DVSConfigSpec from a JSON string"""
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
    def from_dict(cls, obj: Dict) -> Union[Self]:
        """Create an instance of DVSConfigSpec from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = globals()[object_type]
            return klass.from_dict(obj)
        else:
            raise ValueError("DVSConfigSpec failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))

from vmware_vi.models.array_of_binary import ArrayOfBinary
from vmware_vi.models.array_of_prop_path import ArrayOfPropPath
from vmware_vi.models.array_of_uri import ArrayOfURI
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
from vmware_vi.models.v_mware_dvs_config_spec import VMwareDVSConfigSpec
# TODO: Rewrite to not use raise_errors
DVSConfigSpec.model_rebuild(raise_errors=False)
