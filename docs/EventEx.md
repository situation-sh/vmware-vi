# EventEx

EventEx is a dynamically typed Event class, whose type is indicated by its eventTypeId property.  A collection of eventTypeIds is registered by Extensions, which can now pass in optional type information for each eventTypeId which indicates the applicable argument names and types, among other properties.  EventEx allows event arguments of any type, though today, the system only supports \"string\" and \"moid\" (a string which can be interpreted as an object ID in the system) as argument types. In the future, the system may optionally strongly check the types of the arguments in the event against the declared type information, based on how the event type is declared.  EventEx also allows arbitrary \"event object\"s - the object which the event refers to. You can put in any object identifier as the objectId, but objectType should be filled in only if the object is actually present in the VC Server's ManagedEntity inventory.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type_id** | **str** | The type of the event.  ***Since:*** vSphere API 4.0  | 
**severity** | **str** | The severity level of the message: null&#x3D;&amp;gt;info.  See also *EventEventSeverity_enum*.  ***Since:*** vSphere API 4.0  | [optional] 
**message** | **str** | An arbitrary message string, not localized.  ***Since:*** vSphere API 4.0  | [optional] 
**arguments** | [**List[KeyAnyValue]**](KeyAnyValue.md) | The event arguments associated with the event  ***Since:*** vSphere API 4.0  | [optional] 
**object_id** | **str** | The ID of the object (VM, Host, Folder..) which the event pertains to.  Federated or local inventory path.  ***Since:*** vSphere API 4.0  | [optional] 
**object_type** | **str** | the type of the object, if known to the VirtualCenter inventory  ***Since:*** vSphere API 4.0  | [optional] 
**object_name** | **str** | The name of the object  ***Since:*** vSphere API 4.1  | [optional] 
**fault** | [**MethodFault**](MethodFault.md) |  | [optional] 

## Example

```python
from vmware_vi.models.event_ex import EventEx

# TODO update the JSON string below
json = "{}"
# create an instance of EventEx from a JSON string
event_ex_instance = EventEx.from_json(json)
# print the JSON string representation of the object
print EventEx.to_json()

# convert the object into a dict
event_ex_dict = event_ex_instance.to_dict()
# create an instance of EventEx from a dict
event_ex_form_dict = event_ex.from_dict(event_ex_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


