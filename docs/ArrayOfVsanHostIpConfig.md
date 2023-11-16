# ArrayOfVsanHostIpConfig

A boxed array of *VsanHostIpConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VsanHostIpConfig]**](VsanHostIpConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vsan_host_ip_config import ArrayOfVsanHostIpConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVsanHostIpConfig from a JSON string
array_of_vsan_host_ip_config_instance = ArrayOfVsanHostIpConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfVsanHostIpConfig.to_json()

# convert the object into a dict
array_of_vsan_host_ip_config_dict = array_of_vsan_host_ip_config_instance.to_dict()
# create an instance of ArrayOfVsanHostIpConfig from a dict
array_of_vsan_host_ip_config_form_dict = array_of_vsan_host_ip_config.from_dict(array_of_vsan_host_ip_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


