# ArrayOfOvfInvalidPackage

A boxed array of *OvfInvalidPackage*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OvfInvalidPackage]**](OvfInvalidPackage.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ovf_invalid_package import ArrayOfOvfInvalidPackage

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOvfInvalidPackage from a JSON string
array_of_ovf_invalid_package_instance = ArrayOfOvfInvalidPackage.from_json(json)
# print the JSON string representation of the object
print ArrayOfOvfInvalidPackage.to_json()

# convert the object into a dict
array_of_ovf_invalid_package_dict = array_of_ovf_invalid_package_instance.to_dict()
# create an instance of ArrayOfOvfInvalidPackage from a dict
array_of_ovf_invalid_package_form_dict = array_of_ovf_invalid_package.from_dict(array_of_ovf_invalid_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


