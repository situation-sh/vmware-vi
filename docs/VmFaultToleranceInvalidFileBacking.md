# VmFaultToleranceInvalidFileBacking

Indicates the file backing for some device prevents fault tolerance protection  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backing_type** | **str** | The device type of the file backing  ***Since:*** vSphere API 4.0  | [optional] 
**backing_filename** | **str** |  | [optional] 

## Example

```python
from vmware_vi.models.vm_fault_tolerance_invalid_file_backing import VmFaultToleranceInvalidFileBacking

# TODO update the JSON string below
json = "{}"
# create an instance of VmFaultToleranceInvalidFileBacking from a JSON string
vm_fault_tolerance_invalid_file_backing_instance = VmFaultToleranceInvalidFileBacking.from_json(json)
# print the JSON string representation of the object
print VmFaultToleranceInvalidFileBacking.to_json()

# convert the object into a dict
vm_fault_tolerance_invalid_file_backing_dict = vm_fault_tolerance_invalid_file_backing_instance.to_dict()
# create an instance of VmFaultToleranceInvalidFileBacking from a dict
vm_fault_tolerance_invalid_file_backing_form_dict = vm_fault_tolerance_invalid_file_backing.from_dict(vm_fault_tolerance_invalid_file_backing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


