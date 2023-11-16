# FaultToleranceNeedsThickDisk

Fault Tolerance VM requires thick disks  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm_name** | **str** | The name of the VM.  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.fault_tolerance_needs_thick_disk import FaultToleranceNeedsThickDisk

# TODO update the JSON string below
json = "{}"
# create an instance of FaultToleranceNeedsThickDisk from a JSON string
fault_tolerance_needs_thick_disk_instance = FaultToleranceNeedsThickDisk.from_json(json)
# print the JSON string representation of the object
print FaultToleranceNeedsThickDisk.to_json()

# convert the object into a dict
fault_tolerance_needs_thick_disk_dict = fault_tolerance_needs_thick_disk_instance.to_dict()
# create an instance of FaultToleranceNeedsThickDisk from a dict
fault_tolerance_needs_thick_disk_form_dict = fault_tolerance_needs_thick_disk.from_dict(fault_tolerance_needs_thick_disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


