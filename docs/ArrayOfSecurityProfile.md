# ArrayOfSecurityProfile

A boxed array of *SecurityProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SecurityProfile]**](SecurityProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_security_profile import ArrayOfSecurityProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfSecurityProfile from a JSON string
array_of_security_profile_instance = ArrayOfSecurityProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfSecurityProfile.to_json()

# convert the object into a dict
array_of_security_profile_dict = array_of_security_profile_instance.to_dict()
# create an instance of ArrayOfSecurityProfile from a dict
array_of_security_profile_form_dict = array_of_security_profile.from_dict(array_of_security_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


