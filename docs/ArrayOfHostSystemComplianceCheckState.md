# ArrayOfHostSystemComplianceCheckState

A boxed array of *HostSystemComplianceCheckState*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostSystemComplianceCheckState]**](HostSystemComplianceCheckState.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_system_compliance_check_state import ArrayOfHostSystemComplianceCheckState

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostSystemComplianceCheckState from a JSON string
array_of_host_system_compliance_check_state_instance = ArrayOfHostSystemComplianceCheckState.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostSystemComplianceCheckState.to_json()

# convert the object into a dict
array_of_host_system_compliance_check_state_dict = array_of_host_system_compliance_check_state_instance.to_dict()
# create an instance of ArrayOfHostSystemComplianceCheckState from a dict
array_of_host_system_compliance_check_state_form_dict = array_of_host_system_compliance_check_state.from_dict(array_of_host_system_compliance_check_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


