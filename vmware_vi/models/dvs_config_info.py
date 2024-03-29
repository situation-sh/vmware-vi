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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import StrictBool, StrictInt, StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.distributed_virtual_switch_host_member import DistributedVirtualSwitchHostMember
from vmware_vi.models.distributed_virtual_switch_keyed_opaque_blob import DistributedVirtualSwitchKeyedOpaqueBlob
from vmware_vi.models.distributed_virtual_switch_product_spec import DistributedVirtualSwitchProductSpec
from vmware_vi.models.dv_port_setting import DVPortSetting
from vmware_vi.models.dvs_contact_info import DVSContactInfo
from vmware_vi.models.dvs_health_check_config import DVSHealthCheckConfig
from vmware_vi.models.dvs_host_infrastructure_traffic_resource import DvsHostInfrastructureTrafficResource
from vmware_vi.models.dvs_policy import DVSPolicy
from vmware_vi.models.dvs_uplink_port_policy import DVSUplinkPortPolicy
from vmware_vi.models.dvsvm_vnic_network_resource_pool import DVSVmVnicNetworkResourcePool
from vmware_vi.models.managed_object_reference import ManagedObjectReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DVSConfigInfo(DataObject):
    """
    Configuration of a *DistributedVirtualSwitch*.  ***Since:*** vSphere API 4.0 
    """ # noqa: E501
    uuid: StrictStr = Field(description="Generated UUID of the switch.  Unique across vCenter Server inventory and instances.  ***Since:*** vSphere API 4.0 ")
    name: StrictStr = Field(description="Name of the switch.  ***Since:*** vSphere API 4.0 ")
    num_standalone_ports: StrictInt = Field(description="Number of standalone ports in the switch.  Standalone ports are ports that do not belong to any portgroup.  ***Since:*** vSphere API 4.0 ", alias="numStandalonePorts")
    num_ports: StrictInt = Field(description="Current number of ports, not including conflict ports.  ***Since:*** vSphere API 4.0 ", alias="numPorts")
    max_ports: StrictInt = Field(description="Maximum number of ports allowed in the switch, not including conflict ports.  ***Since:*** vSphere API 4.0 ", alias="maxPorts")
    uplink_port_policy: DVSUplinkPortPolicy = Field(alias="uplinkPortPolicy")
    uplink_portgroup: Optional[List[ManagedObjectReference]] = Field(default=None, description="List of uplink portgroups.  When adding host members, the server uses the *DVSConfigInfo.uplinkPortPolicy* to create a number of uplink ports for the host. If portgroups are shown here, those uplink ports will be added to the portgroups, with uplink ports evenly spread among the portgroups.  ***Since:*** vSphere API 4.0  Refers instances of *DistributedVirtualPortgroup*. ", alias="uplinkPortgroup")
    default_port_config: DVPortSetting = Field(alias="defaultPortConfig")
    host: Optional[List[DistributedVirtualSwitchHostMember]] = Field(default=None, description="Hosts that join the switch.  ***Since:*** vSphere API 4.0 ")
    product_info: DistributedVirtualSwitchProductSpec = Field(alias="productInfo")
    target_info: Optional[DistributedVirtualSwitchProductSpec] = Field(default=None, alias="targetInfo")
    extension_key: Optional[StrictStr] = Field(default=None, description="Key of the extension registered by the remote server that controls the switch.  ***Since:*** vSphere API 4.0 ", alias="extensionKey")
    vendor_specific_config: Optional[List[DistributedVirtualSwitchKeyedOpaqueBlob]] = Field(default=None, description="Opaque binary blob that stores vendor specific configuration.  ***Since:*** vSphere API 4.0 ", alias="vendorSpecificConfig")
    policy: Optional[DVSPolicy] = None
    description: Optional[StrictStr] = Field(default=None, description="Description string for the switch.  ***Since:*** vSphere API 4.0 ")
    config_version: StrictStr = Field(description="Version string of the configuration.  ***Since:*** vSphere API 4.0 ", alias="configVersion")
    contact: DVSContactInfo
    switch_ip_address: Optional[StrictStr] = Field(default=None, description="IP address for the switch, specified using IPv4 dot notation.  The utility of this address is defined by other switch features.  ***Since:*** vSphere API 5.0 ", alias="switchIpAddress")
    create_time: datetime = Field(description="Create time of the switch.  ***Since:*** vSphere API 4.0 ", alias="createTime")
    network_resource_management_enabled: StrictBool = Field(description="Boolean to indicate if network I/O control is enabled on the switch.  ***Since:*** vSphere API 4.1 ", alias="networkResourceManagementEnabled")
    default_proxy_switch_max_num_ports: Optional[StrictInt] = Field(default=None, description="Default host proxy switch maximum port number  ***Since:*** vSphere API 5.1 ", alias="defaultProxySwitchMaxNumPorts")
    health_check_config: Optional[List[DVSHealthCheckConfig]] = Field(default=None, description="VDS health check configuration.  ***Since:*** vSphere API 5.1 ", alias="healthCheckConfig")
    infrastructure_traffic_resource_config: Optional[List[DvsHostInfrastructureTrafficResource]] = Field(default=None, description="Host infrastructure traffic class resource configuration.  ***Since:*** vSphere API 6.0 ", alias="infrastructureTrafficResourceConfig")
    net_resource_pool_traffic_resource_config: Optional[List[DvsHostInfrastructureTrafficResource]] = Field(default=None, description="Dynamic Host infrastructure traffic class resource configuration.  ***Since:*** vSphere API 6.7 ", alias="netResourcePoolTrafficResourceConfig")
    network_resource_control_version: Optional[StrictStr] = Field(default=None, description="Network resource control version of the switch.  Possible value can be of *DistributedVirtualSwitchNetworkResourceControlVersion_enum*.  ***Since:*** vSphere API 6.0 ", alias="networkResourceControlVersion")
    vm_vnic_network_resource_pool: Optional[List[DVSVmVnicNetworkResourcePool]] = Field(default=None, description="The Virtual NIC network resource pool information for the switch.  ***Since:*** vSphere API 6.0 ", alias="vmVnicNetworkResourcePool")
    pnic_capacity_ratio_for_reservation: Optional[StrictInt] = Field(default=None, description="The percentage of physical nic link speed *PhysicalNicLinkInfo.speedMb* available for infrastructure traffic reservation.  If this value is 75, then for a 1Gbps physical nic, only 750Mbps is allowed for all infrastructure traffic reservations.  ***Since:*** vSphere API 6.0 ", alias="pnicCapacityRatioForReservation")
    __properties: ClassVar[List[str]] = ["_typeName"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[List[str]] = '_typeName'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'ArrayOfAnyURI': 'ArrayOfURI','ArrayOfBase64Binary': 'ArrayOfBinary','ArrayOfPropertyPath': 'ArrayOfPropPath','MethodName': 'PrimitiveMethodName','PropertyPath': 'PrimitivePropPath','TypeName': 'PrimitiveTypeName','anyURI': 'PrimitiveURI','base64Binary': 'PrimitiveBinary','boolean': 'PrimitiveBoolean','byte': 'PrimitiveByte','dateTime': 'PrimitiveDateTime','double': 'PrimitiveDouble','float': 'PrimitiveFloat','int': 'PrimitiveInt','long': 'PrimitiveLong','short': 'PrimitiveShort','string': 'PrimitiveString','VMwareDVSConfigInfo': 'VMwareDVSConfigInfo'
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
        """Create an instance of DVSConfigInfo from a JSON string"""
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
        """Create an instance of DVSConfigInfo from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = globals()[object_type]
            return klass.from_dict(obj)
        else:
            raise ValueError("DVSConfigInfo failed to lookup discriminator value from " +
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
from vmware_vi.models.v_mware_dvs_config_info import VMwareDVSConfigInfo
# TODO: Rewrite to not use raise_errors
DVSConfigInfo.model_rebuild(raise_errors=False)

