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
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import StrictBool, StrictInt, StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.distributed_virtual_switch_port_connectee import DistributedVirtualSwitchPortConnectee
from vmware_vi.models.dv_port_config_info import DVPortConfigInfo
from vmware_vi.models.dv_port_state import DVPortState
from vmware_vi.models.managed_object_reference import ManagedObjectReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DistributedVirtualPort(DataObject):
    """
    The *DistributedVirtualPort* data object represents a port in a *DistributedVirtualSwitch*.  Virtual ports are part of a distributed virtual portgroup. Servers create virtual ports according to the portgroup type (*DistributedVirtualPortgroup*.*DistributedVirtualPortgroup.config*.*DVPortgroupConfigInfo.type*). See *DistributedVirtualPortgroupPortgroupType_enum*. - To configure host network access by port, set the distributed virtual port   in the host virtual NIC specification   (*HostVirtualNicSpec*.*HostVirtualNicSpec.distributedVirtualPort*.*DistributedVirtualSwitchPortConnection.portKey*). - To configure virtual machine network access by port, set the port   in the virtual Ethernet card backing   (*VirtualEthernetCard*.*VirtualDevice.backing*.*VirtualEthernetCardDistributedVirtualPortBackingInfo.port*.*DistributedVirtualSwitchPortConnection.portKey*).    ***Since:*** vSphere API 4.0 
    """ # noqa: E501
    key: StrictStr = Field(description="Port key.  ***Since:*** vSphere API 4.0 ")
    config: DVPortConfigInfo
    dvs_uuid: StrictStr = Field(description="UUID of the *DistributedVirtualSwitch* to which the port belongs.  ***Since:*** vSphere API 4.0 ", alias="dvsUuid")
    portgroup_key: Optional[StrictStr] = Field(default=None, description="Key of the portgroup *DistributedVirtualPortgroup* to which the port belongs, if any.  ***Since:*** vSphere API 4.0 ", alias="portgroupKey")
    proxy_host: Optional[ManagedObjectReference] = Field(default=None, alias="proxyHost")
    connectee: Optional[DistributedVirtualSwitchPortConnectee] = None
    conflict: StrictBool = Field(description="Specifies whether the port is a conflict port.  A port could be marked as conflict if an entity is discovered connecting to a port that is already occupied, or if the host creates a port without conferring with vCenter Server.  The distributed virtual switch does not persist the runtime state of a conflict port. Also, the port cannot move away from the host. vCenter Server will not move a virtual machine (VMotion) that is using a conflict port.  ***Since:*** vSphere API 4.0 ")
    conflict_port_key: Optional[StrictStr] = Field(default=None, description="If the port is marked conflict in the case of two entities connecting to the same port (see *DistributedVirtualPort.conflict*), this is the key of the port which the connected entity is contending for.  ***Since:*** vSphere API 4.0 ", alias="conflictPortKey")
    state: Optional[DVPortState] = None
    connection_cookie: Optional[StrictInt] = Field(default=None, description="Cookie representing the current instance of association between a port and a virtual or physical NIC.  See *DistributedVirtualSwitchPortConnection*. The same cookie is present in the physical or virtual NIC configuration (*DistributedVirtualSwitchPortConnection*.*DistributedVirtualSwitchPortConnection.connectionCookie*) so that the Server can verify that the entity is the rightful connectee of the port.  ***Since:*** vSphere API 4.0 ", alias="connectionCookie")
    last_status_change: datetime = Field(description="The last time the *DistributedVirtualPort.state*.*DVPortState.runtimeInfo* value was changed.  ***Since:*** vSphere API 4.0 ", alias="lastStatusChange")
    host_local_port: Optional[StrictBool] = Field(default=None, description="Specifies whether the port is a host local port.  A host local port is created to resurrect the management network connection on a VMkernel virtual NIC. You cannot use vCenter Server to reconfigure this port and you cannot reassign the port.  ***Since:*** vSphere API 5.1 ", alias="hostLocalPort")
    external_id: Optional[StrictStr] = Field(default=None, description="Populate the Id assigned to vmknic or vnic by external management plane to port, if the port is connected to the nics.  ***Since:*** vSphere API 7.0 ", alias="externalId")
    segment_port_id: Optional[StrictStr] = Field(default=None, description="Populate the segmentPortId assigned to LSP.  ***Since:*** vSphere API 7.0 ", alias="segmentPortId")
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
        """Create an instance of DistributedVirtualPort from a JSON string"""
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
        """Create an instance of DistributedVirtualPort from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


