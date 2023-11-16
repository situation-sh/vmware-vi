# ArrayOfLicenseExpired

A boxed array of *LicenseExpired*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[LicenseExpired]**](LicenseExpired.md) |  | 

## Example

```python
from vmware_vi.models.array_of_license_expired import ArrayOfLicenseExpired

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfLicenseExpired from a JSON string
array_of_license_expired_instance = ArrayOfLicenseExpired.from_json(json)
# print the JSON string representation of the object
print ArrayOfLicenseExpired.to_json()

# convert the object into a dict
array_of_license_expired_dict = array_of_license_expired_instance.to_dict()
# create an instance of ArrayOfLicenseExpired from a dict
array_of_license_expired_form_dict = array_of_license_expired.from_dict(array_of_license_expired_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


