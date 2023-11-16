# VsanPolicyChangeBatch

PolicyChangeBatch -- Structure to specify a list of object uuids and a policy for what-if analysis.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **List[str]** | UUIDs of the objects.  ***Since:*** vSphere API 5.5  | [optional] 
**policy** | **str** | New policy in SPBM or VSAN expression format.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.vsan_policy_change_batch import VsanPolicyChangeBatch

# TODO update the JSON string below
json = "{}"
# create an instance of VsanPolicyChangeBatch from a JSON string
vsan_policy_change_batch_instance = VsanPolicyChangeBatch.from_json(json)
# print the JSON string representation of the object
print VsanPolicyChangeBatch.to_json()

# convert the object into a dict
vsan_policy_change_batch_dict = vsan_policy_change_batch_instance.to_dict()
# create an instance of VsanPolicyChangeBatch from a dict
vsan_policy_change_batch_form_dict = vsan_policy_change_batch.from_dict(vsan_policy_change_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


