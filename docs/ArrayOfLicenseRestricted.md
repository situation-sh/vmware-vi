# ArrayOfLicenseRestricted

A boxed array of *LicenseRestricted*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[LicenseRestricted]**](LicenseRestricted.md) |  | 

## Example

```python
from vmware_vi.models.array_of_license_restricted import ArrayOfLicenseRestricted

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfLicenseRestricted from a JSON string
array_of_license_restricted_instance = ArrayOfLicenseRestricted.from_json(json)
# print the JSON string representation of the object
print ArrayOfLicenseRestricted.to_json()

# convert the object into a dict
array_of_license_restricted_dict = array_of_license_restricted_instance.to_dict()
# create an instance of ArrayOfLicenseRestricted from a dict
array_of_license_restricted_form_dict = array_of_license_restricted.from_dict(array_of_license_restricted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


