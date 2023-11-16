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


from typing import Any, ClassVar, Dict, List
from pydantic import StrictInt, StrictStr
from pydantic import Field
from vmware_vi.models.auto_start_wait_heartbeat_setting_enum import AutoStartWaitHeartbeatSettingEnum
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.managed_object_reference import ManagedObjectReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AutoStartPowerInfo(DataObject):
    """
    This object type describes the power-on / power-off behavior for a given virtual machine.  Virtual machines can be configured to wait for a period of time before starting or to wait to receive a successful heartbeat from a virtual machine before starting the next virtual machine in the sequence. - For a power-on operation, if waitForHeartbeat is true, then the power-on   sequence continues after the first heartbeat has been received. If   waitForHeartbeat is false, the system waits for the specified delay and   then continues the power-on sequence. - For a power-off operation, if delay is non-zero, the requested power-off   action is invoked (powerOff, suspend, guestShutdown) on the virtual   machine and the system waits until the number of seconds specified in the   delay have passed.    If startAction and stopAction for a virtual machine are both set to none, that virtual machine is removed from the AutoStart sequence. Virtual machines can be configured both to wait for a period of time before starting and to wait for a heartbeat. In such a case, the waiting virtual machine only waits until either of these conditions are met. In other words, a virtual machine starts in either of the following cases: - After receiving a heartbeat but before the start delay has elapsed - After the start delay has elapsed but before receiving a heartbeat    This provides a better experience since as soon as one virtual machine begins sending heartbeats, indicating it has successfully started up, the next machine will begin starting up. This happens even if the startDelay has not yet elapsed. Similarly, if one virtual machine fails to begin sending heartbeats, perhaps because it could not start up, other machines are not blocked from starting up since the startDelay eventually elapses. 
    """ # noqa: E501
    key: ManagedObjectReference
    start_order: StrictInt = Field(description="The autostart priority of this virtual machine.  Virtual machines with a lower number are powered on first. On host shutdown, the virtual machines are shut down in reverse order, meaning those with a higher number are powered off first.  Positive values indicate a start order and -1 indicates the machine can be powered on at any time. Machines with a -1 value are typically powered on and off after all virtual machines with positive startOrder values. Failure to meet the following requirements results in an InvalidArgument exception: - startOrder must be set to -1 if startAction is set to none - startOrder must be -1 or positive integers. Values such as 0 or   \\-2 are not valid. - startOrder is relative to other virtual machines in the autostart   sequence. Hence specifying a startOrder of 4 when there are only 3   virtual machines in the Autostart sequence is not valid.    If a newly established or changed startOrder value for a virtual machine matches an existing startOrder value, the newly applied value takes precedence, and the existing value is incremented by one. The incremented startOrder value is checked for collisions, and the same rule is applied if one is found. This simple system ensures no two virtual machines ever have the same order number.  For example, consider the case where there are three virtual machines with different startOrder values. Virtual machine A has not yet established a startOrder, virtual machine B has a startOrder value of 1 and Virtual Machine C has a startOrder value of 2. If virtual machine A's startOrder is set to 1, then virtual machine B's startOrder is incremented to 2. This creates a conflict with virtual machine C's startOrder value, which is also incremented, this time to 3. ", alias="startOrder")
    start_delay: StrictInt = Field(description="Delay in seconds before continuing with the next virtual machine in the order of machines to be started.  If the delay is specified as -1, then the system default is used. ", alias="startDelay")
    wait_for_heartbeat: AutoStartWaitHeartbeatSettingEnum = Field(alias="waitForHeartbeat")
    start_action: StrictStr = Field(description="How to start the virtual machine.  Valid settings are none or powerOn. If set to none, then the virtual machine does not participate in auto-start. ", alias="startAction")
    stop_delay: StrictInt = Field(description="Delay in seconds before continuing with the next virtual machine in the order sequence.  If the delay is -1, then the system default is used. ", alias="stopDelay")
    stop_action: StrictStr = Field(description="Defines the stop action for the virtual machine.  Can be set to none, systemDefault, powerOff, or suspend. If set to none, then the virtual machine does not participate in auto-stop. ", alias="stopAction")
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
        """Create an instance of AutoStartPowerInfo from a JSON string"""
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
        """Create an instance of AutoStartPowerInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


