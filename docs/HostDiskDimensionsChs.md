# HostDiskDimensionsChs

This data object type describes dimensions using the cylinder, head, sector (CHS) coordinate system.  This coordinate system is generally needed for partitioning for legacy reasons. When defining partitions, many partitioning utilities do not function correctly when certain CHS constraints are not met. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cylinder** | **int** | The number of cylinders.  | 
**head** | **int** | The number of heads per cylinders.  | 
**sector** | **int** | The number of sectors per head.  | 

## Example

```python
from vmware_vi.models.host_disk_dimensions_chs import HostDiskDimensionsChs

# TODO update the JSON string below
json = "{}"
# create an instance of HostDiskDimensionsChs from a JSON string
host_disk_dimensions_chs_instance = HostDiskDimensionsChs.from_json(json)
# print the JSON string representation of the object
print HostDiskDimensionsChs.to_json()

# convert the object into a dict
host_disk_dimensions_chs_dict = host_disk_dimensions_chs_instance.to_dict()
# create an instance of HostDiskDimensionsChs from a dict
host_disk_dimensions_chs_form_dict = host_disk_dimensions_chs.from_dict(host_disk_dimensions_chs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


