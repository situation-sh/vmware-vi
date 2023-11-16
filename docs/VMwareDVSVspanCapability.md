# VMwareDVSVspanCapability

Indicators of support for version-specific Distributed Port Mirroring sessions.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mixed_dest_supported** | **bool** | Flag to indicate whether mixed dest mirror session is supported on the vSphere Distributed Switch.  ***Since:*** vSphere API 5.1  | 
**dvport_supported** | **bool** | Flag to indicate whether dvport mirror session is supported on the vSphere Distributed Switch.  ***Since:*** vSphere API 5.1  | 
**remote_source_supported** | **bool** | Flag to indicate whether remote mirror source session is supported on the vSphere Distributed Switch.  ***Since:*** vSphere API 5.1  | 
**remote_dest_supported** | **bool** | Flag to indicate whether remote mirror destination session is supported on the vSphere Distributed Switch.  ***Since:*** vSphere API 5.1  | 
**encap_remote_source_supported** | **bool** | Flag to indicate whether encapsulated remote mirror source session is supported on the vSphere Distributed Switch.  ***Since:*** vSphere API 5.1  | 
**erspan_protocol_supported** | **bool** | Flag to indicate whether ERSPAN protocol encapsulation is supported on the vSphere Distributed Switch.  ***Since:*** vSphere API 6.5  | [optional] 
**mirror_netstack_supported** | **bool** | Flag to indicate whether dvport mirror can be configured to use a dedicated network stack instance.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.v_mware_dvs_vspan_capability import VMwareDVSVspanCapability

# TODO update the JSON string below
json = "{}"
# create an instance of VMwareDVSVspanCapability from a JSON string
v_mware_dvs_vspan_capability_instance = VMwareDVSVspanCapability.from_json(json)
# print the JSON string representation of the object
print VMwareDVSVspanCapability.to_json()

# convert the object into a dict
v_mware_dvs_vspan_capability_dict = v_mware_dvs_vspan_capability_instance.to_dict()
# create an instance of VMwareDVSVspanCapability from a dict
v_mware_dvs_vspan_capability_form_dict = v_mware_dvs_vspan_capability.from_dict(v_mware_dvs_vspan_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


