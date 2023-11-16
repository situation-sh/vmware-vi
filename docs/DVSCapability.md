# DVSCapability

The *DVSCapability* data object describes the distributed virtual switch features and indicates the level of configuration that is allowed.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dvs_operation_supported** | **bool** | Indicates whether this switch allows vCenter users to modify the switch configuration at the switch level, except for host member, policy, and scope operations.  ***Since:*** vSphere API 4.0  | [optional] 
**dv_port_group_operation_supported** | **bool** | Indicates whether this switch allows vCenter users to modify the switch configuration at the portgroup level, except for host member, policy, and scope operations.  ***Since:*** vSphere API 4.0  | [optional] 
**dv_port_operation_supported** | **bool** | Indicates whether this switch allows vCenter users to modify the switch configuration at the port level, except for host member, policy, and scope operations.  ***Since:*** vSphere API 4.0  | [optional] 
**compatible_host_component_product_info** | [**List[DistributedVirtualSwitchHostProductSpec]**](DistributedVirtualSwitchHostProductSpec.md) | List of host component product information that is compatible with the current switch implementation.  ***Since:*** vSphere API 4.0  | [optional] 
**features_supported** | [**DVSFeatureCapability**](DVSFeatureCapability.md) |  | [optional] 

## Example

```python
from vmware_vi.models.dvs_capability import DVSCapability

# TODO update the JSON string below
json = "{}"
# create an instance of DVSCapability from a JSON string
dvs_capability_instance = DVSCapability.from_json(json)
# print the JSON string representation of the object
print DVSCapability.to_json()

# convert the object into a dict
dvs_capability_dict = dvs_capability_instance.to_dict()
# create an instance of DVSCapability from a dict
dvs_capability_form_dict = dvs_capability.from_dict(dvs_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


