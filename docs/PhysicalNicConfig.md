# PhysicalNicConfig

The configuration of the physical network adapter containing both the configurable properties and identification information. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | PhysicalNic device to which configuration applies.  | 
**spec** | [**PhysicalNicSpec**](PhysicalNicSpec.md) |  | 

## Example

```python
from vmware_vi.models.physical_nic_config import PhysicalNicConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalNicConfig from a JSON string
physical_nic_config_instance = PhysicalNicConfig.from_json(json)
# print the JSON string representation of the object
print PhysicalNicConfig.to_json()

# convert the object into a dict
physical_nic_config_dict = physical_nic_config_instance.to_dict()
# create an instance of PhysicalNicConfig from a dict
physical_nic_config_form_dict = physical_nic_config.from_dict(physical_nic_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


