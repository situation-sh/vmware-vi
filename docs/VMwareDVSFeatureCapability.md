# VMwareDVSFeatureCapability

Indicators of support for version-specific DVS features that are only available on a VMware-class switch.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vspan_supported** | **bool** | Flag to indicate whether vspan(DVMirror) is supported on the vSphere Distributed Switch.  Distributed Port Mirroring is supported in vSphere Distributed Switch Version 5.0 or later.  ***Since:*** vSphere API 5.0  | [optional] 
**lldp_supported** | **bool** | Flag to indicate whether LLDP(Link Layer Discovery Protocol) is supported on the vSphere Distributed Switch.  LLDP is supported in vSphere Distributed Switch Version 5.0 or later.  ***Since:*** vSphere API 5.0  | [optional] 
**ipfix_supported** | **bool** | Deprecated as of vSphere API 6.0, use *VMwareDvsIpfixCapability*.  Flag to indicate whether IPFIX(NetFlow) is supported on the vSphere Distributed Switch.  IPFIX is supported in vSphere Distributed Switch Version 5.0 or later.  ***Since:*** vSphere API 5.0  | [optional] 
**ipfix_capability** | [**VMwareDvsIpfixCapability**](VMwareDvsIpfixCapability.md) |  | [optional] 
**multicast_snooping_supported** | **bool** | Flag to indicate whether multicast snooping(IGMP/MLD Snooping) is supported on the vSphere Distributed Switch.  IGMP/MLD Snooping is supported in vSphere Distributed Switch Version 6.0 or later.  ***Since:*** vSphere API 6.0  | [optional] 
**vspan_capability** | [**VMwareDVSVspanCapability**](VMwareDVSVspanCapability.md) |  | [optional] 
**lacp_capability** | [**VMwareDvsLacpCapability**](VMwareDvsLacpCapability.md) |  | [optional] 
**dpu_capability** | [**VMwareDvsDpuCapability**](VMwareDvsDpuCapability.md) |  | [optional] 
**nsx_supported** | **bool** | Flag to indicate whether NSX is supported on the vSphere Distributed Switch.  NSX is supported in vSphere Distributed Switch Version 7.0 or later.  ***Since:*** vSphere API 7.0  | [optional] 
**mtu_capability** | [**VMwareDvsMtuCapability**](VMwareDvsMtuCapability.md) |  | [optional] 

## Example

```python
from vmware_vi.models.v_mware_dvs_feature_capability import VMwareDVSFeatureCapability

# TODO update the JSON string below
json = "{}"
# create an instance of VMwareDVSFeatureCapability from a JSON string
v_mware_dvs_feature_capability_instance = VMwareDVSFeatureCapability.from_json(json)
# print the JSON string representation of the object
print VMwareDVSFeatureCapability.to_json()

# convert the object into a dict
v_mware_dvs_feature_capability_dict = v_mware_dvs_feature_capability_instance.to_dict()
# create an instance of VMwareDVSFeatureCapability from a dict
v_mware_dvs_feature_capability_form_dict = v_mware_dvs_feature_capability.from_dict(v_mware_dvs_feature_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


