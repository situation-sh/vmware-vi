# ArrayOfHostNonCompliantEvent

A boxed array of *HostNonCompliantEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNonCompliantEvent]**](HostNonCompliantEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_non_compliant_event import ArrayOfHostNonCompliantEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNonCompliantEvent from a JSON string
array_of_host_non_compliant_event_instance = ArrayOfHostNonCompliantEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNonCompliantEvent.to_json()

# convert the object into a dict
array_of_host_non_compliant_event_dict = array_of_host_non_compliant_event_instance.to_dict()
# create an instance of ArrayOfHostNonCompliantEvent from a dict
array_of_host_non_compliant_event_form_dict = array_of_host_non_compliant_event.from_dict(array_of_host_non_compliant_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


