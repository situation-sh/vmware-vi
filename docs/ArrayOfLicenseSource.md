# ArrayOfLicenseSource

A boxed array of *LicenseSource*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[LicenseSource]**](LicenseSource.md) |  | 

## Example

```python
from vmware_vi.models.array_of_license_source import ArrayOfLicenseSource

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfLicenseSource from a JSON string
array_of_license_source_instance = ArrayOfLicenseSource.from_json(json)
# print the JSON string representation of the object
print ArrayOfLicenseSource.to_json()

# convert the object into a dict
array_of_license_source_dict = array_of_license_source_instance.to_dict()
# create an instance of ArrayOfLicenseSource from a dict
array_of_license_source_form_dict = array_of_license_source.from_dict(array_of_license_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


