# ArrayOfNamePasswordAuthentication

A boxed array of *NamePasswordAuthentication*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NamePasswordAuthentication]**](NamePasswordAuthentication.md) |  | 

## Example

```python
from vmware_vi.models.array_of_name_password_authentication import ArrayOfNamePasswordAuthentication

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNamePasswordAuthentication from a JSON string
array_of_name_password_authentication_instance = ArrayOfNamePasswordAuthentication.from_json(json)
# print the JSON string representation of the object
print ArrayOfNamePasswordAuthentication.to_json()

# convert the object into a dict
array_of_name_password_authentication_dict = array_of_name_password_authentication_instance.to_dict()
# create an instance of ArrayOfNamePasswordAuthentication from a dict
array_of_name_password_authentication_form_dict = array_of_name_password_authentication.from_dict(array_of_name_password_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


