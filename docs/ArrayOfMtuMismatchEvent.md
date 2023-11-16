# ArrayOfMtuMismatchEvent

A boxed array of *MtuMismatchEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[MtuMismatchEvent]**](MtuMismatchEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_mtu_mismatch_event import ArrayOfMtuMismatchEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfMtuMismatchEvent from a JSON string
array_of_mtu_mismatch_event_instance = ArrayOfMtuMismatchEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfMtuMismatchEvent.to_json()

# convert the object into a dict
array_of_mtu_mismatch_event_dict = array_of_mtu_mismatch_event_instance.to_dict()
# create an instance of ArrayOfMtuMismatchEvent from a dict
array_of_mtu_mismatch_event_form_dict = array_of_mtu_mismatch_event.from_dict(array_of_mtu_mismatch_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


