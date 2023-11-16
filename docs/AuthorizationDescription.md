# AuthorizationDescription

Static strings for authorization. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**privilege** | [**List[ElementDescription]**](ElementDescription.md) | Description of the privilege.  | 
**privilege_group** | [**List[ElementDescription]**](ElementDescription.md) | Description of a category of similar privileges, grouped together for convenience.  | 

## Example

```python
from vmware_vi.models.authorization_description import AuthorizationDescription

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationDescription from a JSON string
authorization_description_instance = AuthorizationDescription.from_json(json)
# print the JSON string representation of the object
print AuthorizationDescription.to_json()

# convert the object into a dict
authorization_description_dict = authorization_description_instance.to_dict()
# create an instance of AuthorizationDescription from a dict
authorization_description_form_dict = authorization_description.from_dict(authorization_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


