# DVPortSetting

The *DVPortSetting* data object describes the network configuration of a *DistributedVirtualPort*.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blocked** | [**BoolPolicy**](BoolPolicy.md) |  | [optional] 
**vm_direct_path_gen2_allowed** | [**BoolPolicy**](BoolPolicy.md) |  | [optional] 
**in_shaping_policy** | [**DVSTrafficShapingPolicy**](DVSTrafficShapingPolicy.md) |  | [optional] 
**out_shaping_policy** | [**DVSTrafficShapingPolicy**](DVSTrafficShapingPolicy.md) |  | [optional] 
**vendor_specific_config** | [**DVSVendorSpecificConfig**](DVSVendorSpecificConfig.md) |  | [optional] 
**network_resource_pool_key** | [**StringPolicy**](StringPolicy.md) |  | [optional] 
**filter_policy** | [**DvsFilterPolicy**](DvsFilterPolicy.md) |  | [optional] 

## Example

```python
from vmware_vi.models.dv_port_setting import DVPortSetting

# TODO update the JSON string below
json = "{}"
# create an instance of DVPortSetting from a JSON string
dv_port_setting_instance = DVPortSetting.from_json(json)
# print the JSON string representation of the object
print DVPortSetting.to_json()

# convert the object into a dict
dv_port_setting_dict = dv_port_setting_instance.to_dict()
# create an instance of DVPortSetting from a dict
dv_port_setting_form_dict = dv_port_setting.from_dict(dv_port_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


