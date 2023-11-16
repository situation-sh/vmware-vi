# ArrayOfMtuMatchEvent

A boxed array of *MtuMatchEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[MtuMatchEvent]**](MtuMatchEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_mtu_match_event import ArrayOfMtuMatchEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfMtuMatchEvent from a JSON string
array_of_mtu_match_event_instance = ArrayOfMtuMatchEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfMtuMatchEvent.to_json()

# convert the object into a dict
array_of_mtu_match_event_dict = array_of_mtu_match_event_instance.to_dict()
# create an instance of ArrayOfMtuMatchEvent from a dict
array_of_mtu_match_event_form_dict = array_of_mtu_match_event.from_dict(array_of_mtu_match_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


