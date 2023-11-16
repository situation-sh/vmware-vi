# OvfInvalidVmName

This fault is used if we can not normalize the vm name  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the invalid Virtual Machine  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_invalid_vm_name import OvfInvalidVmName

# TODO update the JSON string below
json = "{}"
# create an instance of OvfInvalidVmName from a JSON string
ovf_invalid_vm_name_instance = OvfInvalidVmName.from_json(json)
# print the JSON string representation of the object
print OvfInvalidVmName.to_json()

# convert the object into a dict
ovf_invalid_vm_name_dict = ovf_invalid_vm_name_instance.to_dict()
# create an instance of OvfInvalidVmName from a dict
ovf_invalid_vm_name_form_dict = ovf_invalid_vm_name.from_dict(ovf_invalid_vm_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


