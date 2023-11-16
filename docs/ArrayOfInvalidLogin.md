# ArrayOfInvalidLogin

A boxed array of *InvalidLogin*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InvalidLogin]**](InvalidLogin.md) |  | 

## Example

```python
from vmware_vi.models.array_of_invalid_login import ArrayOfInvalidLogin

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInvalidLogin from a JSON string
array_of_invalid_login_instance = ArrayOfInvalidLogin.from_json(json)
# print the JSON string representation of the object
print ArrayOfInvalidLogin.to_json()

# convert the object into a dict
array_of_invalid_login_dict = array_of_invalid_login_instance.to_dict()
# create an instance of ArrayOfInvalidLogin from a dict
array_of_invalid_login_form_dict = array_of_invalid_login.from_dict(array_of_invalid_login_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


