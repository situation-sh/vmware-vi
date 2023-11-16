# UpgradeVMRequestType

The parameters of *VirtualMachine.UpgradeVM_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | If specified, upgrade to that specified version. If not specified, upgrade to the most current virtual hardware supported on the host.  | [optional] 

## Example

```python
from vmware_vi.models.upgrade_vm_request_type import UpgradeVMRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeVMRequestType from a JSON string
upgrade_vm_request_type_instance = UpgradeVMRequestType.from_json(json)
# print the JSON string representation of the object
print UpgradeVMRequestType.to_json()

# convert the object into a dict
upgrade_vm_request_type_dict = upgrade_vm_request_type_instance.to_dict()
# create an instance of UpgradeVMRequestType from a dict
upgrade_vm_request_type_form_dict = upgrade_vm_request_type.from_dict(upgrade_vm_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


