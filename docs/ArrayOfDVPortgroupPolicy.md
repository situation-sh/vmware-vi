# ArrayOfDVPortgroupPolicy

A boxed array of *DVPortgroupPolicy*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DVPortgroupPolicy]**](DVPortgroupPolicy.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dv_portgroup_policy import ArrayOfDVPortgroupPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDVPortgroupPolicy from a JSON string
array_of_dv_portgroup_policy_instance = ArrayOfDVPortgroupPolicy.from_json(json)
# print the JSON string representation of the object
print ArrayOfDVPortgroupPolicy.to_json()

# convert the object into a dict
array_of_dv_portgroup_policy_dict = array_of_dv_portgroup_policy_instance.to_dict()
# create an instance of ArrayOfDVPortgroupPolicy from a dict
array_of_dv_portgroup_policy_form_dict = array_of_dv_portgroup_policy.from_dict(array_of_dv_portgroup_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


