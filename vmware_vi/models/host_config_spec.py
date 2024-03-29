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
from pydantic import StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.host_account_spec import HostAccountSpec
from vmware_vi.models.host_active_directory import HostActiveDirectory
from vmware_vi.models.host_assignable_hardware_config import HostAssignableHardwareConfig
from vmware_vi.models.host_date_time_config import HostDateTimeConfig
from vmware_vi.models.host_firewall_config import HostFirewallConfig
from vmware_vi.models.host_graphics_config import HostGraphicsConfig
from vmware_vi.models.host_license_spec import HostLicenseSpec
from vmware_vi.models.host_memory_spec import HostMemorySpec
from vmware_vi.models.host_nas_volume_config import HostNasVolumeConfig
from vmware_vi.models.host_network_config import HostNetworkConfig
from vmware_vi.models.host_security_spec import HostSecuritySpec
from vmware_vi.models.host_service_config import HostServiceConfig
from vmware_vi.models.host_storage_device_info import HostStorageDeviceInfo
from vmware_vi.models.host_virtual_nic_manager_nic_type_selection import HostVirtualNicManagerNicTypeSelection
from vmware_vi.models.key_any_value import KeyAnyValue
from vmware_vi.models.option_value import OptionValue
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HostConfigSpec(DataObject):
    """
    The *HostConfigSpec* data object provides access to data objects that specify configuration changes to be applied to an ESX host.  ***Since:*** vSphere API 4.0 
    """ # noqa: E501
    nas_datastore: Optional[List[HostNasVolumeConfig]] = Field(default=None, description="Configurations to create NAS datastores.  ***Since:*** vSphere API 4.0 ", alias="nasDatastore")
    network: Optional[HostNetworkConfig] = None
    nic_type_selection: Optional[List[HostVirtualNicManagerNicTypeSelection]] = Field(default=None, description="Type selection for different VirtualNics.  ***Since:*** vSphere API 4.0 ", alias="nicTypeSelection")
    service: Optional[List[HostServiceConfig]] = Field(default=None, description="Host service configuration.  ***Since:*** vSphere API 4.0 ")
    firewall: Optional[HostFirewallConfig] = None
    option: Optional[List[OptionValue]] = Field(default=None, description="Host configuration options as defined by the *OptionValue* data object type.  ***Since:*** vSphere API 4.0 ")
    datastore_principal: Optional[StrictStr] = Field(default=None, description="Datastore principal user.  ***Since:*** vSphere API 4.0 ", alias="datastorePrincipal")
    datastore_principal_passwd: Optional[StrictStr] = Field(default=None, description="Password for the datastore principal.  ***Since:*** vSphere API 4.0 ", alias="datastorePrincipalPasswd")
    datetime: Optional[HostDateTimeConfig] = None
    storage_device: Optional[HostStorageDeviceInfo] = Field(default=None, alias="storageDevice")
    license: Optional[HostLicenseSpec] = None
    security: Optional[HostSecuritySpec] = None
    user_account: Optional[List[HostAccountSpec]] = Field(default=None, description="List of users to create/update with new password.  ***Since:*** vSphere API 4.0 ", alias="userAccount")
    usergroup_account: Optional[List[HostAccountSpec]] = Field(default=None, description="List of users to create/update with new password.  ***Since:*** vSphere API 4.0 ", alias="usergroupAccount")
    memory: Optional[HostMemorySpec] = None
    active_directory: Optional[List[HostActiveDirectory]] = Field(default=None, description="Active Directory configuration change.  ***Since:*** vSphere API 4.1 ", alias="activeDirectory")
    generic_config: Optional[List[KeyAnyValue]] = Field(default=None, description="Advanced configuration.  ***Since:*** vSphere API 5.0 ", alias="genericConfig")
    graphics_config: Optional[HostGraphicsConfig] = Field(default=None, alias="graphicsConfig")
    assignable_hardware_config: Optional[HostAssignableHardwareConfig] = Field(default=None, alias="assignableHardwareConfig")
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
        """Create an instance of HostConfigSpec from a JSON string"""
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
        """Create an instance of HostConfigSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


