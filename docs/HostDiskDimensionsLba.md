# HostDiskDimensionsLba

This data object type describes the logical block addressing system that uses block numbers and block sizes to refer to a block.  This scheme is employed by SCSI. If a SCSI disk is not involved, then blockSize is 512 bytes. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_size** | **int** | The size of the blocks.  | 
**block** | **int** | The number of blocks.  | 

## Example

```python
from vmware_vi.models.host_disk_dimensions_lba import HostDiskDimensionsLba

# TODO update the JSON string below
json = "{}"
# create an instance of HostDiskDimensionsLba from a JSON string
host_disk_dimensions_lba_instance = HostDiskDimensionsLba.from_json(json)
# print the JSON string representation of the object
print HostDiskDimensionsLba.to_json()

# convert the object into a dict
host_disk_dimensions_lba_dict = host_disk_dimensions_lba_instance.to_dict()
# create an instance of HostDiskDimensionsLba from a dict
host_disk_dimensions_lba_form_dict = host_disk_dimensions_lba.from_dict(host_disk_dimensions_lba_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


