# HostSystemComplianceCheckState

The host profile compliance check state.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The compliance check operation state.  See *ComplianceResultStatus_enum* for the valid values.  ***Since:*** vSphere API 6.7  | 
**check_time** | **datetime** | The compliance check starting time for running state; compliance check finish time for others.  ***Since:*** vSphere API 6.7  | 

## Example

```python
from vmware_vi.models.host_system_compliance_check_state import HostSystemComplianceCheckState

# TODO update the JSON string below
json = "{}"
# create an instance of HostSystemComplianceCheckState from a JSON string
host_system_compliance_check_state_instance = HostSystemComplianceCheckState.from_json(json)
# print the JSON string representation of the object
print HostSystemComplianceCheckState.to_json()

# convert the object into a dict
host_system_compliance_check_state_dict = host_system_compliance_check_state_instance.to_dict()
# create an instance of HostSystemComplianceCheckState from a dict
host_system_compliance_check_state_form_dict = host_system_compliance_check_state.from_dict(host_system_compliance_check_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


