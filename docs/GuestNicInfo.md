# GuestNicInfo

Information about each virtual network adapter configured in the guest operating system. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** | Name of the virtual switch portgroup or dvPort connected to this adapter.  | [optional] 
**ip_address** | **List[str]** | Deprecated as of vSphere API 5.0, use ipConfig property.  IP addresses of the adapter.  | [optional] 
**mac_address** | **str** | MAC address of the adapter.  | [optional] 
**connected** | **bool** | Flag indicating whether or not the virtual device is connected.  | 
**device_config_id** | **int** | Link to the corresponding virtual device.  | 
**dns_config** | [**NetDnsConfigInfo**](NetDnsConfigInfo.md) |  | [optional] 
**ip_config** | [**NetIpConfigInfo**](NetIpConfigInfo.md) |  | [optional] 
**net_bios_config** | [**NetBIOSConfigInfo**](NetBIOSConfigInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.guest_nic_info import GuestNicInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GuestNicInfo from a JSON string
guest_nic_info_instance = GuestNicInfo.from_json(json)
# print the JSON string representation of the object
print GuestNicInfo.to_json()

# convert the object into a dict
guest_nic_info_dict = guest_nic_info_instance.to_dict()
# create an instance of GuestNicInfo from a dict
guest_nic_info_form_dict = guest_nic_info.from_dict(guest_nic_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


