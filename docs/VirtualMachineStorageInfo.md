# VirtualMachineStorageInfo

Information about the amount of storage used by a virtual machine across datastores that it is located on.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**per_datastore_usage** | [**List[VirtualMachineUsageOnDatastore]**](VirtualMachineUsageOnDatastore.md) | Storage space used by this virtual machine on all datastores that it is located on.  Total storage space committed to this virtual machine across all datastores is simply an aggregate of the property *VirtualMachineUsageOnDatastore.committed*.  See also *VirtualMachineStorageSummary.committed*.  ***Since:*** vSphere API 4.0  | [optional] 
**timestamp** | **datetime** | Time when values in this structure were last updated.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.virtual_machine_storage_info import VirtualMachineStorageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineStorageInfo from a JSON string
virtual_machine_storage_info_instance = VirtualMachineStorageInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineStorageInfo.to_json()

# convert the object into a dict
virtual_machine_storage_info_dict = virtual_machine_storage_info_instance.to_dict()
# create an instance of VirtualMachineStorageInfo from a dict
virtual_machine_storage_info_form_dict = virtual_machine_storage_info.from_dict(virtual_machine_storage_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


