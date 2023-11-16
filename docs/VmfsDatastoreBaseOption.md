# VmfsDatastoreBaseOption

Base class that describes a VMFS datastore provisioning option. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**layout** | [**HostDiskPartitionLayout**](HostDiskPartitionLayout.md) |  | 
**partition_format_change** | **bool** | Indicates whether selecting this option will change the partition format type on the disk.  See also *HostDiskPartitionInfoPartitionFormat_enum*.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.vmfs_datastore_base_option import VmfsDatastoreBaseOption

# TODO update the JSON string below
json = "{}"
# create an instance of VmfsDatastoreBaseOption from a JSON string
vmfs_datastore_base_option_instance = VmfsDatastoreBaseOption.from_json(json)
# print the JSON string representation of the object
print VmfsDatastoreBaseOption.to_json()

# convert the object into a dict
vmfs_datastore_base_option_dict = vmfs_datastore_base_option_instance.to_dict()
# create an instance of VmfsDatastoreBaseOption from a dict
vmfs_datastore_base_option_form_dict = vmfs_datastore_base_option.from_dict(vmfs_datastore_base_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


