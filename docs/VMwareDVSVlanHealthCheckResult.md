# VMwareDVSVlanHealthCheckResult

This class defines Vlan health check result of an uplink port in the VMware vSphered Distributed Switch.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trunked_vlan** | [**List[NumericRange]**](NumericRange.md) | The vlans which are trunked by the physical switch connected to the uplink port.  If the vlan is not a range, but a single Id, both start and end have the same value with the single vlan Id.  ***Since:*** vSphere API 5.1  | [optional] 
**untrunked_vlan** | [**List[NumericRange]**](NumericRange.md) | The vlans which are not trunked by the physical switch connected to the uplink port.  If the vlan is not a range, but a single Id, both start and end have the same value with the single vlan Id.  ***Since:*** vSphere API 5.1  | [optional] 

## Example

```python
from vmware_vi.models.v_mware_dvs_vlan_health_check_result import VMwareDVSVlanHealthCheckResult

# TODO update the JSON string below
json = "{}"
# create an instance of VMwareDVSVlanHealthCheckResult from a JSON string
v_mware_dvs_vlan_health_check_result_instance = VMwareDVSVlanHealthCheckResult.from_json(json)
# print the JSON string representation of the object
print VMwareDVSVlanHealthCheckResult.to_json()

# convert the object into a dict
v_mware_dvs_vlan_health_check_result_dict = v_mware_dvs_vlan_health_check_result_instance.to_dict()
# create an instance of VMwareDVSVlanHealthCheckResult from a dict
v_mware_dvs_vlan_health_check_result_form_dict = v_mware_dvs_vlan_health_check_result.from_dict(v_mware_dvs_vlan_health_check_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


