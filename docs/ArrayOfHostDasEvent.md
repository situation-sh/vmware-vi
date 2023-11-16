# ArrayOfHostDasEvent

A boxed array of *HostDasEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostDasEvent]**](HostDasEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_das_event import ArrayOfHostDasEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostDasEvent from a JSON string
array_of_host_das_event_instance = ArrayOfHostDasEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostDasEvent.to_json()

# convert the object into a dict
array_of_host_das_event_dict = array_of_host_das_event_instance.to_dict()
# create an instance of ArrayOfHostDasEvent from a dict
array_of_host_das_event_form_dict = array_of_host_das_event.from_dict(array_of_host_das_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


