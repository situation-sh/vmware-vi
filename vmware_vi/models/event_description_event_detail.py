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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class EventDescriptionEventDetail(DataObject):
    """
    Each Event object provides an automatic event message string through its *fullFormattedMessage* property.  However, you can use the EventDetail object's properties to format an event message string that is appropriate when viewed from a specific context. The variable information (vm.name, and so on) is derived from the Event object's event arguments (*VmEventArgument*, and so on). 
    """ # noqa: E501
    key: StrictStr = Field(description="Type of event being described. ")
    description: Optional[StrictStr] = Field(default=None, description="A string that is a short human-parseable description of the event.  This is not the full message string (which may contain details of the arguments, etc.), but merely a more understandable, and localized, description of what the event stands for. It is meant for contexts where the _name_ of the event has to be displayed to end-users, e.g. when creating Event-based Alarms. \\` \\*   E.g., for *VmPoweredOnEvent*, the eventDescription in English might say \"VM Powered On\".  ***Since:*** vSphere API 4.0 ")
    category: StrictStr = Field(description="A category of events. ")
    format_on_datacenter: StrictStr = Field(description="A string that is appropriate in the context of a specific Datacenter.  For example, a renaming event in this context produces the following string:  \"Renamed {vm.name} from {oldName} to {newName}\"  where *oldName* and *newName* are properties of the VmRenamedEvent object. ", alias="formatOnDatacenter")
    format_on_compute_resource: StrictStr = Field(description="A string that is appropriate in the context of a specific cluster.  For example, a powering on event in this context produces the following string:  \"{vm.name} on {host.name} is powered on\". ", alias="formatOnComputeResource")
    format_on_host: StrictStr = Field(description="A string that is appropriate in the context of a specific Host.  For example, a powering on event in this context produces the following string:  \"{vm.name} is powered on\" ", alias="formatOnHost")
    format_on_vm: StrictStr = Field(description="A string that is appropriate for the context of a specific virtual machine.  For example, a powering on event in this context produces the following string:  \"Virtual machine on {host.name} is powered on\" ", alias="formatOnVm")
    full_format: StrictStr = Field(description="A string whose context is not entity-specific.  For example, a powering on event produces the following string:  \"{vm.name} on {host.name} in {datacenter.name} is powered on\" ", alias="fullFormat")
    long_description: Optional[StrictStr] = Field(default=None, description="A detailed description of the event.  It includes common causes and actions to remediate them. It may also include links to kb articles and other diagnostic information. For example, the BadUserNameSessionEvent may produce the following string:           <EventLongDescription id=\"vim.event.BadUserNameSessionEvent\">             <description>                The user could not be logged in because of an unknown or invalid                user name.             </description>             <cause>                <description>The user name was unknown to the system</description>                <action>Use a user name known to the system user directory</action>                <action>(On Linux) Check if the user directory is correctly                        configured.</action>                <action>Check the health of the domain controller (if you are using                        Active Directory)</action>             </cause>             <cause>                <description>The user provided an invalid password</description>                <action>Supply the correct password</action>             </cause>          </EventLongDescription>  ***Since:*** vSphere API 4.1 ", alias="longDescription")
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
        """Create an instance of EventDescriptionEventDetail from a JSON string"""
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
        """Create an instance of EventDescriptionEventDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

