# LicenseSourceUnavailable

A LicenseSourceUnavailable is thrown if it is unable to check out a license because the license source is unavailable.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_source** | [**LicenseSource**](LicenseSource.md) |  | 

## Example

```python
from vmware_vi.models.license_source_unavailable import LicenseSourceUnavailable

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseSourceUnavailable from a JSON string
license_source_unavailable_instance = LicenseSourceUnavailable.from_json(json)
# print the JSON string representation of the object
print LicenseSourceUnavailable.to_json()

# convert the object into a dict
license_source_unavailable_dict = license_source_unavailable_instance.to_dict()
# create an instance of LicenseSourceUnavailable from a dict
license_source_unavailable_form_dict = license_source_unavailable.from_dict(license_source_unavailable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


