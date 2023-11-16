# ArrayOfHostPowerOperationType

A boxed array of *HostPowerOperationType_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostPowerOperationTypeEnum]**](HostPowerOperationTypeEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_power_operation_type import ArrayOfHostPowerOperationType

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostPowerOperationType from a JSON string
array_of_host_power_operation_type_instance = ArrayOfHostPowerOperationType.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostPowerOperationType.to_json()

# convert the object into a dict
array_of_host_power_operation_type_dict = array_of_host_power_operation_type_instance.to_dict()
# create an instance of ArrayOfHostPowerOperationType from a dict
array_of_host_power_operation_type_form_dict = array_of_host_power_operation_type.from_dict(array_of_host_power_operation_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


