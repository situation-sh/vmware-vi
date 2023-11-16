# VStorageObjectAssociations

This data object is a key-value pair whose key is the virtual storage object id, and value is the vm association information.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**vm_disk_associations** | [**List[VStorageObjectAssociationsVmDiskAssociations]**](VStorageObjectAssociationsVmDiskAssociations.md) | Array of vm associations related to the virtual storage object.  ***Since:*** vSphere API 6.7  | [optional] 
**fault** | [**MethodFault**](MethodFault.md) |  | [optional] 

## Example

```python
from vmware_vi.models.v_storage_object_associations import VStorageObjectAssociations

# TODO update the JSON string below
json = "{}"
# create an instance of VStorageObjectAssociations from a JSON string
v_storage_object_associations_instance = VStorageObjectAssociations.from_json(json)
# print the JSON string representation of the object
print VStorageObjectAssociations.to_json()

# convert the object into a dict
v_storage_object_associations_dict = v_storage_object_associations_instance.to_dict()
# create an instance of VStorageObjectAssociations from a dict
v_storage_object_associations_form_dict = v_storage_object_associations.from_dict(v_storage_object_associations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


