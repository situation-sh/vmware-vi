# HostDiagnosticPartitionCreateOption

This data object describes a disk that can be used to create a diagnostic partition. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_type** | **str** | Indicates the storage type of diagnostic partition to be created.  See also *DiagnosticPartitionStorageType_enum*.  | 
**diagnostic_type** | **str** | Indicates the type of the diagnostic partition to be created.  See also *DiagnosticPartitionType_enum*.  | 
**disk** | [**HostScsiDisk**](HostScsiDisk.md) |  | 

## Example

```python
from vmware_vi.models.host_diagnostic_partition_create_option import HostDiagnosticPartitionCreateOption

# TODO update the JSON string below
json = "{}"
# create an instance of HostDiagnosticPartitionCreateOption from a JSON string
host_diagnostic_partition_create_option_instance = HostDiagnosticPartitionCreateOption.from_json(json)
# print the JSON string representation of the object
print HostDiagnosticPartitionCreateOption.to_json()

# convert the object into a dict
host_diagnostic_partition_create_option_dict = host_diagnostic_partition_create_option_instance.to_dict()
# create an instance of HostDiagnosticPartitionCreateOption from a dict
host_diagnostic_partition_create_option_form_dict = host_diagnostic_partition_create_option.from_dict(host_diagnostic_partition_create_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


