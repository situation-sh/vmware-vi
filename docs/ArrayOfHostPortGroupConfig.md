# ArrayOfHostPortGroupConfig

A boxed array of *HostPortGroupConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostPortGroupConfig]**](HostPortGroupConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_port_group_config import ArrayOfHostPortGroupConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostPortGroupConfig from a JSON string
array_of_host_port_group_config_instance = ArrayOfHostPortGroupConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostPortGroupConfig.to_json()

# convert the object into a dict
array_of_host_port_group_config_dict = array_of_host_port_group_config_instance.to_dict()
# create an instance of ArrayOfHostPortGroupConfig from a dict
array_of_host_port_group_config_form_dict = array_of_host_port_group_config.from_dict(array_of_host_port_group_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


