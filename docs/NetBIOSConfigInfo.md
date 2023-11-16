# NetBIOSConfigInfo

This data object type describes the NetBIOS configuration of an operating system.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | NetBIOS configuration mode.  The supported values are described by *NetBIOSConfigInfoMode_enum*.  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.net_bios_config_info import NetBIOSConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NetBIOSConfigInfo from a JSON string
net_bios_config_info_instance = NetBIOSConfigInfo.from_json(json)
# print the JSON string representation of the object
print NetBIOSConfigInfo.to_json()

# convert the object into a dict
net_bios_config_info_dict = net_bios_config_info_instance.to_dict()
# create an instance of NetBIOSConfigInfo from a dict
net_bios_config_info_form_dict = net_bios_config_info.from_dict(net_bios_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


