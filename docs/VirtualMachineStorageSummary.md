# VirtualMachineStorageSummary

A subset of the storage information of this virtual machine.  See *VirtualMachineStorageInfo* for a detailed storage break-up.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**committed** | **int** | Total storage space, in bytes, committed to this virtual machine across all datastores.  Essentially an aggregate of the property *VirtualMachineUsageOnDatastore.committed* across all datastores that this virtual machine is located on.  ***Since:*** vSphere API 4.0  | 
**uncommitted** | **int** | Additional storage space, in bytes, potentially used by this virtual machine on all datastores.  Essentially an aggregate of the property *VirtualMachineUsageOnDatastore.uncommitted* across all datastores that this virtual machine is located on.  ***Since:*** vSphere API 4.0  | 
**unshared** | **int** | Total storage space, in bytes, occupied by the virtual machine across all datastores, that is not shared with any other virtual machine.  ***Since:*** vSphere API 4.0  | 
**timestamp** | **datetime** | Time when values in this structure were last updated.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.virtual_machine_storage_summary import VirtualMachineStorageSummary

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineStorageSummary from a JSON string
virtual_machine_storage_summary_instance = VirtualMachineStorageSummary.from_json(json)
# print the JSON string representation of the object
print VirtualMachineStorageSummary.to_json()

# convert the object into a dict
virtual_machine_storage_summary_dict = virtual_machine_storage_summary_instance.to_dict()
# create an instance of VirtualMachineStorageSummary from a dict
virtual_machine_storage_summary_form_dict = virtual_machine_storage_summary.from_dict(virtual_machine_storage_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


