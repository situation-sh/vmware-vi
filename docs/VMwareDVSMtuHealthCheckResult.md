# VMwareDVSMtuHealthCheckResult

This class defines MTU health check result of an uplink port in the VMware vSphered Distributed Switch.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mtu_mismatch** | **bool** | True if the MTU configured in the vSphere Distributed Switch is different from the value configured in the Physical NIC, else false.  If it is true, MTU health check is stopped. In this case, *VMwareDVSMtuHealthCheckResult.vlanSupportSwitchMtu* and *VMwareDVSMtuHealthCheckResult.vlanNotSupportSwitchMtu* will not have values.  ***Since:*** vSphere API 5.1  | 
**vlan_support_switch_mtu** | [**List[NumericRange]**](NumericRange.md) | The vlan&#39;s MTU setting on physical switch allows vSphere Distributed Switch max MTU size packets passing.  If the vlan is not a range, but a single Id, both start and end have the same value with the single vlan Id.  ***Since:*** vSphere API 5.1  | [optional] 
**vlan_not_support_switch_mtu** | [**List[NumericRange]**](NumericRange.md) | The vlan&#39;s MTU setting on physical switch does not allow vSphere Distributed Switch max MTU size packets passing.  If the vlan is not a range, but a single Id, both start and end have the same value with the single vlan Id.  ***Since:*** vSphere API 5.1  | [optional] 

## Example

```python
from vmware_vi.models.v_mware_dvs_mtu_health_check_result import VMwareDVSMtuHealthCheckResult

# TODO update the JSON string below
json = "{}"
# create an instance of VMwareDVSMtuHealthCheckResult from a JSON string
v_mware_dvs_mtu_health_check_result_instance = VMwareDVSMtuHealthCheckResult.from_json(json)
# print the JSON string representation of the object
print VMwareDVSMtuHealthCheckResult.to_json()

# convert the object into a dict
v_mware_dvs_mtu_health_check_result_dict = v_mware_dvs_mtu_health_check_result_instance.to_dict()
# create an instance of VMwareDVSMtuHealthCheckResult from a dict
v_mware_dvs_mtu_health_check_result_form_dict = v_mware_dvs_mtu_health_check_result.from_dict(v_mware_dvs_mtu_health_check_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


