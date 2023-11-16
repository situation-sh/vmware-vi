# HostDiagnosticPartitionCreateDescription

The diagnostic partition create description details what will be done to create a new diagnostic partition on a disk.  It contains a CreateSpec that can be submitted to create the partition and information that can be shown to the user. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**layout** | [**HostDiskPartitionLayout**](HostDiskPartitionLayout.md) |  | 
**disk_uuid** | **str** | The UUID of the SCSI disk on which to create the diagnostic partition.  This disk UUID will match that found in the identification field of the creation spec.  See also *HostScsiDisk*, *ScsiLun.uuid*.  | 
**spec** | [**HostDiagnosticPartitionCreateSpec**](HostDiagnosticPartitionCreateSpec.md) |  | 

## Example

```python
from vmware_vi.models.host_diagnostic_partition_create_description import HostDiagnosticPartitionCreateDescription

# TODO update the JSON string below
json = "{}"
# create an instance of HostDiagnosticPartitionCreateDescription from a JSON string
host_diagnostic_partition_create_description_instance = HostDiagnosticPartitionCreateDescription.from_json(json)
# print the JSON string representation of the object
print HostDiagnosticPartitionCreateDescription.to_json()

# convert the object into a dict
host_diagnostic_partition_create_description_dict = host_diagnostic_partition_create_description_instance.to_dict()
# create an instance of HostDiagnosticPartitionCreateDescription from a dict
host_diagnostic_partition_create_description_form_dict = host_diagnostic_partition_create_description.from_dict(host_diagnostic_partition_create_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


