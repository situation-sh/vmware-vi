# VsanHostIpConfig

An *VsanHostIpConfig* is a pair of multicast IP addresses for use by the VSAN service.  For VSAN there is one such IpConfig pair per \"virtual network\" as represented by *VsanHostConfigInfoNetworkInfoPortConfig*.  See also *VsanHostConfigInfoNetworkInfo*, *VsanHostConfigInfoNetworkInfo.port*, *VsanHostConfigInfoNetworkInfoPortConfig*, *HostVsanSystem.UpdateVsan_Task*.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upstream_ip_address** | **str** | Agent-to-master multicast IP address.  ***Since:*** vSphere API 5.5  | 
**downstream_ip_address** | **str** | Master-to-agent multicast IP address.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.vsan_host_ip_config import VsanHostIpConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VsanHostIpConfig from a JSON string
vsan_host_ip_config_instance = VsanHostIpConfig.from_json(json)
# print the JSON string representation of the object
print VsanHostIpConfig.to_json()

# convert the object into a dict
vsan_host_ip_config_dict = vsan_host_ip_config_instance.to_dict()
# create an instance of VsanHostIpConfig from a dict
vsan_host_ip_config_form_dict = vsan_host_ip_config.from_dict(vsan_host_ip_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


