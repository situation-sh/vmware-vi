# ArrayOfAuthorizationRole

A boxed array of *AuthorizationRole*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AuthorizationRole]**](AuthorizationRole.md) |  | 

## Example

```python
from vmware_vi.models.array_of_authorization_role import ArrayOfAuthorizationRole

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfAuthorizationRole from a JSON string
array_of_authorization_role_instance = ArrayOfAuthorizationRole.from_json(json)
# print the JSON string representation of the object
print ArrayOfAuthorizationRole.to_json()

# convert the object into a dict
array_of_authorization_role_dict = array_of_authorization_role_instance.to_dict()
# create an instance of ArrayOfAuthorizationRole from a dict
array_of_authorization_role_form_dict = array_of_authorization_role.from_dict(array_of_authorization_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


