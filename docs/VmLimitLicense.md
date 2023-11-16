# VmLimitLicense

A VmLimitLicense fault is thrown if powering on the virtual machine would exceed the maximum number of running virtual machines allowed. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The maximum number of running virtual machines limit.  | 

## Example

```python
from vmware_vi.models.vm_limit_license import VmLimitLicense

# TODO update the JSON string below
json = "{}"
# create an instance of VmLimitLicense from a JSON string
vm_limit_license_instance = VmLimitLicense.from_json(json)
# print the JSON string representation of the object
print VmLimitLicense.to_json()

# convert the object into a dict
vm_limit_license_dict = vm_limit_license_instance.to_dict()
# create an instance of VmLimitLicense from a dict
vm_limit_license_form_dict = vm_limit_license.from_dict(vm_limit_license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


