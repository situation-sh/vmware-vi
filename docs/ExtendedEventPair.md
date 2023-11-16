# ExtendedEventPair

key/value pair  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from vmware_vi.models.extended_event_pair import ExtendedEventPair

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedEventPair from a JSON string
extended_event_pair_instance = ExtendedEventPair.from_json(json)
# print the JSON string representation of the object
print ExtendedEventPair.to_json()

# convert the object into a dict
extended_event_pair_dict = extended_event_pair_instance.to_dict()
# create an instance of ExtendedEventPair from a dict
extended_event_pair_form_dict = extended_event_pair.from_dict(extended_event_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


