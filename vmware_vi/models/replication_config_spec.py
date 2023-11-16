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
from vmware_vi.models.replication_info_disk_settings import ReplicationInfoDiskSettings
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ReplicationConfigSpec(DataObject):
    """
    The ReplicationConfigSpec object type encapsulates the replication configuration parameters for a virtual machine.  It consists of two parts: 1) a set of virtual machine-wide replication properties; 2) a set of properties per replicated virtual disk. ReplicationSetting is passed as an argument for initial replication configuration (@see vim.HbrManager#enableReplication) as well as for re-configuration of a replicated VM's properties (@see vim.HbrManager#reconfigureReplication).  ***Since:*** vSphere API 5.0 
    """ # noqa: E501
    generation: StrictInt = Field(description="A generation number (&gt;=0) that reflects the \"freshness\" of the ReplicationConfigSpec on which a re-configuration is based.  The generation number is used to detect and disallow concurrent updates to a VM's replication settings. For initial replication enablement, generation = 0. The replication settings of every replication re-configuration operation must reflect the latest generation number known to the caller. It takes an explicit call to get the latest replication settings to find out what the latest generation number is. The update algorithm of the generation number is opaque to the caller; e.g., the caller cannot assume that the generation numbers are incremented by one every time replication is (re)configured, not even that they are changing monotonically.  ***Since:*** vSphere API 5.0 ")
    vm_replication_id: StrictStr = Field(description="An opaque identifier that uniquely identifies a replicated VM between primary and secondary sites.  ***Since:*** vSphere API 5.0 ", alias="vmReplicationId")
    destination: StrictStr = Field(description="The IP address of the HBR Server in the secondary site where this VM is replicated to.  Note: If net encryption is enabled, this is the address of the encryption tunnelling agent.  ***Since:*** vSphere API 5.0 ")
    port: StrictInt = Field(description="The port on the HBR Server in the secondary site where this VM is replicated to.  Note: If net encryption is enabled, this is the port of the encryption tunneling agent.  ***Since:*** vSphere API 5.0 ")
    rpo: StrictInt = Field(description="The Recovery Point Objective specified for this VM, in minutes.  Currently, valid values are in the range of 1 minute to 1440 minutes (24 hours).  ***Since:*** vSphere API 5.0 ")
    quiesce_guest_enabled: StrictBool = Field(description="Flag that indicates whether or not to quiesce the file system or applications in the guest OS before a consistent replica is created.  ***Since:*** vSphere API 5.0 ", alias="quiesceGuestEnabled")
    paused: StrictBool = Field(description="Flag that indicates whether or not the vm or group has been paused for replication.  ***Since:*** vSphere API 5.0 ")
    opp_updates_enabled: StrictBool = Field(description="Flag that indicates whether or not to perform opportunistic updates in-between consistent replicas.  ***Since:*** vSphere API 5.0 ", alias="oppUpdatesEnabled")
    net_compression_enabled: Optional[StrictBool] = Field(default=None, description="Flag that indicates whether or not compression should be used when sending traffic over the network.  The primary will negotiate the best compression with the server on the secondary if this is enabled.  ***Since:*** vSphere API 6.0 ", alias="netCompressionEnabled")
    net_encryption_enabled: Optional[StrictBool] = Field(default=None, description="Flag that indicates whether or not encription should be used when sending traffic over the network.  The primary will use the remoteCertificateThumbprint to verify the identity of the remote server.  ***Since:*** vSphere API 6.7 ", alias="netEncryptionEnabled")
    encryption_destination: Optional[StrictStr] = Field(default=None, description="The IP address of the remote HBR server, target for encrypted LWD.  This field is required when net encryption is enabled, ignored otherwise.  ***Since:*** vSphere API 6.7 ", alias="encryptionDestination")
    encryption_port: Optional[StrictInt] = Field(default=None, description="The port on the remote HBR server, target for encrypted LWD.  This field is only relevant when net encryption is enabled.  ***Since:*** vSphere API 6.7 ", alias="encryptionPort")
    remote_certificate_thumbprint: Optional[StrictStr] = Field(default=None, description="The SHA256 thumbprint of the remote server certificate.  This field is only relevant when net encription is enabled.  ***Since:*** vSphere API 6.7 ", alias="remoteCertificateThumbprint")
    data_sets_replication_enabled: Optional[StrictBool] = Field(default=None, description="Flag that indicates whether DataSets files are replicated or not. ", alias="dataSetsReplicationEnabled")
    disk: Optional[List[ReplicationInfoDiskSettings]] = Field(default=None, description="The set of the disks of this VM that are configured for replication.  ***Since:*** vSphere API 5.0 ")
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
        """Create an instance of ReplicationConfigSpec from a JSON string"""
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
        """Create an instance of ReplicationConfigSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

