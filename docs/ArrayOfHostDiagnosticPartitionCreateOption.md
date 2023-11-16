# ArrayOfHostDiagnosticPartitionCreateOption

A boxed array of *HostDiagnosticPartitionCreateOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostDiagnosticPartitionCreateOption]**](HostDiagnosticPartitionCreateOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_diagnostic_partition_create_option import ArrayOfHostDiagnosticPartitionCreateOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostDiagnosticPartitionCreateOption from a JSON string
array_of_host_diagnostic_partition_create_option_instance = ArrayOfHostDiagnosticPartitionCreateOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostDiagnosticPartitionCreateOption.to_json()

# convert the object into a dict
array_of_host_diagnostic_partition_create_option_dict = array_of_host_diagnostic_partition_create_option_instance.to_dict()
# create an instance of ArrayOfHostDiagnosticPartitionCreateOption from a dict
array_of_host_diagnostic_partition_create_option_form_dict = array_of_host_diagnostic_partition_create_option.from_dict(array_of_host_diagnostic_partition_create_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


