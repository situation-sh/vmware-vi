# ArrayOfHostDasEnablingEvent

A boxed array of *HostDasEnablingEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostDasEnablingEvent]**](HostDasEnablingEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_das_enabling_event import ArrayOfHostDasEnablingEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostDasEnablingEvent from a JSON string
array_of_host_das_enabling_event_instance = ArrayOfHostDasEnablingEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostDasEnablingEvent.to_json()

# convert the object into a dict
array_of_host_das_enabling_event_dict = array_of_host_das_enabling_event_instance.to_dict()
# create an instance of ArrayOfHostDasEnablingEvent from a dict
array_of_host_das_enabling_event_form_dict = array_of_host_das_enabling_event.from_dict(array_of_host_das_enabling_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


