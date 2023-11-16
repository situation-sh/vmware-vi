# HostDiskPartitionAttributes

Information about a single disk partition.  A partition is a contiguous set of blocks on a disk that is marked for use. The typeId identifies the purpose of the data in the partition. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partition** | **int** | The partition number.  Must be a positive integer.  | 
**start_sector** | **int** | The start sector.  | 
**end_sector** | **int** | The end sector.  | 
**type** | **str** | Type of data in the partition.  If it is a well-known partition type, it will be one of the defined types. If it is not, then it will be reported as a hexadecimal number. For example, \&quot;none\&quot;, \&quot;vmfs\&quot;, \&quot;linux\&quot;, and \&quot;0x20\&quot; are all valid values.  See also *HostDiskPartitionInfoType_enum*.  | 
**guid** | **str** | Globally Unique Identifier of the partition, as defined by the GUID Partition Table (GPT) format.  This is available only for GPT formatted disks.  ***Since:*** vSphere API 5.0  | [optional] 
**logical** | **bool** | The flag to indicate whether or not the partition is logical.  If true, the partition number should be greater than 4.  | 
**attributes** | **int** | The attributes on the partition.  | 
**partition_alignment** | **int** | Partition alignment in bytes.  If unset, partition alignment value is unknown.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.host_disk_partition_attributes import HostDiskPartitionAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of HostDiskPartitionAttributes from a JSON string
host_disk_partition_attributes_instance = HostDiskPartitionAttributes.from_json(json)
# print the JSON string representation of the object
print HostDiskPartitionAttributes.to_json()

# convert the object into a dict
host_disk_partition_attributes_dict = host_disk_partition_attributes_instance.to_dict()
# create an instance of HostDiskPartitionAttributes from a dict
host_disk_partition_attributes_form_dict = host_disk_partition_attributes.from_dict(host_disk_partition_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


