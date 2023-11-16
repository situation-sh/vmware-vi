# VmDiskFileQueryFilter

The filter for the virtual disk primary file. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_type** | **List[str]** | If this optional property is set, only the virtual disk primary files that match one of the specified disk types are selected.  If no disk types are specified, this search criteria is ignored.  The specified disk type is one of the backing information types for a virtual disk.  See also *VirtualDisk*.  | [optional] 
**match_hardware_version** | **List[int]** | If this optional property is set, only virtual disk primary files that match one of the specified hardware versions are selected.  If no versions are specified, this search criteria is ignored.  | [optional] 
**controller_type** | **List[str]** | Deprecated as of vSphere API 5.0, this property is no longer relevant and should not be used. With the current state of emulation, we don&#39;t care about the adapter type a disk is connected to, as disks may be shuffled around. For example, a disk may be unplugged from a buslogic controller and plugged into an lsilogic controller.  If this optional property is set, only virtual disk files that have a controller type that matches one of the controller types specified are returned.  If no controller types are specified, this search criteria is ignored.  The specified controller type is one of the controller types for a virtual disk.  See also *VirtualIDEController*, *VirtualSCSIController*.  ***Since:*** VI API 2.5  | [optional] 
**thin** | **bool** | This optional property can be used to filter disks based on whether they are thin-provsioned or not: if set to true, only thin-provisioned disks are returned, and vice-versa.  ***Since:*** vSphere API 4.0  | [optional] 
**encrypted** | **bool** | This optional property can be used to filter disks based on whether they are encrypted or not.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.vm_disk_file_query_filter import VmDiskFileQueryFilter

# TODO update the JSON string below
json = "{}"
# create an instance of VmDiskFileQueryFilter from a JSON string
vm_disk_file_query_filter_instance = VmDiskFileQueryFilter.from_json(json)
# print the JSON string representation of the object
print VmDiskFileQueryFilter.to_json()

# convert the object into a dict
vm_disk_file_query_filter_dict = vm_disk_file_query_filter_instance.to_dict()
# create an instance of VmDiskFileQueryFilter from a dict
vm_disk_file_query_filter_form_dict = vm_disk_file_query_filter.from_dict(vm_disk_file_query_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


