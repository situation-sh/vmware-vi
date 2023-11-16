# VsanDiskFault

Base exception class for VSAN disk-related faults.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The canonical name for the disk at hand, if applicable.  See also *ScsiLun.canonicalName*.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.vsan_disk_fault import VsanDiskFault

# TODO update the JSON string below
json = "{}"
# create an instance of VsanDiskFault from a JSON string
vsan_disk_fault_instance = VsanDiskFault.from_json(json)
# print the JSON string representation of the object
print VsanDiskFault.to_json()

# convert the object into a dict
vsan_disk_fault_dict = vsan_disk_fault_instance.to_dict()
# create an instance of VsanDiskFault from a dict
vsan_disk_fault_form_dict = vsan_disk_fault.from_dict(vsan_disk_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


