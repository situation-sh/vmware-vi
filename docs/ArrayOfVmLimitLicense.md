# ArrayOfVmLimitLicense

A boxed array of *VmLimitLicense*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmLimitLicense]**](VmLimitLicense.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_limit_license import ArrayOfVmLimitLicense

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmLimitLicense from a JSON string
array_of_vm_limit_license_instance = ArrayOfVmLimitLicense.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmLimitLicense.to_json()

# convert the object into a dict
array_of_vm_limit_license_dict = array_of_vm_limit_license_instance.to_dict()
# create an instance of ArrayOfVmLimitLicense from a dict
array_of_vm_limit_license_form_dict = array_of_vm_limit_license.from_dict(array_of_vm_limit_license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


