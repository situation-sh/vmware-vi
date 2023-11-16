# VStorageObjectAssociationsVmDiskAssociations

This data object contains infomation of a VM Disk associations.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm_id** | **str** | ID of the virtual machine.  ***Since:*** vSphere API 6.7  | 
**disk_key** | **int** | Device key of the disk attached to the VM.  ***Since:*** vSphere API 6.7  | 

## Example

```python
from vmware_vi.models.v_storage_object_associations_vm_disk_associations import VStorageObjectAssociationsVmDiskAssociations

# TODO update the JSON string below
json = "{}"
# create an instance of VStorageObjectAssociationsVmDiskAssociations from a JSON string
v_storage_object_associations_vm_disk_associations_instance = VStorageObjectAssociationsVmDiskAssociations.from_json(json)
# print the JSON string representation of the object
print VStorageObjectAssociationsVmDiskAssociations.to_json()

# convert the object into a dict
v_storage_object_associations_vm_disk_associations_dict = v_storage_object_associations_vm_disk_associations_instance.to_dict()
# create an instance of VStorageObjectAssociationsVmDiskAssociations from a dict
v_storage_object_associations_vm_disk_associations_form_dict = v_storage_object_associations_vm_disk_associations.from_dict(v_storage_object_associations_vm_disk_associations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


