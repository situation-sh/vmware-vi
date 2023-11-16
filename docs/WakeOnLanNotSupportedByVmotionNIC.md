# WakeOnLanNotSupportedByVmotionNIC

This fault is thrown when Wake-on-LAN isn't supported by the Vmotion NIC on the host.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.wake_on_lan_not_supported_by_vmotion_nic import WakeOnLanNotSupportedByVmotionNIC

# TODO update the JSON string below
json = "{}"
# create an instance of WakeOnLanNotSupportedByVmotionNIC from a JSON string
wake_on_lan_not_supported_by_vmotion_nic_instance = WakeOnLanNotSupportedByVmotionNIC.from_json(json)
# print the JSON string representation of the object
print WakeOnLanNotSupportedByVmotionNIC.to_json()

# convert the object into a dict
wake_on_lan_not_supported_by_vmotion_nic_dict = wake_on_lan_not_supported_by_vmotion_nic_instance.to_dict()
# create an instance of WakeOnLanNotSupportedByVmotionNIC from a dict
wake_on_lan_not_supported_by_vmotion_nic_form_dict = wake_on_lan_not_supported_by_vmotion_nic.from_dict(wake_on_lan_not_supported_by_vmotion_nic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


