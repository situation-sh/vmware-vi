# FileBackedVirtualDiskSpec

Specification used to create a file based virtual disk  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity_kb** | **int** | Specify the capacity of the virtual disk in Kb.  ***Since:*** VI API 2.5  | 
**profile** | [**List[VirtualMachineProfileSpec]**](VirtualMachineProfileSpec.md) | Virtual Disk Profile requirement.  Profiles are solution specifics. Profile Based Storage Management is a vSphere server extension. The API users who want to provision VMs using Storage Profiles, need to interact with it. This is an optional parameter and if user doesn&#39;t specify profile, the default behavior will apply.  ***Since:*** vSphere API 5.5  | [optional] 
**crypto** | [**CryptoSpec**](CryptoSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.file_backed_virtual_disk_spec import FileBackedVirtualDiskSpec

# TODO update the JSON string below
json = "{}"
# create an instance of FileBackedVirtualDiskSpec from a JSON string
file_backed_virtual_disk_spec_instance = FileBackedVirtualDiskSpec.from_json(json)
# print the JSON string representation of the object
print FileBackedVirtualDiskSpec.to_json()

# convert the object into a dict
file_backed_virtual_disk_spec_dict = file_backed_virtual_disk_spec_instance.to_dict()
# create an instance of FileBackedVirtualDiskSpec from a dict
file_backed_virtual_disk_spec_form_dict = file_backed_virtual_disk_spec.from_dict(file_backed_virtual_disk_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


