# ArrayOfVsanPolicyChangeBatch

A boxed array of *VsanPolicyChangeBatch*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VsanPolicyChangeBatch]**](VsanPolicyChangeBatch.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vsan_policy_change_batch import ArrayOfVsanPolicyChangeBatch

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVsanPolicyChangeBatch from a JSON string
array_of_vsan_policy_change_batch_instance = ArrayOfVsanPolicyChangeBatch.from_json(json)
# print the JSON string representation of the object
print ArrayOfVsanPolicyChangeBatch.to_json()

# convert the object into a dict
array_of_vsan_policy_change_batch_dict = array_of_vsan_policy_change_batch_instance.to_dict()
# create an instance of ArrayOfVsanPolicyChangeBatch from a dict
array_of_vsan_policy_change_batch_form_dict = array_of_vsan_policy_change_batch.from_dict(array_of_vsan_policy_change_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


