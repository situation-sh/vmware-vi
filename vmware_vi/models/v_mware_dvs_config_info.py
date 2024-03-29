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
from pydantic import StrictInt, StrictStr
from pydantic import Field
from vmware_vi.models.dvs_config_info import DVSConfigInfo
from vmware_vi.models.link_discovery_protocol_config import LinkDiscoveryProtocolConfig
from vmware_vi.models.v_mware_dvs_lacp_group_config import VMwareDvsLacpGroupConfig
from vmware_vi.models.v_mware_dvs_pvlan_map_entry import VMwareDVSPvlanMapEntry
from vmware_vi.models.v_mware_ipfix_config import VMwareIpfixConfig
from vmware_vi.models.v_mware_vspan_session import VMwareVspanSession
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VMwareDVSConfigInfo(DVSConfigInfo):
    """
    This class defines the VMware specific configuration for DistributedVirtualSwitch.  ***Since:*** vSphere API 4.0 
    """ # noqa: E501
    vspan_session: Optional[List[VMwareVspanSession]] = Field(default=None, description="The Distributed Port Mirroring sessions in the switch.  ***Since:*** vSphere API 5.0 ", alias="vspanSession")
    pvlan_config: Optional[List[VMwareDVSPvlanMapEntry]] = Field(default=None, description="The PVLAN configured in the switch.  ***Since:*** vSphere API 4.0 ", alias="pvlanConfig")
    max_mtu: StrictInt = Field(description="The maximum MTU in the switch.  ***Since:*** vSphere API 4.0 ", alias="maxMtu")
    link_discovery_protocol_config: Optional[LinkDiscoveryProtocolConfig] = Field(default=None, alias="linkDiscoveryProtocolConfig")
    ipfix_config: Optional[VMwareIpfixConfig] = Field(default=None, alias="ipfixConfig")
    lacp_group_config: Optional[List[VMwareDvsLacpGroupConfig]] = Field(default=None, description="The Link Aggregation Control Protocol groups in the switch.  ***Since:*** vSphere API 5.5 ", alias="lacpGroupConfig")
    lacp_api_version: Optional[StrictStr] = Field(default=None, description="The Link Aggregation Control Protocol group version in the switch.  See *VMwareDvsLacpApiVersion_enum* for valid values.  ***Since:*** vSphere API 5.5 ", alias="lacpApiVersion")
    multicast_filtering_mode: Optional[StrictStr] = Field(default=None, description="The Multicast Filtering mode in the switch.  See *VMwareDvsMulticastFilteringMode_enum* for valid values.  ***Since:*** vSphere API 6.0 ", alias="multicastFilteringMode")
    network_offload_spec_id: Optional[StrictStr] = Field(default=None, description="Indicate the ID of NetworkOffloadSpec used in the switch.  ID \"None\" means that network offload is not allowed in the switch. ", alias="networkOffloadSpecId")
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
        """Create an instance of VMwareDVSConfigInfo from a JSON string"""
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
        """Create an instance of VMwareDVSConfigInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


