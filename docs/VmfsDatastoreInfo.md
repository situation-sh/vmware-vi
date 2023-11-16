# VmfsDatastoreInfo

Information details about a VMFS datastore. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_physical_rdm_file_size** | **int** | Maximum raw device mapping size (physical compatibility)  ***Since:*** vSphere API 5.1  | 
**max_virtual_rdm_file_size** | **int** | Maximum raw device mapping size (virtual compatibility)  ***Since:*** vSphere API 5.1  | 
**vmfs** | [**HostVmfsVolume**](HostVmfsVolume.md) |  | [optional] 

## Example

```python
from vmware_vi.models.vmfs_datastore_info import VmfsDatastoreInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VmfsDatastoreInfo from a JSON string
vmfs_datastore_info_instance = VmfsDatastoreInfo.from_json(json)
# print the JSON string representation of the object
print VmfsDatastoreInfo.to_json()

# convert the object into a dict
vmfs_datastore_info_dict = vmfs_datastore_info_instance.to_dict()
# create an instance of VmfsDatastoreInfo from a dict
vmfs_datastore_info_form_dict = vmfs_datastore_info.from_dict(vmfs_datastore_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


