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
from pydantic import StrictBool, StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.host_capability import HostCapability
from vmware_vi.models.host_connect_info_network_info import HostConnectInfoNetworkInfo
from vmware_vi.models.host_datastore_connect_info import HostDatastoreConnectInfo
from vmware_vi.models.host_license_connect_info import HostLicenseConnectInfo
from vmware_vi.models.host_list_summary import HostListSummary
from vmware_vi.models.virtual_machine_summary import VirtualMachineSummary
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HostConnectInfo(DataObject):
    """
    This data object type contains information about a single host that can be used by the connection wizard.  This can be returned without adding the host to VirtualCenter. 
    """ # noqa: E501
    server_ip: Optional[StrictStr] = Field(default=None, description="The IP address of the VirtualCenter already managing this host, if any. ", alias="serverIp")
    in_das_cluster: Optional[StrictBool] = Field(default=None, description="If the host is already being managed by a vCenter Server, this property reports true if the host is also part of a vSphere HA enabled cluster.  If this is the case, remove or disconnect the host from this cluster before adding it to another vCenter Server.  ***Since:*** vSphere API 5.0 ", alias="inDasCluster")
    host: HostListSummary
    vm: Optional[List[VirtualMachineSummary]] = Field(default=None, description="The list of virtual machines on the host. ")
    vim_account_name_required: Optional[StrictBool] = Field(default=None, description="Whether or not the host requires a vimAccountName and password to be set in the ConnectSpec.  This is normally only required for VMware Server hosts. ", alias="vimAccountNameRequired")
    cluster_supported: Optional[StrictBool] = Field(default=None, description="Whether or not the host supports clustering capabilities such as HA or DRS and therefore can be added to a cluster.  If false, the host must be added as a standalone host. ", alias="clusterSupported")
    network: Optional[List[HostConnectInfoNetworkInfo]] = Field(default=None, description="The list of network information for networks configured on this host. ")
    datastore: Optional[List[HostDatastoreConnectInfo]] = Field(default=None, description="The list of datastores on the host. ")
    license: Optional[HostLicenseConnectInfo] = None
    capability: Optional[HostCapability] = None
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
        """Create an instance of HostConnectInfo from a JSON string"""
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
        """Create an instance of HostConnectInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


