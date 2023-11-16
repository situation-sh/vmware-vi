# NotAuthenticated

Thrown when an operation is denied because the session has not yet successfully logged in.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.not_authenticated import NotAuthenticated

# TODO update the JSON string below
json = "{}"
# create an instance of NotAuthenticated from a JSON string
not_authenticated_instance = NotAuthenticated.from_json(json)
# print the JSON string representation of the object
print NotAuthenticated.to_json()

# convert the object into a dict
not_authenticated_dict = not_authenticated_instance.to_dict()
# create an instance of NotAuthenticated from a dict
not_authenticated_form_dict = not_authenticated.from_dict(not_authenticated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


