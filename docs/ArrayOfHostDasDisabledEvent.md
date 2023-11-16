# ArrayOfHostDasDisabledEvent

A boxed array of *HostDasDisabledEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostDasDisabledEvent]**](HostDasDisabledEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_das_disabled_event import ArrayOfHostDasDisabledEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostDasDisabledEvent from a JSON string
array_of_host_das_disabled_event_instance = ArrayOfHostDasDisabledEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostDasDisabledEvent.to_json()

# convert the object into a dict
array_of_host_das_disabled_event_dict = array_of_host_das_disabled_event_instance.to_dict()
# create an instance of ArrayOfHostDasDisabledEvent from a dict
array_of_host_das_disabled_event_form_dict = array_of_host_das_disabled_event.from_dict(array_of_host_das_disabled_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


