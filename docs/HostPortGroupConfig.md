# HostPortGroupConfig

This describes the port group configuration containing both the configurable properties on a port group and the associated virtual switch. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_operation** | **str** | Indicates the change operation to apply on this configuration specification.  See also *HostConfigChangeOperation_enum*.  | [optional] 
**spec** | [**HostPortGroupSpec**](HostPortGroupSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_port_group_config import HostPortGroupConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HostPortGroupConfig from a JSON string
host_port_group_config_instance = HostPortGroupConfig.from_json(json)
# print the JSON string representation of the object
print HostPortGroupConfig.to_json()

# convert the object into a dict
host_port_group_config_dict = host_port_group_config_instance.to_dict()
# create an instance of HostPortGroupConfig from a dict
host_port_group_config_form_dict = host_port_group_config.from_dict(host_port_group_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


