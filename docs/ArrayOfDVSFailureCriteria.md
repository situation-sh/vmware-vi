# ArrayOfDVSFailureCriteria

A boxed array of *DVSFailureCriteria*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DVSFailureCriteria]**](DVSFailureCriteria.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_failure_criteria import ArrayOfDVSFailureCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDVSFailureCriteria from a JSON string
array_of_dvs_failure_criteria_instance = ArrayOfDVSFailureCriteria.from_json(json)
# print the JSON string representation of the object
print ArrayOfDVSFailureCriteria.to_json()

# convert the object into a dict
array_of_dvs_failure_criteria_dict = array_of_dvs_failure_criteria_instance.to_dict()
# create an instance of ArrayOfDVSFailureCriteria from a dict
array_of_dvs_failure_criteria_form_dict = array_of_dvs_failure_criteria.from_dict(array_of_dvs_failure_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


