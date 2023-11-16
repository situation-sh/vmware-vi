# FcoeConfigFcoeSpecification

An FcoeSpecification contains values relevant to issuing FCoE discovery.  Non-mandatory values are denoted '@optional'.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**underlying_pnic** | **str** | The name of this FcoeSpecification&#39;s underlying PhysicalNic  ***Since:*** vSphere API 5.0  | 
**priority_class** | **int** | 802.1p priority class to use for FCoE traffic.  ***Since:*** vSphere API 5.0  | [optional] 
**source_mac** | **str** | Source MAC address to use for FCoE traffic.  This MAC address is associated with the logical construct that is a physical NIC&#39;s associated underlying FCoE Controller, as defined in the FC-BB-5 standard. This MAC address should be of the form \&quot;xx:xx:xx:xx:xx:xx\&quot;, where &#39;x&#39; is a hexadecimal digit. Valid MAC addresses are unicast addresses.  ***Since:*** vSphere API 5.0  | [optional] 
**vlan_range** | [**List[FcoeConfigVlanRange]**](FcoeConfigVlanRange.md) | VLAN ranges to use for FCoE traffic.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.fcoe_config_fcoe_specification import FcoeConfigFcoeSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of FcoeConfigFcoeSpecification from a JSON string
fcoe_config_fcoe_specification_instance = FcoeConfigFcoeSpecification.from_json(json)
# print the JSON string representation of the object
print FcoeConfigFcoeSpecification.to_json()

# convert the object into a dict
fcoe_config_fcoe_specification_dict = fcoe_config_fcoe_specification_instance.to_dict()
# create an instance of FcoeConfigFcoeSpecification from a dict
fcoe_config_fcoe_specification_form_dict = fcoe_config_fcoe_specification.from_dict(fcoe_config_fcoe_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


