# ArrayOfVsanPolicyCost

A boxed array of *VsanPolicyCost*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VsanPolicyCost]**](VsanPolicyCost.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vsan_policy_cost import ArrayOfVsanPolicyCost

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVsanPolicyCost from a JSON string
array_of_vsan_policy_cost_instance = ArrayOfVsanPolicyCost.from_json(json)
# print the JSON string representation of the object
print ArrayOfVsanPolicyCost.to_json()

# convert the object into a dict
array_of_vsan_policy_cost_dict = array_of_vsan_policy_cost_instance.to_dict()
# create an instance of ArrayOfVsanPolicyCost from a dict
array_of_vsan_policy_cost_form_dict = array_of_vsan_policy_cost.from_dict(array_of_vsan_policy_cost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


