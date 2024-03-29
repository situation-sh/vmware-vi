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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import StrictBool, StrictInt, StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.distributed_virtual_switch_keyed_opaque_blob import DistributedVirtualSwitchKeyedOpaqueBlob
from vmware_vi.models.dv_port_setting import DVPortSetting
from vmware_vi.models.dv_portgroup_policy import DVPortgroupPolicy
from vmware_vi.models.dynamic_property import DynamicProperty
from vmware_vi.models.managed_object_reference import ManagedObjectReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DVPortgroupConfigSpec(DataObject):
    """
    The *DVPortgroupConfigSpec* data object contains configuration data for a *DistributedVirtualPortgroup*.  Use the *DistributedVirtualPortgroup.ReconfigureDVPortgroup_Task* method to apply the configuration to the portgroup.  ***Since:*** vSphere API 4.0 
    """ # noqa: E501
    dynamic_property: Optional[List[DynamicProperty]] = Field(default=None, description="Set of dynamic properties.  This property is optional because only the properties of an object that are unknown to a client will be part of this set. This property is not readonly just in case we want to send such properties from a client in the future. ", alias="dynamicProperty")
    config_version: Optional[StrictStr] = Field(default=None, description="Version string of the configuration that this spec is trying to change.  This property is required in reconfiguring a portgroup and should be set to the same value as the *DVPortgroupConfigInfo.configVersion*. This property is ignored in creating a portgroup if set.  ***Since:*** vSphere API 4.0 ", alias="configVersion")
    name: Optional[StrictStr] = Field(default=None, description="Name of the portgroup.  ***Since:*** vSphere API 4.0 ")
    num_ports: Optional[StrictInt] = Field(default=None, description="Number of ports in the portgroup.  Setting this number larger than the number of existing ports in the portgroup causes new ports to be added to the portgroup to meet the number. Setting this property smaller than the number of existing ports deletes the free ports from the portgroup. If the number cannot be met by deleting free ports, a fault is raised. If new ports are added to the portgroup, they are also added to the switch. For portgroups of type ephemeral this property is ignored.  ***Since:*** vSphere API 4.0 ", alias="numPorts")
    port_name_format: Optional[StrictStr] = Field(default=None, description="Format of the name of the ports when ports are created in the portgroup.  For details see *DVPortgroupConfigInfo.portNameFormat*.  ***Since:*** vSphere API 4.0 ", alias="portNameFormat")
    default_port_config: Optional[DVPortSetting] = Field(default=None, alias="defaultPortConfig")
    description: Optional[StrictStr] = Field(default=None, description="Description of the portgroup.  ***Since:*** vSphere API 4.0 ")
    type: Optional[StrictStr] = Field(default=None, description="Type of portgroup.  See *DistributedVirtualPortgroup*.*DistributedVirtualPortgroupPortgroupType_enum* for possible values.  ***Since:*** vSphere API 4.0 ")
    backing_type: Optional[StrictStr] = Field(default=None, description="Backing type of portgroup.  See *DistributedVirtualPortgroup*.*DistributedVirtualPortgroupBackingType_enum* for possible values. The default value is \"standard\"  ***Since:*** vSphere API 7.0 ", alias="backingType")
    scope: Optional[List[ManagedObjectReference]] = Field(default=None, description="Deprecated as of vSphere API 5.5.  Eligible entities that can connect to the port.  See *DVPortgroupConfigInfo*.*DVPortgroupConfigInfo.scope*.  ***Since:*** vSphere API 4.0  Refers instances of *ManagedEntity*. ")
    policy: Optional[DVPortgroupPolicy] = None
    vendor_specific_config: Optional[List[DistributedVirtualSwitchKeyedOpaqueBlob]] = Field(default=None, description="Opaque binary blob that stores vendor specific configuration.  ***Since:*** vSphere API 4.0 ", alias="vendorSpecificConfig")
    auto_expand: Optional[StrictBool] = Field(default=None, description="If set to true, this property ignores the limit on the number of ports in the portgroup.  When a Virtual Machine/Host tries to connect to the portgroup and there are no free ports available in the portgroup, new ports will be automatically added to the portgroup. The flag is currently supported only for static portgroups.  Setting this property to true makes the portgroup a potential candidate for auto-shrink. Once the portgroup has auto-expanded then its disconnected ports are likely to be deleted automatically, as a part of auto-shrink step, if there are more than certain number of free ports. If the portgroup never auto-expanded, then it will never lose any free ports.  ***Since:*** vSphere API 5.0 ", alias="autoExpand")
    vm_vnic_network_resource_pool_key: Optional[StrictStr] = Field(default=None, description="The key of virtual NIC network resource pool to be associated with a portgroup.  Setting this property to \"-1\", would mean that this portgroup is not associated with any virtual NIC network resource pool.  ***Since:*** vSphere API 6.0 ", alias="vmVnicNetworkResourcePoolKey")
    transport_zone_uuid: Optional[StrictStr] = Field(default=None, description="The UUID of transport zone to be associated with a NSX portgroup.  ***Since:*** vSphere API 7.0 ", alias="transportZoneUuid")
    transport_zone_name: Optional[StrictStr] = Field(default=None, description="The name of transport zone to be associated with a NSX portgroup.  ***Since:*** vSphere API 7.0 ", alias="transportZoneName")
    logical_switch_uuid: Optional[StrictStr] = Field(default=None, description="The logical switch UUID, which is used by NSX portgroup  ***Since:*** vSphere API 7.0 ", alias="logicalSwitchUuid")
    segment_id: Optional[StrictStr] = Field(default=None, description="The segment ID of logical switch  ***Since:*** vSphere API 7.0 ", alias="segmentId")
    __properties: ClassVar[List[str]] = ["_typeName"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DVPortgroupConfigSpec from a JSON string"""
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
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of DVPortgroupConfigSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


