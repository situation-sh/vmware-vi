# ArrayOfHostSystemRemediationState

A boxed array of *HostSystemRemediationState*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostSystemRemediationState]**](HostSystemRemediationState.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_system_remediation_state import ArrayOfHostSystemRemediationState

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostSystemRemediationState from a JSON string
array_of_host_system_remediation_state_instance = ArrayOfHostSystemRemediationState.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostSystemRemediationState.to_json()

# convert the object into a dict
array_of_host_system_remediation_state_dict = array_of_host_system_remediation_state_instance.to_dict()
# create an instance of ArrayOfHostSystemRemediationState from a dict
array_of_host_system_remediation_state_form_dict = array_of_host_system_remediation_state.from_dict(array_of_host_system_remediation_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


