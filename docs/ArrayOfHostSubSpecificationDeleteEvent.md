# ArrayOfHostSubSpecificationDeleteEvent

A boxed array of *HostSubSpecificationDeleteEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostSubSpecificationDeleteEvent]**](HostSubSpecificationDeleteEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_sub_specification_delete_event import ArrayOfHostSubSpecificationDeleteEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostSubSpecificationDeleteEvent from a JSON string
array_of_host_sub_specification_delete_event_instance = ArrayOfHostSubSpecificationDeleteEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostSubSpecificationDeleteEvent.to_json()

# convert the object into a dict
array_of_host_sub_specification_delete_event_dict = array_of_host_sub_specification_delete_event_instance.to_dict()
# create an instance of ArrayOfHostSubSpecificationDeleteEvent from a dict
array_of_host_sub_specification_delete_event_form_dict = array_of_host_sub_specification_delete_event.from_dict(array_of_host_sub_specification_delete_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


