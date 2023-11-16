# ArrayOfPasswordExpired

A boxed array of *PasswordExpired*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PasswordExpired]**](PasswordExpired.md) |  | 

## Example

```python
from vmware_vi.models.array_of_password_expired import ArrayOfPasswordExpired

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPasswordExpired from a JSON string
array_of_password_expired_instance = ArrayOfPasswordExpired.from_json(json)
# print the JSON string representation of the object
print ArrayOfPasswordExpired.to_json()

# convert the object into a dict
array_of_password_expired_dict = array_of_password_expired_instance.to_dict()
# create an instance of ArrayOfPasswordExpired from a dict
array_of_password_expired_form_dict = array_of_password_expired.from_dict(array_of_password_expired_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


