# ArrayOfAuthorizationDescription

A boxed array of *AuthorizationDescription*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AuthorizationDescription]**](AuthorizationDescription.md) |  | 

## Example

```python
from vmware_vi.models.array_of_authorization_description import ArrayOfAuthorizationDescription

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfAuthorizationDescription from a JSON string
array_of_authorization_description_instance = ArrayOfAuthorizationDescription.from_json(json)
# print the JSON string representation of the object
print ArrayOfAuthorizationDescription.to_json()

# convert the object into a dict
array_of_authorization_description_dict = array_of_authorization_description_instance.to_dict()
# create an instance of ArrayOfAuthorizationDescription from a dict
array_of_authorization_description_form_dict = array_of_authorization_description.from_dict(array_of_authorization_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


