# VirtualMachineWipeResult

Data structure used by wipeDisk to return the amount of disk space that can be saved on an Flex-SE disk if a subsequent shrinkDisk API is invoked on that disk.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_id** | **int** | The disk id for the disk that was wiped.  ***Since:*** vSphere API 5.1  | 
**shrinkable_disk_space** | **int** | The amount of shrinkable disk space in kB.  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.virtual_machine_wipe_result import VirtualMachineWipeResult

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineWipeResult from a JSON string
virtual_machine_wipe_result_instance = VirtualMachineWipeResult.from_json(json)
# print the JSON string representation of the object
print VirtualMachineWipeResult.to_json()

# convert the object into a dict
virtual_machine_wipe_result_dict = virtual_machine_wipe_result_instance.to_dict()
# create an instance of VirtualMachineWipeResult from a dict
virtual_machine_wipe_result_form_dict = virtual_machine_wipe_result.from_dict(virtual_machine_wipe_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


