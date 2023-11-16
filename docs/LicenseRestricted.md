# LicenseRestricted

This fault is thrown if the required licenses were unable to be checked out due to a restriction in the option file of the license server.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.license_restricted import LicenseRestricted

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseRestricted from a JSON string
license_restricted_instance = LicenseRestricted.from_json(json)
# print the JSON string representation of the object
print LicenseRestricted.to_json()

# convert the object into a dict
license_restricted_dict = license_restricted_instance.to_dict()
# create an instance of LicenseRestricted from a dict
license_restricted_form_dict = license_restricted.from_dict(license_restricted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


