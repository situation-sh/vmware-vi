# VmfsDatastoreOption

VMFS datastore provisioning option that can be applied on a disk.  VMFS datastores can be created or have their capacity increased using storage from a disk. There are often multiple ways in which extents can be allocated on a disk. Each instance of this structure represents one of the possible options that can be applied to provisiong VMFS datastore storage. Only options that follow ESX Server best practice guidelines will be presented. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | [**VmfsDatastoreBaseOption**](VmfsDatastoreBaseOption.md) |  | 
**spec** | [**VmfsDatastoreSpec**](VmfsDatastoreSpec.md) |  | 

## Example

```python
from vmware_vi.models.vmfs_datastore_option import VmfsDatastoreOption

# TODO update the JSON string below
json = "{}"
# create an instance of VmfsDatastoreOption from a JSON string
vmfs_datastore_option_instance = VmfsDatastoreOption.from_json(json)
# print the JSON string representation of the object
print VmfsDatastoreOption.to_json()

# convert the object into a dict
vmfs_datastore_option_dict = vmfs_datastore_option_instance.to_dict()
# create an instance of VmfsDatastoreOption from a dict
vmfs_datastore_option_form_dict = vmfs_datastore_option.from_dict(vmfs_datastore_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


