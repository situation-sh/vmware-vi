# ArrayOfHostSpecificationChangedEvent

A boxed array of *HostSpecificationChangedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostSpecificationChangedEvent]**](HostSpecificationChangedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_specification_changed_event import ArrayOfHostSpecificationChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostSpecificationChangedEvent from a JSON string
array_of_host_specification_changed_event_instance = ArrayOfHostSpecificationChangedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostSpecificationChangedEvent.to_json()

# convert the object into a dict
array_of_host_specification_changed_event_dict = array_of_host_specification_changed_event_instance.to_dict()
# create an instance of ArrayOfHostSpecificationChangedEvent from a dict
array_of_host_specification_changed_event_form_dict = array_of_host_specification_changed_event.from_dict(array_of_host_specification_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


