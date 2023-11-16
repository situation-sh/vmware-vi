# ArrayOfLicenseServerUnavailable

A boxed array of *LicenseServerUnavailable*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[LicenseServerUnavailable]**](LicenseServerUnavailable.md) |  | 

## Example

```python
from vmware_vi.models.array_of_license_server_unavailable import ArrayOfLicenseServerUnavailable

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfLicenseServerUnavailable from a JSON string
array_of_license_server_unavailable_instance = ArrayOfLicenseServerUnavailable.from_json(json)
# print the JSON string representation of the object
print ArrayOfLicenseServerUnavailable.to_json()

# convert the object into a dict
array_of_license_server_unavailable_dict = array_of_license_server_unavailable_instance.to_dict()
# create an instance of ArrayOfLicenseServerUnavailable from a dict
array_of_license_server_unavailable_form_dict = array_of_license_server_unavailable.from_dict(array_of_license_server_unavailable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


