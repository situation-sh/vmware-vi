# ArrayOfPasswordField

A boxed array of *PasswordField*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PasswordField]**](PasswordField.md) |  | 

## Example

```python
from vmware_vi.models.array_of_password_field import ArrayOfPasswordField

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPasswordField from a JSON string
array_of_password_field_instance = ArrayOfPasswordField.from_json(json)
# print the JSON string representation of the object
print ArrayOfPasswordField.to_json()

# convert the object into a dict
array_of_password_field_dict = array_of_password_field_instance.to_dict()
# create an instance of ArrayOfPasswordField from a dict
array_of_password_field_form_dict = array_of_password_field.from_dict(array_of_password_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


