# ArrayOfLocalLicenseSource

A boxed array of *LocalLicenseSource*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[LocalLicenseSource]**](LocalLicenseSource.md) |  | 

## Example

```python
from vmware_vi.models.array_of_local_license_source import ArrayOfLocalLicenseSource

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfLocalLicenseSource from a JSON string
array_of_local_license_source_instance = ArrayOfLocalLicenseSource.from_json(json)
# print the JSON string representation of the object
print ArrayOfLocalLicenseSource.to_json()

# convert the object into a dict
array_of_local_license_source_dict = array_of_local_license_source_instance.to_dict()
# create an instance of ArrayOfLocalLicenseSource from a dict
array_of_local_license_source_form_dict = array_of_local_license_source.from_dict(array_of_local_license_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


