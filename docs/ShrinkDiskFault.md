# ShrinkDiskFault

This exception is thrown when VirtualMachine.shrinkDisk encounters an error  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_id** | **int** | Disk Id of the virtual disk that caused the fault  ***Since:*** vSphere API 5.1  | [optional] 

## Example

```python
from vmware_vi.models.shrink_disk_fault import ShrinkDiskFault

# TODO update the JSON string below
json = "{}"
# create an instance of ShrinkDiskFault from a JSON string
shrink_disk_fault_instance = ShrinkDiskFault.from_json(json)
# print the JSON string representation of the object
print ShrinkDiskFault.to_json()

# convert the object into a dict
shrink_disk_fault_dict = shrink_disk_fault_instance.to_dict()
# create an instance of ShrinkDiskFault from a dict
shrink_disk_fault_form_dict = shrink_disk_fault.from_dict(shrink_disk_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


