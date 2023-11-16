# PhysicalNicSpec

This data object type describes the physical network adapter specification representing the properties on a physical network adapter that can be configured once the object exists. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | [**HostIpConfig**](HostIpConfig.md) |  | [optional] 
**link_speed** | [**PhysicalNicLinkInfo**](PhysicalNicLinkInfo.md) |  | [optional] 
**enable_enhanced_networking_stack** | **bool** | If set the flag indicates if the physical network adapter is configured for Enhanced Networking Stack  ***Since:*** vSphere API 6.7  | [optional] 
**ens_interrupt_enabled** | **bool** | If set the flag indicates if the physical network adapter is configured for Enhanced Networking Stack interrupt mode  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.physical_nic_spec import PhysicalNicSpec

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalNicSpec from a JSON string
physical_nic_spec_instance = PhysicalNicSpec.from_json(json)
# print the JSON string representation of the object
print PhysicalNicSpec.to_json()

# convert the object into a dict
physical_nic_spec_dict = physical_nic_spec_instance.to_dict()
# create an instance of PhysicalNicSpec from a dict
physical_nic_spec_form_dict = physical_nic_spec.from_dict(physical_nic_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


