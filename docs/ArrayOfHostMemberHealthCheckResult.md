# ArrayOfHostMemberHealthCheckResult

A boxed array of *HostMemberHealthCheckResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostMemberHealthCheckResult]**](HostMemberHealthCheckResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_member_health_check_result import ArrayOfHostMemberHealthCheckResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostMemberHealthCheckResult from a JSON string
array_of_host_member_health_check_result_instance = ArrayOfHostMemberHealthCheckResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostMemberHealthCheckResult.to_json()

# convert the object into a dict
array_of_host_member_health_check_result_dict = array_of_host_member_health_check_result_instance.to_dict()
# create an instance of ArrayOfHostMemberHealthCheckResult from a dict
array_of_host_member_health_check_result_form_dict = array_of_host_member_health_check_result.from_dict(array_of_host_member_health_check_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


