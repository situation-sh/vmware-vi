# ArrayOfHostDiagnosticPartitionCreateDescription

A boxed array of *HostDiagnosticPartitionCreateDescription*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostDiagnosticPartitionCreateDescription]**](HostDiagnosticPartitionCreateDescription.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_diagnostic_partition_create_description import ArrayOfHostDiagnosticPartitionCreateDescription

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostDiagnosticPartitionCreateDescription from a JSON string
array_of_host_diagnostic_partition_create_description_instance = ArrayOfHostDiagnosticPartitionCreateDescription.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostDiagnosticPartitionCreateDescription.to_json()

# convert the object into a dict
array_of_host_diagnostic_partition_create_description_dict = array_of_host_diagnostic_partition_create_description_instance.to_dict()
# create an instance of ArrayOfHostDiagnosticPartitionCreateDescription from a dict
array_of_host_diagnostic_partition_create_description_form_dict = array_of_host_diagnostic_partition_create_description.from_dict(array_of_host_diagnostic_partition_create_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


