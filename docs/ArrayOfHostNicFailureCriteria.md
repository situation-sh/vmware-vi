# ArrayOfHostNicFailureCriteria

A boxed array of *HostNicFailureCriteria*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNicFailureCriteria]**](HostNicFailureCriteria.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_nic_failure_criteria import ArrayOfHostNicFailureCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNicFailureCriteria from a JSON string
array_of_host_nic_failure_criteria_instance = ArrayOfHostNicFailureCriteria.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNicFailureCriteria.to_json()

# convert the object into a dict
array_of_host_nic_failure_criteria_dict = array_of_host_nic_failure_criteria_instance.to_dict()
# create an instance of ArrayOfHostNicFailureCriteria from a dict
array_of_host_nic_failure_criteria_form_dict = array_of_host_nic_failure_criteria.from_dict(array_of_host_nic_failure_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


