# HostDiskMappingInfo

The HostDiskMappingInfo data object type describes a virtual disk mapping to a host disk. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**physical_partition** | [**HostDiskMappingPartitionInfo**](HostDiskMappingPartitionInfo.md) |  | [optional] 
**name** | **str** | Host resource name.  | 
**exclusive** | **bool** | Flag to indicate whether or not the virtual machine has exclusive access to the host device.  | [optional] 

## Example

```python
from vmware_vi.models.host_disk_mapping_info import HostDiskMappingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostDiskMappingInfo from a JSON string
host_disk_mapping_info_instance = HostDiskMappingInfo.from_json(json)
# print the JSON string representation of the object
print HostDiskMappingInfo.to_json()

# convert the object into a dict
host_disk_mapping_info_dict = host_disk_mapping_info_instance.to_dict()
# create an instance of HostDiskMappingInfo from a dict
host_disk_mapping_info_form_dict = host_disk_mapping_info.from_dict(host_disk_mapping_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


