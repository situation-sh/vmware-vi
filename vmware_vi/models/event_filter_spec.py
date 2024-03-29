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
from vmware_vi.models.event_filter_spec_by_entity import EventFilterSpecByEntity
from vmware_vi.models.event_filter_spec_by_time import EventFilterSpecByTime
from vmware_vi.models.event_filter_spec_by_username import EventFilterSpecByUsername
from vmware_vi.models.managed_object_reference import ManagedObjectReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class EventFilterSpec(DataObject):
    """
    Event filter used to query events in the history collector database.  The client creates an event history collector with a filter specification, then retrieves the events from the event history collector. 
    """ # noqa: E501
    entity: Optional[EventFilterSpecByEntity] = None
    time: Optional[EventFilterSpecByTime] = None
    user_name: Optional[EventFilterSpecByUsername] = Field(default=None, alias="userName")
    event_chain_id: Optional[StrictInt] = Field(default=None, description="The filter specification for retrieving events by chain ID.  If the property is not set, events with any chain ID are collected. ", alias="eventChainId")
    alarm: Optional[ManagedObjectReference] = None
    scheduled_task: Optional[ManagedObjectReference] = Field(default=None, alias="scheduledTask")
    disable_full_message: Optional[StrictBool] = Field(default=None, description="Flag to specify whether or not to prepare the full formatted message for each event.  If the property is not set, the collected events do not include the full formatted message. ", alias="disableFullMessage")
    category: Optional[List[StrictStr]] = Field(default=None, description="This property, if set, limits the set of collected events to those associated with the specified category.  If the property is not set, events are collected regardless of their association with any category. \"category\" here is the same as Event.severity. ")
    type: Optional[List[StrictStr]] = Field(default=None, description="Deprecated as of vSphere API 4.0, use *EventFilterSpec.eventTypeId* instead.  This property, if set, limits the set of collected events to those specified types.  If the property is not set, events are collected regardless of their types. ")
    tag: Optional[List[StrictStr]] = Field(default=None, description="This property, if set, limits the set of filtered events to those that have it.  If not set, or the size of it 0, the tag of an event is disregarded. A blank string indicates events without tags.  ***Since:*** vSphere API 4.0 ")
    event_type_id: Optional[List[StrictStr]] = Field(default=None, description="This property, if set, limits the set of collected events to those specified types.  Note: if both *EventFilterSpec.eventTypeId* and *EventFilterSpec.type* are specified, an exception may be thrown by *EventManager.CreateCollectorForEvents*.  The semantics of how eventTypeId matching is done is as follows: - If the event being collected is of type *EventEx*   or *ExtendedEvent*, then we match against the   <code>eventTypeId</code> (for <code>EventEx</code>) or   <code>eventId</code> (for <code>ExtendedEvent</code>) member of the Event. - Otherwise, we match against the type of the Event itself.    If neither this property, nor <code>type</code>, is set, events are collected regardless of their types.  ***Since:*** vSphere API 4.0 ", alias="eventTypeId")
    max_count: Optional[StrictInt] = Field(default=None, description="This property, if set, specifies the maximum number of returned events.  If unset, the default maximum number will be used. Using this property with *EventManager.CreateCollectorForEvents* is more efficient than a call to *HistoryCollector.SetCollectorPageSize*.  ***Since:*** vSphere API 6.5 ", alias="maxCount")
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
        """Create an instance of EventFilterSpec from a JSON string"""
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
        """Create an instance of EventFilterSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


