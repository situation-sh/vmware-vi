# ArrayOfDvsFilterPolicy

A boxed array of *DvsFilterPolicy*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DvsFilterPolicy]**](DvsFilterPolicy.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_filter_policy import ArrayOfDvsFilterPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDvsFilterPolicy from a JSON string
array_of_dvs_filter_policy_instance = ArrayOfDvsFilterPolicy.from_json(json)
# print the JSON string representation of the object
print ArrayOfDvsFilterPolicy.to_json()

# convert the object into a dict
array_of_dvs_filter_policy_dict = array_of_dvs_filter_policy_instance.to_dict()
# create an instance of ArrayOfDvsFilterPolicy from a dict
array_of_dvs_filter_policy_form_dict = array_of_dvs_filter_policy.from_dict(array_of_dvs_filter_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


