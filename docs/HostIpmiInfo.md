# HostIpmiInfo

The IpmiInfo data object contains IPMI (Intelligent Platform Management Interface) and BMC (Baseboard Management Controller) information for the host.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bmc_ip_address** | **str** | IP address of the BMC on the host.  It should be null terminated.  ***Since:*** vSphere API 4.0  | [optional] 
**bmc_mac_address** | **str** | MAC address of the BMC on the host.  The MAC address should be of the form xx:xx:xx:xx:xx:xx where each x is a hex digit. It should be null terminated.  ***Since:*** vSphere API 4.0  | [optional] 
**login** | **str** | User ID for logging into the BMC.  BMC usernames may be up to 16 characters and must be null terminated. Hence, a login comprises 17 or fewer characters.  ***Since:*** vSphere API 4.0  | [optional] 
**password** | **str** | Password for logging into the BMC.  Only used for configuration, returned as unset while reading. The password can be up to 16 characters and must be null terminated. Hence, a password comprises 17 or fewer characters.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.host_ipmi_info import HostIpmiInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostIpmiInfo from a JSON string
host_ipmi_info_instance = HostIpmiInfo.from_json(json)
# print the JSON string representation of the object
print HostIpmiInfo.to_json()

# convert the object into a dict
host_ipmi_info_dict = host_ipmi_info_instance.to_dict()
# create an instance of HostIpmiInfo from a dict
host_ipmi_info_form_dict = host_ipmi_info.from_dict(host_ipmi_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


