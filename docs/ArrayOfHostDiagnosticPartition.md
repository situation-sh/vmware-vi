# ArrayOfHostDiagnosticPartition

A boxed array of *HostDiagnosticPartition*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostDiagnosticPartition]**](HostDiagnosticPartition.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_diagnostic_partition import ArrayOfHostDiagnosticPartition

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostDiagnosticPartition from a JSON string
array_of_host_diagnostic_partition_instance = ArrayOfHostDiagnosticPartition.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostDiagnosticPartition.to_json()

# convert the object into a dict
array_of_host_diagnostic_partition_dict = array_of_host_diagnostic_partition_instance.to_dict()
# create an instance of ArrayOfHostDiagnosticPartition from a dict
array_of_host_diagnostic_partition_form_dict = array_of_host_diagnostic_partition.from_dict(array_of_host_diagnostic_partition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


