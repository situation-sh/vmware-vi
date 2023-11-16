# VsanNewPolicyBatch

NewPolicyBatch -- Structure to specify a list of object sizes and a policy for what-if analysis.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **List[int]** | Size (in bytes) of the objects.  ***Since:*** vSphere API 5.5  | [optional] 
**policy** | **str** | New policy in SPBM or VSAN expression format.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.vsan_new_policy_batch import VsanNewPolicyBatch

# TODO update the JSON string below
json = "{}"
# create an instance of VsanNewPolicyBatch from a JSON string
vsan_new_policy_batch_instance = VsanNewPolicyBatch.from_json(json)
# print the JSON string representation of the object
print VsanNewPolicyBatch.to_json()

# convert the object into a dict
vsan_new_policy_batch_dict = vsan_new_policy_batch_instance.to_dict()
# create an instance of VsanNewPolicyBatch from a dict
vsan_new_policy_batch_form_dict = vsan_new_policy_batch.from_dict(vsan_new_policy_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


