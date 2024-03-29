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
from vmware_vi.models.managed_object_reference import ManagedObjectReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VAppEntityConfigInfo(DataObject):
    """
    This object type describes the behavior of an entity (virtual machine or sub-vApp container) in a vApp container.  The auto-start/auto-stop configurations control the behavior of the start/stop vApp operations.  An virtual machine entity can be configured to wait for a period of time before starting or to wait to receive a successful heartbeat from a virtual machine before starting the next virtual machine in the sequence. - For a power-on operation, if waitForHeartbeat is true, then the power-on   sequence continues after the the first heartbeat has been received. If   waitingForGuest is false, the system waits for the specified delay and   then continues the power-on sequence. - For a power-off operation, if delay is non-zero, the requested power-off   action is invoked (powerOff, suspend, guestShutdown) on the virtual   machine and the system waits until the number of seconds specified in the   delay have passed.    If startAction and stopAction for an entity are both set to none, that entity does not participate in the sequence.  The start/stop delay and waitingForGuest is not used if the entity is a vApp container. For a vApp the only value values for startAction is none or powerOn, and the valid values for stopAction is none or powerOff.  ***Since:*** vSphere API 4.0 
    """ # noqa: E501
    key: Optional[ManagedObjectReference] = None
    tag: Optional[StrictStr] = Field(default=None, description="Tag for entity.  Reconfigure privilege: VApp.ApplicationConfig  ***Since:*** vSphere API 4.0 ")
    start_order: Optional[StrictInt] = Field(default=None, description="Specifies the start order for this entity.  Entities are started from lower numbers to higher-numbers and reverse on shutdown. Multiple entities with the same start-order can be started in parallel and the order is unspecified. This value must be 0 or higher.  Reconfigure privilege: VApp.ApplicationConfig  ***Since:*** vSphere API 4.0 ", alias="startOrder")
    start_delay: Optional[StrictInt] = Field(default=None, description="Delay in seconds before continuing with the next entity in the order of entities to be started.  Reconfigure privilege: VApp.ApplicationConfig  ***Since:*** vSphere API 4.0 ", alias="startDelay")
    waiting_for_guest: Optional[StrictBool] = Field(default=None, description="Determines if the virtual machine should start after receiving a heartbeat, from the guest.  When a virtual machine is next in the start order, the system either waits a specified period of time for a virtual machine to power on or it waits until it receives a successful heartbeat from a powered on virtual machine. By default, this is set to false.  This property has no effect for vApps.  Reconfigure privilege: VApp.ApplicationConfig  ***Since:*** vSphere API 4.0 ", alias="waitingForGuest")
    start_action: Optional[StrictStr] = Field(default=None, description="How to start the entity.  Valid settings are none or powerOn. If set to none, then the entity does not participate in auto-start.  Reconfigure privilege: VApp.ApplicationConfig  ***Since:*** vSphere API 4.0 ", alias="startAction")
    stop_delay: Optional[StrictInt] = Field(default=None, description="Delay in seconds before continuing with the next entity in the order sequence.  This is only used if the stopAction is guestShutdown.  Reconfigure privilege: VApp.ApplicationConfig  ***Since:*** vSphere API 4.0 ", alias="stopDelay")
    stop_action: Optional[StrictStr] = Field(default=None, description="Defines the stop action for the entity.  Can be set to none, powerOff, guestShutdown, or suspend. If set to none, then the entity does not participate in auto-stop.  Reconfigure privilege: VApp.ApplicationConfig  ***Since:*** vSphere API 4.0 ", alias="stopAction")
    destroy_with_parent: Optional[StrictBool] = Field(default=None, description="Deprecated as of vSphere API 5.1.  Whether the entity should be removed, when this vApp is removed.  This is only set for linked children.  Reconfigure privilege: VApp.ApplicationConfig  ***Since:*** vSphere API 4.1 ", alias="destroyWithParent")
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
        """Create an instance of VAppEntityConfigInfo from a JSON string"""
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
        """Create an instance of VAppEntityConfigInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


