# FaultToleranceVMConfigSpec

FaultToleranceVMConfigSpec contains information about placement of fault tolerant VM.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm_config** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**disks** | [**List[FaultToleranceDiskSpec]**](FaultToleranceDiskSpec.md) | Array of disks associated with the VM  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.fault_tolerance_vm_config_spec import FaultToleranceVMConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of FaultToleranceVMConfigSpec from a JSON string
fault_tolerance_vm_config_spec_instance = FaultToleranceVMConfigSpec.from_json(json)
# print the JSON string representation of the object
print FaultToleranceVMConfigSpec.to_json()

# convert the object into a dict
fault_tolerance_vm_config_spec_dict = fault_tolerance_vm_config_spec_instance.to_dict()
# create an instance of FaultToleranceVMConfigSpec from a dict
fault_tolerance_vm_config_spec_form_dict = fault_tolerance_vm_config_spec.from_dict(fault_tolerance_vm_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


