# HostDiagnosticPartition

This data object type contains information about an available or active diagnostic partition. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_type** | **str** | Indicates the storage type of the diagnostic partition.  See also *DiagnosticPartitionStorageType_enum*.  | 
**diagnostic_type** | **str** | Indicates the type of the diagnostic partition.  See also *DiagnosticPartitionType_enum*.  | 
**slots** | **int** | The number of slots in the diagnostic partition.  | 
**id** | [**HostScsiDiskPartition**](HostScsiDiskPartition.md) |  | 

## Example

```python
from vmware_vi.models.host_diagnostic_partition import HostDiagnosticPartition

# TODO update the JSON string below
json = "{}"
# create an instance of HostDiagnosticPartition from a JSON string
host_diagnostic_partition_instance = HostDiagnosticPartition.from_json(json)
# print the JSON string representation of the object
print HostDiagnosticPartition.to_json()

# convert the object into a dict
host_diagnostic_partition_dict = host_diagnostic_partition_instance.to_dict()
# create an instance of HostDiagnosticPartition from a dict
host_diagnostic_partition_form_dict = host_diagnostic_partition.from_dict(host_diagnostic_partition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


