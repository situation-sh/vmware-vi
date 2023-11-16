# HostNatServiceConfig

This data object type describes the network address translation (NAT) service configuration representing both the configured properties on a NAT Service and identification information.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_operation** | **str** | Indicates the change operation to apply on this configuration specification.  See also *HostConfigChangeOperation_enum*.  ***Since:*** VI API 2.5  | [optional] 
**key** | **str** | The instance ID of the NAT service.  ***Since:*** VI API 2.5  | 
**spec** | [**HostNatServiceSpec**](HostNatServiceSpec.md) |  | 

## Example

```python
from vmware_vi.models.host_nat_service_config import HostNatServiceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HostNatServiceConfig from a JSON string
host_nat_service_config_instance = HostNatServiceConfig.from_json(json)
# print the JSON string representation of the object
print HostNatServiceConfig.to_json()

# convert the object into a dict
host_nat_service_config_dict = host_nat_service_config_instance.to_dict()
# create an instance of HostNatServiceConfig from a dict
host_nat_service_config_form_dict = host_nat_service_config.from_dict(host_nat_service_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


