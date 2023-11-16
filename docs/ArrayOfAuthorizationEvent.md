# ArrayOfAuthorizationEvent

A boxed array of *AuthorizationEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AuthorizationEvent]**](AuthorizationEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_authorization_event import ArrayOfAuthorizationEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfAuthorizationEvent from a JSON string
array_of_authorization_event_instance = ArrayOfAuthorizationEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfAuthorizationEvent.to_json()

# convert the object into a dict
array_of_authorization_event_dict = array_of_authorization_event_instance.to_dict()
# create an instance of ArrayOfAuthorizationEvent from a dict
array_of_authorization_event_form_dict = array_of_authorization_event.from_dict(array_of_authorization_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


