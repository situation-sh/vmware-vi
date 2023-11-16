# ArrayOfHostSpecificationUpdateEvent

A boxed array of *HostSpecificationUpdateEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostSpecificationUpdateEvent]**](HostSpecificationUpdateEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_specification_update_event import ArrayOfHostSpecificationUpdateEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostSpecificationUpdateEvent from a JSON string
array_of_host_specification_update_event_instance = ArrayOfHostSpecificationUpdateEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostSpecificationUpdateEvent.to_json()

# convert the object into a dict
array_of_host_specification_update_event_dict = array_of_host_specification_update_event_instance.to_dict()
# create an instance of ArrayOfHostSpecificationUpdateEvent from a dict
array_of_host_specification_update_event_form_dict = array_of_host_specification_update_event.from_dict(array_of_host_specification_update_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


