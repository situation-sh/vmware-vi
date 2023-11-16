# VMwareDvsIpfixCapability

The feature capabilities of Ipfix supported by the vSphere Distributed Switch.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipfix_supported** | **bool** | Flag to indicate whether IPFIX(NetFlow) is supported on the vSphere Distributed Switch.  IPFIX is supported in vSphere Distributed Switch Version 5.0 or later.  ***Since:*** vSphere API 6.0  | [optional] 
**ipv6_for_ipfix_supported** | **bool** | Flag to indicate whether IPv6 for IPFIX(NetFlow) is supported on the vSphere Distributed Switch.  IPv6 for IPFIX is supported in vSphere Distributed Switch Version 6.0 or later.  ***Since:*** vSphere API 6.0  | [optional] 
**observation_domain_id_supported** | **bool** | Flag to indicate whether Observation Domain Id for IPFIX is supported on the vSphere Distributed Switch.  Observation Domain Id is supported in vSphere Distributed Switch Version 6.0 or later.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.v_mware_dvs_ipfix_capability import VMwareDvsIpfixCapability

# TODO update the JSON string below
json = "{}"
# create an instance of VMwareDvsIpfixCapability from a JSON string
v_mware_dvs_ipfix_capability_instance = VMwareDvsIpfixCapability.from_json(json)
# print the JSON string representation of the object
print VMwareDvsIpfixCapability.to_json()

# convert the object into a dict
v_mware_dvs_ipfix_capability_dict = v_mware_dvs_ipfix_capability_instance.to_dict()
# create an instance of VMwareDvsIpfixCapability from a dict
v_mware_dvs_ipfix_capability_form_dict = v_mware_dvs_ipfix_capability.from_dict(v_mware_dvs_ipfix_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


