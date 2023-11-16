# VMwareDVSHealthCheckCapability

The feature capabilities of health check supported by the vSphere Distributed Switch  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vlan_mtu_supported** | **bool** | Flag to indicate whether vlan/mtu health check is supported on the vSphere Distributed Switch.  ***Since:*** vSphere API 5.1  | 
**teaming_supported** | **bool** | Flag to indicate whether teaming health check is supported on the vSphere Distributed Switch.  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.v_mware_dvs_health_check_capability import VMwareDVSHealthCheckCapability

# TODO update the JSON string below
json = "{}"
# create an instance of VMwareDVSHealthCheckCapability from a JSON string
v_mware_dvs_health_check_capability_instance = VMwareDVSHealthCheckCapability.from_json(json)
# print the JSON string representation of the object
print VMwareDVSHealthCheckCapability.to_json()

# convert the object into a dict
v_mware_dvs_health_check_capability_dict = v_mware_dvs_health_check_capability_instance.to_dict()
# create an instance of VMwareDVSHealthCheckCapability from a dict
v_mware_dvs_health_check_capability_form_dict = v_mware_dvs_health_check_capability.from_dict(v_mware_dvs_health_check_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


