# WipeDiskFault

This exception is thrown when VirtualMachine.wipeDisk encounters an error  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.wipe_disk_fault import WipeDiskFault

# TODO update the JSON string below
json = "{}"
# create an instance of WipeDiskFault from a JSON string
wipe_disk_fault_instance = WipeDiskFault.from_json(json)
# print the JSON string representation of the object
print WipeDiskFault.to_json()

# convert the object into a dict
wipe_disk_fault_dict = wipe_disk_fault_instance.to_dict()
# create an instance of WipeDiskFault from a dict
wipe_disk_fault_form_dict = wipe_disk_fault.from_dict(wipe_disk_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


