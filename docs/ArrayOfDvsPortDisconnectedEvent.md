# ArrayOfDvsPortDisconnectedEvent

A boxed array of *DvsPortDisconnectedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DvsPortDisconnectedEvent]**](DvsPortDisconnectedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_port_disconnected_event import ArrayOfDvsPortDisconnectedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDvsPortDisconnectedEvent from a JSON string
array_of_dvs_port_disconnected_event_instance = ArrayOfDvsPortDisconnectedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfDvsPortDisconnectedEvent.to_json()

# convert the object into a dict
array_of_dvs_port_disconnected_event_dict = array_of_dvs_port_disconnected_event_instance.to_dict()
# create an instance of ArrayOfDvsPortDisconnectedEvent from a dict
array_of_dvs_port_disconnected_event_form_dict = array_of_dvs_port_disconnected_event.from_dict(array_of_dvs_port_disconnected_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


