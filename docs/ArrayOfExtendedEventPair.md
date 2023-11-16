# ArrayOfExtendedEventPair

A boxed array of *ExtendedEventPair*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ExtendedEventPair]**](ExtendedEventPair.md) |  | 

## Example

```python
from vmware_vi.models.array_of_extended_event_pair import ArrayOfExtendedEventPair

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfExtendedEventPair from a JSON string
array_of_extended_event_pair_instance = ArrayOfExtendedEventPair.from_json(json)
# print the JSON string representation of the object
print ArrayOfExtendedEventPair.to_json()

# convert the object into a dict
array_of_extended_event_pair_dict = array_of_extended_event_pair_instance.to_dict()
# create an instance of ArrayOfExtendedEventPair from a dict
array_of_extended_event_pair_form_dict = array_of_extended_event_pair.from_dict(array_of_extended_event_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


