# ApplyEvcModeVMRequestType

The parameters of *VirtualMachine.ApplyEvcModeVM_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mask** | [**List[HostFeatureMask]**](HostFeatureMask.md) | The feature masks to apply to the virtual machine. An empty set of masks will clear EVC settings.  ***Since:*** vSphere API 5.1  | [optional] 
**complete_masks** | **bool** | Defaults to true if not set. A true value implies that any unspecified feature will not be exposed to the guest. A false value will expose any unspecified feature to the guest with the value of the host.  | [optional] 

## Example

```python
from vmware_vi.models.apply_evc_mode_vm_request_type import ApplyEvcModeVMRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyEvcModeVMRequestType from a JSON string
apply_evc_mode_vm_request_type_instance = ApplyEvcModeVMRequestType.from_json(json)
# print the JSON string representation of the object
print ApplyEvcModeVMRequestType.to_json()

# convert the object into a dict
apply_evc_mode_vm_request_type_dict = apply_evc_mode_vm_request_type_instance.to_dict()
# create an instance of ApplyEvcModeVMRequestType from a dict
apply_evc_mode_vm_request_type_form_dict = apply_evc_mode_vm_request_type.from_dict(apply_evc_mode_vm_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


