# HostSystemRemediationState

The valid remediation states.  Host profile apply has two stages: precheck remediation and remediation. Precheck remediation generates task list and task requirement: apply may fail when task requirements are not satisfied. Remediation stage can be started only when precheck remediation succeeded.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The remediation or precheck remediation operation state.  See *HostSystemRemediationStateState_enum* for the valid values.  ***Since:*** vSphere API 6.7  | 
**operation_time** | **datetime** | For any \&quot;running\&quot; state, this is the starting time; for others, this is the completion time.  ***Since:*** vSphere API 6.7  | 

## Example

```python
from vmware_vi.models.host_system_remediation_state import HostSystemRemediationState

# TODO update the JSON string below
json = "{}"
# create an instance of HostSystemRemediationState from a JSON string
host_system_remediation_state_instance = HostSystemRemediationState.from_json(json)
# print the JSON string representation of the object
print HostSystemRemediationState.to_json()

# convert the object into a dict
host_system_remediation_state_dict = host_system_remediation_state_instance.to_dict()
# create an instance of HostSystemRemediationState from a dict
host_system_remediation_state_form_dict = host_system_remediation_state.from_dict(host_system_remediation_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


