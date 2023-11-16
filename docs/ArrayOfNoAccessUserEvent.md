# ArrayOfNoAccessUserEvent

A boxed array of *NoAccessUserEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NoAccessUserEvent]**](NoAccessUserEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_no_access_user_event import ArrayOfNoAccessUserEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNoAccessUserEvent from a JSON string
array_of_no_access_user_event_instance = ArrayOfNoAccessUserEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfNoAccessUserEvent.to_json()

# convert the object into a dict
array_of_no_access_user_event_dict = array_of_no_access_user_event_instance.to_dict()
# create an instance of ArrayOfNoAccessUserEvent from a dict
array_of_no_access_user_event_form_dict = array_of_no_access_user_event.from_dict(array_of_no_access_user_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


