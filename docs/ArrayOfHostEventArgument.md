# ArrayOfHostEventArgument

A boxed array of *HostEventArgument*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostEventArgument]**](HostEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_event_argument import ArrayOfHostEventArgument

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostEventArgument from a JSON string
array_of_host_event_argument_instance = ArrayOfHostEventArgument.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostEventArgument.to_json()

# convert the object into a dict
array_of_host_event_argument_dict = array_of_host_event_argument_instance.to_dict()
# create an instance of ArrayOfHostEventArgument from a dict
array_of_host_event_argument_form_dict = array_of_host_event_argument.from_dict(array_of_host_event_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


