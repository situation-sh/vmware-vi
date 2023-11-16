# AuthorizationEvent

These events indicate authorization events. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.authorization_event import AuthorizationEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationEvent from a JSON string
authorization_event_instance = AuthorizationEvent.from_json(json)
# print the JSON string representation of the object
print AuthorizationEvent.to_json()

# convert the object into a dict
authorization_event_dict = authorization_event_instance.to_dict()
# create an instance of AuthorizationEvent from a dict
authorization_event_form_dict = authorization_event.from_dict(authorization_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


