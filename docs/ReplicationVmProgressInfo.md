# ReplicationVmProgressInfo

A set of statistics related to the progress of the current operation (full sync or lwd).  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**progress** | **int** | An estimation of the operation progress as a percentage completed, from 0 to 100.  ***Since:*** vSphere API 5.0  | 
**bytes_transferred** | **int** | Number of bytes transferred so far.  For sync operations, this value includes (i.e. counts multiple times) areas that were transferred multiple times (due to stopping and continuing the operation, or for some errors).  ***Since:*** vSphere API 5.0  | 
**bytes_to_transfer** | **int** | The total number of bytes to be transferred.  For lwd operations, this is the total size of the disk images that are transferring. This is known from the start and will not change during a lwd operation.  For sync operations, this is the total size of the blocks that have been found not to match between the primary and secondary (by comparing checksums). It starts from 0 and grows as the checksum operations advance. The value includes (i.e. counts multiple times) areas that will end up being transferred more than once (due to stopping and continuing the operation, or for some errors).  ***Since:*** vSphere API 5.0  | 
**checksum_total_bytes** | **int** | The total number of bytes to be checksummed, only present for sync tasks.  This is the total size of all disks.  ***Since:*** vSphere API 5.0  | [optional] 
**checksum_compared_bytes** | **int** | The total number of bytes that were checksummed, only present for sync tasks.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.replication_vm_progress_info import ReplicationVmProgressInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationVmProgressInfo from a JSON string
replication_vm_progress_info_instance = ReplicationVmProgressInfo.from_json(json)
# print the JSON string representation of the object
print ReplicationVmProgressInfo.to_json()

# convert the object into a dict
replication_vm_progress_info_dict = replication_vm_progress_info_instance.to_dict()
# create an instance of ReplicationVmProgressInfo from a dict
replication_vm_progress_info_form_dict = replication_vm_progress_info.from_dict(replication_vm_progress_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


