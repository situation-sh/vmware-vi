# Event

This event is the base data object type from which all events inherit.  All event objects are data structures that describe events. While event data objects are data structures that describe events, event data type documentation may describe what the event records, rather than the data structure, itself. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **int** | The event ID.  | 
**chain_id** | **int** | The parent or group ID.  | 
**created_time** | **datetime** | The time the event was created.  | 
**user_name** | **str** | The user who caused the event.  | 
**datacenter** | [**DatacenterEventArgument**](DatacenterEventArgument.md) |  | [optional] 
**compute_resource** | [**ComputeResourceEventArgument**](ComputeResourceEventArgument.md) |  | [optional] 
**host** | [**HostEventArgument**](HostEventArgument.md) |  | [optional] 
**vm** | [**VmEventArgument**](VmEventArgument.md) |  | [optional] 
**ds** | [**DatastoreEventArgument**](DatastoreEventArgument.md) |  | [optional] 
**net** | [**NetworkEventArgument**](NetworkEventArgument.md) |  | [optional] 
**dvs** | [**DvsEventArgument**](DvsEventArgument.md) |  | [optional] 
**full_formatted_message** | **str** | A formatted text message describing the event.  The message may be localized.  | [optional] 
**change_tag** | **str** | The user entered tag to identify the operations and their side effects  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.event import Event

# TODO update the JSON string below
json = "{}"
# create an instance of Event from a JSON string
event_instance = Event.from_json(json)
# print the JSON string representation of the object
print Event.to_json()

# convert the object into a dict
event_dict = event_instance.to_dict()
# create an instance of Event from a dict
event_form_dict = event.from_dict(event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


