# ArrayOfHostLicenseSpec

A boxed array of *HostLicenseSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostLicenseSpec]**](HostLicenseSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_license_spec import ArrayOfHostLicenseSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostLicenseSpec from a JSON string
array_of_host_license_spec_instance = ArrayOfHostLicenseSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostLicenseSpec.to_json()

# convert the object into a dict
array_of_host_license_spec_dict = array_of_host_license_spec_instance.to_dict()
# create an instance of ArrayOfHostLicenseSpec from a dict
array_of_host_license_spec_form_dict = array_of_host_license_spec.from_dict(array_of_host_license_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


