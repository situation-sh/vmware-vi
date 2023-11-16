# ArrayOfSoftwarePackage

A boxed array of *SoftwarePackage*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SoftwarePackage]**](SoftwarePackage.md) |  | 

## Example

```python
from vmware_vi.models.array_of_software_package import ArrayOfSoftwarePackage

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfSoftwarePackage from a JSON string
array_of_software_package_instance = ArrayOfSoftwarePackage.from_json(json)
# print the JSON string representation of the object
print ArrayOfSoftwarePackage.to_json()

# convert the object into a dict
array_of_software_package_dict = array_of_software_package_instance.to_dict()
# create an instance of ArrayOfSoftwarePackage from a dict
array_of_software_package_form_dict = array_of_software_package.from_dict(array_of_software_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


