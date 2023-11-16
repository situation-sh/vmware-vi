# HostPowerOperationType

A boxed *HostPowerOperationType_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**HostPowerOperationTypeEnum**](HostPowerOperationTypeEnum.md) |  | 

## Example

```python
from vmware_vi.models.host_power_operation_type import HostPowerOperationType

# TODO update the JSON string below
json = "{}"
# create an instance of HostPowerOperationType from a JSON string
host_power_operation_type_instance = HostPowerOperationType.from_json(json)
# print the JSON string representation of the object
print HostPowerOperationType.to_json()

# convert the object into a dict
host_power_operation_type_dict = host_power_operation_type_instance.to_dict()
# create an instance of HostPowerOperationType from a dict
host_power_operation_type_form_dict = host_power_operation_type.from_dict(host_power_operation_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


