# FcoeConfig

This data object type describes an FCoE configuration as it pertains to an underlying physical NIC.  Terminology is borrowed from T11's working draft of the Fibre Channel Backbone 5 standard (FC-BB-5). The draft can be found at http://www.t11.org.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority_class** | **int** | 802.1p priority class used for FCoE traffic.  ***Since:*** vSphere API 5.0  | 
**source_mac** | **str** | Source MAC address used for FCoE traffic.  This MAC address is associated with the logical construct that is a physical NIC&#39;s associated underlying FCoE Controller, as defined in the FC-BB-5 standard. This MAC address should be of the form \&quot;xx:xx:xx:xx:xx:xx\&quot;, where &#39;x&#39; is a hexadecimal digit. Valid MAC addresses are unicast addresses.  ***Since:*** vSphere API 5.0  | 
**vlan_range** | [**List[FcoeConfigVlanRange]**](FcoeConfigVlanRange.md) | VLAN ranges associated with this FcoeConfig.  ***Since:*** vSphere API 5.0  | 
**capabilities** | [**FcoeConfigFcoeCapabilities**](FcoeConfigFcoeCapabilities.md) |  | 
**fcoe_active** | **bool** | Indicates whether this FcoeConfig is \&quot;active\&quot; (has been used in conjunction with a parent physical network adapter for FCoE discovery).  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.fcoe_config import FcoeConfig

# TODO update the JSON string below
json = "{}"
# create an instance of FcoeConfig from a JSON string
fcoe_config_instance = FcoeConfig.from_json(json)
# print the JSON string representation of the object
print FcoeConfig.to_json()

# convert the object into a dict
fcoe_config_dict = fcoe_config_instance.to_dict()
# create an instance of FcoeConfig from a dict
fcoe_config_form_dict = fcoe_config.from_dict(fcoe_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


