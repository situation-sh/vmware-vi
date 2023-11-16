# WinNetBIOSConfigInfo

This data object type describes the Windows-specific NetBIOS configuration.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_wins** | **str** | The IP address of the primary WINS server.  ***Since:*** vSphere API 4.1  | 
**secondary_wins** | **str** | The IP address of the secondary WINS server.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.win_net_bios_config_info import WinNetBIOSConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WinNetBIOSConfigInfo from a JSON string
win_net_bios_config_info_instance = WinNetBIOSConfigInfo.from_json(json)
# print the JSON string representation of the object
print WinNetBIOSConfigInfo.to_json()

# convert the object into a dict
win_net_bios_config_info_dict = win_net_bios_config_info_instance.to_dict()
# create an instance of WinNetBIOSConfigInfo from a dict
win_net_bios_config_info_form_dict = win_net_bios_config_info.from_dict(win_net_bios_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


