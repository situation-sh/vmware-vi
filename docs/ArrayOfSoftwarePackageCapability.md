# ArrayOfSoftwarePackageCapability

A boxed array of *SoftwarePackageCapability*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SoftwarePackageCapability]**](SoftwarePackageCapability.md) |  | 

## Example

```python
from vmware_vi.models.array_of_software_package_capability import ArrayOfSoftwarePackageCapability

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfSoftwarePackageCapability from a JSON string
array_of_software_package_capability_instance = ArrayOfSoftwarePackageCapability.from_json(json)
# print the JSON string representation of the object
print ArrayOfSoftwarePackageCapability.to_json()

# convert the object into a dict
array_of_software_package_capability_dict = array_of_software_package_capability_instance.to_dict()
# create an instance of ArrayOfSoftwarePackageCapability from a dict
array_of_software_package_capability_form_dict = array_of_software_package_capability.from_dict(array_of_software_package_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


