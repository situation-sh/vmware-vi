# HostDiskMappingOption

The HostDiskMappingOption data object type describes the options for a virtual disk mapping to a host disk. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**physical_partition** | [**List[HostDiskMappingPartitionOption]**](HostDiskMappingPartitionOption.md) | Array of valid partitions on this physical disk.  There is no default for this array.  | [optional] 
**name** | **str** | Host resource name.  | 

## Example

```python
from vmware_vi.models.host_disk_mapping_option import HostDiskMappingOption

# TODO update the JSON string below
json = "{}"
# create an instance of HostDiskMappingOption from a JSON string
host_disk_mapping_option_instance = HostDiskMappingOption.from_json(json)
# print the JSON string representation of the object
print HostDiskMappingOption.to_json()

# convert the object into a dict
host_disk_mapping_option_dict = host_disk_mapping_option_instance.to_dict()
# create an instance of HostDiskMappingOption from a dict
host_disk_mapping_option_form_dict = host_disk_mapping_option.from_dict(host_disk_mapping_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


