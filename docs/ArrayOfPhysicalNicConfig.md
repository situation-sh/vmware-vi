# ArrayOfPhysicalNicConfig

A boxed array of *PhysicalNicConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PhysicalNicConfig]**](PhysicalNicConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_physical_nic_config import ArrayOfPhysicalNicConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPhysicalNicConfig from a JSON string
array_of_physical_nic_config_instance = ArrayOfPhysicalNicConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfPhysicalNicConfig.to_json()

# convert the object into a dict
array_of_physical_nic_config_dict = array_of_physical_nic_config_instance.to_dict()
# create an instance of ArrayOfPhysicalNicConfig from a dict
array_of_physical_nic_config_form_dict = array_of_physical_nic_config.from_dict(array_of_physical_nic_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


