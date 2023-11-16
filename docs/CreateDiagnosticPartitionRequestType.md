# CreateDiagnosticPartitionRequestType

The parameters of *HostDiagnosticSystem.CreateDiagnosticPartition*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**HostDiagnosticPartitionCreateSpec**](HostDiagnosticPartitionCreateSpec.md) |  | 

## Example

```python
from vmware_vi.models.create_diagnostic_partition_request_type import CreateDiagnosticPartitionRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDiagnosticPartitionRequestType from a JSON string
create_diagnostic_partition_request_type_instance = CreateDiagnosticPartitionRequestType.from_json(json)
# print the JSON string representation of the object
print CreateDiagnosticPartitionRequestType.to_json()

# convert the object into a dict
create_diagnostic_partition_request_type_dict = create_diagnostic_partition_request_type_instance.to_dict()
# create an instance of CreateDiagnosticPartitionRequestType from a dict
create_diagnostic_partition_request_type_form_dict = create_diagnostic_partition_request_type.from_dict(create_diagnostic_partition_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


